## officeWorldSend

Send crypto value to another account/wallet
This software are used for send money in withdraw operations

## Usage
    python3 send.py **value** **wallet_address**

        python3 send.py 700 0xf954D12D577cE8373F4Bf924B3DEA71B1Db785B3

Todo: For more protection, this need request a authorization for verify authenticity of operation with internal workspace block validation

This resource depends only assets/abi.json and correct settings like this:

## Configurations file (.env)

DEBUG=True
----------
If in true mode setup to use binance chain alternative testnet

TEMPLATE_DEBUG=True
-------------------
Necessary only future options with debug alternative, but with DEBUG parameter like false

CONTRACT_ADDRESS
----------------
Here is your token contract (OFF tests='0x3AF47F702a9002a4583830253b1A0b0BeAb15340')

SENDER_WALLET ='0xf954D12D577cE8373F4Bf924B3DEA71B1Db785B3'
-----------------------------------------------------------
The money has get here and sended to destination

SENDER_WALLET_SECRET_KEY
------------------------
Save your financial life, protect this information, this private_key
get in metamask wallet for example, and this is necessary for send money
'0000000000000000000000000000000000000000000000000000000000000000'

MONEY_DIGITS=8
--------------
Parameters indication the digits qty has used in your token
Warning: if you put wrong information here, yout can send 10.000 also 10

DEFAULT_TO="0x0000000000000000000000000000000000000000"
---------------------------------------------------------
A default wallet for use if wallet has no indicated

DEFAULT_MINIMAL_VALUE=1
-----------------------
A default value for send when run this code

