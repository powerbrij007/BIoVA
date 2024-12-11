""" 
Program to connect and communicate with the blockchain
 """

#For connecting to blockchain
#=========== ABI section
import json
#Web3 connection
from web3 import Web3
import os

#import time module
import time

class Bc():
    w3=""
    address=""
    prvKey=""
    x=""
    contract_address=""
    newContract="" #instance of contract
    def __init__(self,User_add,prvKey,Cont_add,gClear):
        #====Connecting to blockchain
       f=open('./abis/smartParking.json') #manually feeded
       abi=json.load(f)
       #print(abi)
       self.w3=Web3(Web3.HTTPProvider('HTTP://127.0.0.1:8545'))
       self.x=self.w3.isConnected()
       print("Blockchain Connection status....",self.x)
       #===Connecting to the network and getting first address
       #user_number=input("Enter user number:[2-9]")
       #self.address1=self.w3.eth.accounts[int(user_number)]
       self.address1=Web3.to_checksum_address(User_add)
       self.prvKey=prvKey
       print("Your address:",self.address1)
       print("Your balance:",self.w3.eth.get_balance(self.address1))
        #===============================Setting default account
       self.w3.eth.default_account=self.address1
       #=====To communicate to a contract we need 1)Contract address 2)contract abi
       self.contract_address=Web3.to_checksum_address(Cont_add)
       #========= instantiating contract through the contract address
       self.newContract=self.w3.eth.contract(address=self.contract_address,abi=abi)
    
    def checkStatus(self):
        print("Status:",self.x)
    
    def buyChargeCall(self,amt):
        #record start time
        start = time.time()
        msg=self.newContract.functions.buyCharge(amt).transact()
        end=time.time()
        # print the difference between start
        # and end time in milli. secs
        print("Charging request time :",(end-start) * 10**3, "ms")
        print("Transaction hash:",msg)
        return msg
    
    #vehicleRegistration
        '''
        vAdd
        vName
        capacity
        gClear
        '''
    def registerVehicle(self,vAdd,vName,capacity,gClear):

    



#Account: 0x352AfD89eF8729928416Ecd992fc455AF25A8bB5
#privateKey: 0x2e191459a93557a0bf0591d7a1027e72b04b0ce9cd2c575e91e5fe869733f39d
#contract: 0x5F063c51D306296810943B42dd3376B4a0737E08

a=Bc('0x352AfD89eF8729928416Ecd992fc455AF25A8bB5','0x2e191459a93557a0bf0591d7a1027e72b04b0ce9cd2c575e91e5fe869733f39d','0x5F063c51D306296810943B42dd3376B4a0737E08')
a.printIt()

# uAdd='0x54c684278159c67d036aB8c07A87D7f962DA1Bfa'
# pKey='0xce477ad50757dd65b83969cdb17f207d77af409191e56a0023f3e05d69652783'
# cAdd='0xd5637dd9fd12ca3fa5b6855c31970be7d0f0d91b'
# a=Bc(uAdd,pKey,cAdd)
# a.printIt()
# a.buyChargeCall(12)
