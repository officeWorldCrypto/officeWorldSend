
from decouple import config
from web3 import Web3
import json
import sys
import time

print('Starting transferences process...')

# if not indicated destinationor value, 
# use default wallet for receive
valueSend = int(config('DEFAULT_MINIMAL_VALUE'))
to_address= config('DEFAULT_TO')

# two parameters, example 
# python3 send.py 170 0x6E375FB9e52418A92Aa2A6BaAC0a329cb1f332Bf
# this example send 170 OFF to address ^
print('Number of arguments: {}'.format(len(sys.argv)))
print('Argument(s) passed: {}'.format(str(sys.argv)))

# first argument (value)
if (sys.argv[1]):
	valueSend = int(sys.argv[1])

# second argument (account/wallet metamask address)
if (sys.argv[2]):
	to_address = sys.argv[2]

SENDER_WALLET = config('SENDER_WALLET')
SENDER_WALLET_SECRET_KEY = config('SENDER_WALLET_SECRET_KEY')
CONTRACT_ADDRESS = config('CONTRACT_ADDRESS')
MONEY_DIGITS = config('MONEY_DIGITS')
DEBUG = config('DEBUG')

# Data
contract_address = CONTRACT_ADDRESS
privatekey = SENDER_WALLET_SECRET_KEY
me = SENDER_WALLET

# Conversion for digits lenght
convertion_value = int('1'+('0'*int(MONEY_DIGITS)))

if DEBUG:
	# testnet: development
	chainid = 97
	bsc = "https://data-seed-prebsc-1-s1.binance.org:8545/"
else:
	# default: production
	chainid = 57
	bsc = "https://bsc-dataseed.binance.org/"

web3 = Web3(Web3.HTTPProvider(bsc))
isConnected = web3.isConnected()

if isConnected:	
	with open('assets/abi.json', 'r') as file:
		data_abi = file.read().replace('\n', '')
	abi = json.loads( data_abi )

	contract = web3.eth.contract(address=contract_address, abi=abi)
	totalSupply = contract.functions.totalSupply().call()
	totalSupply = totalSupply / convertion_value;

	print('Token informations and Total supply (token)')
	print(totalSupply)
	print(contract.functions.name().call())
	print(contract.functions.symbol().call())

	print('Receiver informations')
	balanceOf = contract.functions.balanceOf(to_address).call()
	print('Actual balance (destinatary)')
	print(balanceOf/convertion_value)

	print('Amount sending (efective value)')
	print(valueSend)
	print('Amount converted for sending (value)')
	amount = valueSend * convertion_value  #web3.toWei(send, 'ether')
	print(amount)

	print('Transaction order')
	nonce = web3.eth.getTransactionCount(me)
	print(nonce)
	print('Prepating transaction')
	token_tx = contract.functions.transfer(to_address, amount).buildTransaction({
		'chainId':chainid, 
		'gas': 100000,
		'gasPrice': web3.toWei('10','gwei'), 
		'nonce':nonce
	})
	print('Processing transaction, starting')
	sign_txn = web3.eth.account.signTransaction(token_tx, private_key=privatekey)
	web3.eth.sendRawTransaction(sign_txn.rawTransaction)
	print("Transaction has been sent to address")
	print(to_address)
	print("Transaction resume")
	print(token_tx)
	print('Are new balance value now, waiting 10secs...')
	print('Actual balance (destinatary)')
	for i in range(10):
		time.sleep(1)
		balanceOf = contract.functions.balanceOf(to_address).call()
		print(balanceOf/convertion_value)

print('===[ End of process, all done ]===')
