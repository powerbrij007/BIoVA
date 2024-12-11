""" 
Program to connect and communicate with the blockchain
 """

#For connecting to blockchain
#=========== ABI section
import json
#Web3 connection
from web3 import Web3
import os

class Bconnect():
    w3=""
    address=""
    x=""
    contract_address=""
    newContract="" #instance of contract
    def __init__(self,address):
        #====Connecting to blockchain
       f=open('./abis/sample.json')
       abi=json.load(f)
       #print(abi)
       self.w3=Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))
       self.x=self.w3.isConnected()
       print("Blockchain Connection status....",self.x)
       #===Connecting to the network and getting first address
       user_number=input("Enter user number:[2-9]")
       self.address1=self.w3.eth.accounts[int(user_number)]
       print("Your address:",self.address1)
       print("Your balance:",self.w3.eth.get_balance(self.address1))
        #===============================Setting default account
       self.w3.eth.default_account=self.address1
       #=====To communicate to a contract we need 1)Contract address 2)contract abi
       self.contract_address="0x6dd6045F4f84254E16AaDB60eE360754639bbf74"
       #========= instantiating contract through the contract address
       self.newContract=self.w3.eth.contract(address=self.contract_address,abi=abi)
    
    def printIt(self):
        print("Status:",self.x)
    
    def buyChargeCall(self):
        msg=self.newContract.functions.buyCharge(10).transact()
        print("Transaction hash:",msg)
    



a=Bconnect("abc")
a.printIt()
a.buyChargeCall()
