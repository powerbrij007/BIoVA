""" 
Sending money from one user to another user.
Payment gateway for blockchain
 """


#For connecting to blockchain
#=========== ABI section
import json

import os
import subprocess

#Web3 connection
from web3 import Web3
import os
w3=Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))
x=w3.isConnected()
print("Connection status....",x)
#====================================

#===Connecting to the network and getting first address
address=w3.eth.accounts

#========== Total number of address
print("Total address:",type(address), len(address))

#============
adds=w3.eth.getAccounts()
print(adds)

mnemonic = "choose excite cage want perfect practice spy motion possible mule involve close"
HD_PATH="m/44'/60'/0'/0/account_index"
rpc="HTTP://127.0.0.1:7545"


# sender="0x0b060621f174035E9aD7798589d1de0ab9E6ebf3"
# receiver="0x56BeC9185A32dbC9e225A2D42aDF10A3d5d92fd7"
# amt=int(input("Amount to send= "))
# contract_address="0x9a6744299a8895c9e54af8d56de89297756B543B"

# f=open('./abis/sendmoney.json') #manually feeded
# abi=json.load(f)

# newContract=w3.eth.contract(address=contract_address,abi=abi)
# val=newContract.functions.myBalance(sender).call()
# print(val)
# val=w3.fromWei(val,"ether")
# print(val)
# newContract.functions.depositeMoney(receiver,amt).transact()
