#create a E_car
"""
Car Model: Name
Car Battery Capacity in KW
Car Current Battery status
Car Range in KM
Can cover range, on the basis of charge available
oneKm : power required for one Km (milage)


 [-p BatteryCapacity, BatteryStatus, range,TimesToDrive, groundClearance]
"""
 
import random
from math import floor

#-----Threading
import threading
 
 
#----Progress Bar
from time import sleep
from rich.progress import Progress
from rich.console import Console

#Server connection
import socket
import threading
#for client class
import clientClass

#============ portClass
import portClass

#For connecting to blockchain
#For connecting to blockchain
#=========== ABI section
import json
#Web3 connection
from web3 import Web3,exceptions
import os
import subprocess
#from eth_defi.event_reader.logresult import decode_log
#from web3-ethereum-defi import eth_defi.revert_reason

#import time module
import time
#import Bconnect

#MongoDB connection
#from transaction import Transactions


class E_car():
   vName=""
   EV_id=0
   carRange=0 #Range on full charging
   coverRange=0 #Range car can go
   oneKm=0 #Energy for one Km
   #===============================
   uAdd="" #user account
   privKey="" #users private key
   cAdd="" #Contract address
   w3="" #Web3 connection
   x="" #web3 connection parameter
   newContract="" #instance of Contract
   #==========================Battery
   b_type="" #Type of battery
   b_age=0 #in months from buy
   b_life=0 #in year 
   b_opt_temp=0 #battery operating temperature
   b_degradationFactor=0 #Degradation factor of battery
   b_power_output=0 #power output of battery [Discharge rate]
   b_cycle=0 #Number of times charge
   b_capacity=0 # in kWh
   b_status=0 # in %
   b_charged=0 #in kWh
   b_resistance_full=0 #Full charged battery resistance
   b_discharge_time=0 #Discharge time in hours
   b_charging_mode=['wired','wireless'] # [ Cabled, Wireless ]
   #=======================================EV
   values=[['normal',20], ['medium',60], ['heavy',130], ['very heavy',200]]
   userType=""
   dailyDrive=0
   suddenDrive=random.randint(0,50)
   #-------------------------
   carAge=0 #Age of EV
   carRange=0 #Range on full charging
   coverRange=0 #Range car can go
   oneKm=0 #Energy for one Km
   distanceTraveled=0 #Distance Traveled
   #==============================Ground Clearance
   groundClear=0 #ground clearance
   #===============================   Blockchain Connection 
   #========= Times to Run
   timeToRun=0
   #------------------ Number of user
   nUsers=0
   #------------------------ indicator
   ind=0
   #================== Policy indicators [Id of the policy owner owns]
   policyId=None
   balance=0
   old_balance=0
   #================= client-server
   serverIp=0
   rsuPort=0 #-------- to connect with RSU
 
   def __init__(self,name,b_capacity,b_status,carRange,timeToRun,gClear,uadd,privKey,cadd,nUsers):
       self.vName=name
       self.EV_id=random.choice(range(1,1000)) #== randomly creating an EV
       self.b_capacity= b_capacity
       self.b_status=b_status
       self.carRange=carRange
       self.oneKm = (self.b_capacity/self.carRange)
       self.groundClear=gClear
       #====Connecting to blockchain
       #self.uAdd=uadd
       #self.privKey=privKey
       #self.cAdd=cadd
       #self.bc=Bconnect.Bc(uAdd,privKey,cAdd,gClear)


       #===object creation client
       result = subprocess.run(['hostname', '-I'], capture_output=True, text=True)
       output = result.stdout.strip()
       myIp=output.split() #------------ It works in both cases wirless and wired
       if len(myIp)==1:
            output=myIp[0]
       else:
            output=myIp[0]
       self.client=clientClass.Clients(output,5051)
       self.rsu=portClass.portClass()
       self.serverIp=output
       print("Output:",output)
       print("Port:",self.client.client_Port)
       msg="i,"+self.vName+" New Status:"+str(self.b_status)
       self.client.send(msg)
       #=======mongoDb
       #self.mdb=Transactions()
       #============CarAge
       self.carAge=random.randint(1,8) #Years
       #=====================Battery Age
       self.b_age=random.randint(0,7) #years
       while self.carAge<self.b_age:
           self.b_age=random.randint(0,7) #years
       #======================= User Type
       uValue=random.randint(0,3) #User Type
       self.userType=self.values[uValue][0]
       self.dailyDrive=self.values[uValue][1]
       #==================Distance Traveled
       if self.userType=="normal":
           self.distanceTraveled= (self.dailyDrive + random.randint(1000,3000))*self.carAge
       elif self.userType=="medium":
           self.distanceTraveled= (self.dailyDrive+ random.randint(3000,5000))*self.carAge
       elif self.userType=="heavy":
           self.distanceTraveled= (self.dailyDrive + random.randint(3000,7000))*self.carAge
       else:
           self.distanceTraveled= (self.dailyDrive + random.randint(3000,10000))*self.carAge
       #===================== Blockchain Connection
        #====Connecting to blockchain
       f=open('./abis/v2v.json') #manually feeded
       abi=json.load(f)
       #print(abi)
       link= "HTTP://"+output+":8545"
       #self.w3=Web3(Web3.HTTPProvider('HTTP://127.0.0.1:8545'))
       self.w3=Web3(Web3.HTTPProvider(link))
       self.x=self.w3.is_connected()
       print("Blockchain Connection status....",self.x)
       #===Connecting to the network and getting first address
       #user_number=input("Enter user number:[2-9]")
       #self.address1=self.w3.eth.accounts[int(user_number)]
       self.uAdd=Web3.to_checksum_address(uadd)
       self.privKey=privKey
       print("Your address:",self.uAdd)
       print("Your balance:",self.w3.eth.get_balance(self.uAdd))
        #===============================Setting default account
       self.w3.eth.default_account=self.uAdd
       #=====To communicate to a contract we need 1)Contract address 2)contract abi
       self.cAdd=Web3.to_checksum_address(cadd)
       #========= instantiating contract through the contract address
       self.newContract=self.w3.eth.contract(address=self.cAdd,abi=abi)
       #============== Times to Run
       self.timeToRun = timeToRun
       #---------------------------------
       self.nUsers=nUsers
       #========================== Calling the function
       #self.timesToDriveEv() #---------running vehicle
       self.getRegister()
       print("------Waiting-----")
       time.sleep(3)
       #================================ Car becomes malicious
       if random.randint(1,10)==3:
           print("Malicious...")
           self.malicious()
       self.disconnect()
       self.client.close() #======= Closing older connection
       #======================== RSU Connect
       self.selectRSU()


    #=========== Taking to TA
    # i: for initialization of communication
    #v: vehicle
   #EV(_ID,_uAdd, _pKey,_certi, _NC, _T_exp,_status)
   def getRegister(self):
       ID=random.randint(1000,10000)
       msg= "r,v,"+str(ID) +","+str(self.uAdd)    #self.vName+" New Status:"+str(self.b_status)
       self.client.send(msg)
       #self.client.listen()
       print(self.client.receive())
       
#=========== user selects to be malicious
   def malicious(self):
       msg= "m,v,"+str(12)+","+str(self.uAdd)    #self.vName+" New Status:"+str(self.b_status)
       self.client.send(msg)
       #self.client.listen()
       print(self.client.receive())
       
   #============ disconnecting signal to server
   def disconnect(self):
       self.client.send("!DISCONNECT")
   #======================== Print Info    


   #=================== Connecting to RSUs
   #---------------------- select one RSU among all: requires RSU's and EV count
   def selectRSU(self):
       self.rsuPort=self.rsu.getRsuPort()
       self.client=clientClass.Clients(self.serverIp,int(self.rsuPort))
       msg= "r,v,12,"+str(self.uAdd)    #[ 0: call type, 1: vel/rsu, 2:ID, 3:address]
       self.client.send(msg)
       #self.client.listen()
       print(self.client.receive())

   def writePort(self,port):
        with open('rsuPort.csv', 'a') as f: 
           print(port, file=f)



   def getGasConsumed(self,functionName,tx,tym):
       receipt = self.w3.eth.wait_for_transaction_receipt(tx)
       gas_used = receipt['gasUsed']
       print("Function:",functionName," Gas used:",gas_used, " Time:", tym)
   
   def getBidding(self):
        rs = self.newContract.functions.biddingRequirements().call()
        print("Result: ",rs)
       
       


   def submitCredentialsFunction(self):
       start = time.time()
       tx=self.newContract.functions.submitCredentials("hello").transact()
       #msg = fetch_transaction_revert_reason(Web3,self.newContract.functions.vehicleRegistration(self.uAdd,self.vName,self.b_capacity,self.groundClear).transact())
       end=time.time()
       exeTime=(end-start) * 10**3
       #print("Vehicle registration time :",(end-start) * 10**3, "ms")
       #self.transactionDetails("evRegistration",exeTime,tx,0)
       self.transactionRecorder("SubmitCredentials",exeTime,tx,0)
       self.getGasConsumed("Submit Credentials",tx,exeTime)
       #self.transactionRecorder("Credential Submittion",exeTime,tx,0)


   def placeBid(self):
       start = time.time()
       bidAmount=random.choice(range(800,1000))
       tx=self.newContract.functions.placeBid(bidAmount).transact()
       #msg = fetch_transaction_revert_reason(Web3,self.newContract.functions.vehicleRegistration(self.uAdd,self.vName,self.b_capacity,self.groundClear).transact())
       end=time.time()
       exeTime=(end-start) * 10**3
       #print("Vehicle registration time :",(end-start) * 10**3, "ms")
       #self.transactionDetails("evRegistration",exeTime,tx,0)
       self.transactionRecorder("Place Bid",exeTime,tx,bidAmount)
       self.getGasConsumed("placeBid",tx,exeTime)
       #self.transactionRecorder("Credential Submittion",exeTime,tx,0)       

    #======== To registering the vehicle with smart contract
    #---- need to cheack that this function can only be called once
   def evRegister(self):
       #record start time
        rs = self.newContract.functions.checkRegistration(self.uAdd).call()
        print("Result: ",rs)
        msg=""
        if(rs==True):
            print("Address already registered.")
        else:
            start = time.time()
            tx=self.newContract.functions.registration(self.uAdd).transact()
            #msg = fetch_transaction_revert_reason(Web3,self.newContract.functions.vehicleRegistration(self.uAdd,self.vName,self.b_capacity,self.groundClear).transact())
            end=time.time()
            exeTime=(end-start) * 10**3
            #print("Vehicle registration time :",(end-start) * 10**3, "ms")
            #self.transactionDetails("evRegistration",exeTime,tx,0)
            #self.getGasConsumed("Registration",tx)
            self.transactionRecorder("User registration",exeTime,tx,0)
            #============== Adding vehicle
            #EV_id=random.choice(range(1,100))
            start = time.time()
            tx=self.newContract.functions.addVehicle(self.uAdd,self.vName,self.EV_id).transact()
            #msg = fetch_transaction_revert_reason(Web3,self.newContract.functions.vehicleRegistration(self.uAdd,self.vName,self.b_capacity,self.groundClear).transact())
            end=time.time()
            exeTime=(end-start) * 10**3
            print("Vehicle registration time :",(end-start) * 10**3, "ms")
            #self.transactionDetails("addingVehicle",exeTime,tx,0)
            #self.getGasConsumed("Add Vehicle",tx)
            self.transactionRecorder("Vehicel adding",exeTime,tx,0)
            #print("Transaction hash:",msg)
            #print("Transaction hash:",self.w3.eth.wait_for_transaction_receipt(msg))
            #print("Transaction hash:",self.w3.eth.get_transaction_receipt(msg))

   def toEther(self,value):
       return self.w3.from_wei(value,'ether')
       
   def info(self): #1
       print("Name:",self.vName)
       print("EV_id:",self.EV_id)
       print("Address:",self.uAdd)
       print("Balance:",self.toEther(self.w3.eth.get_balance(self.uAdd)))
       print("Contract Add:",self.cAdd)
       print("Contract balance:",self.toEther(self.w3.eth.get_balance(self.cAdd)))
       #print("Battery Capacity:",self.b_capacity,"kWh")
       #print("Battery Status:",self.b_status ,"kWh")
       #print("Car Range: ",self.carRange,"Km")
       self.coverRange = floor((1/self.b_capacity)*self.b_status*self.carRange)
       print("Distance can go:",self.coverRange ,"Km")
 
   def canGo(self,dist): #Distance car can cover 2
       self.b_status=self.b_status-(dist*self.oneKm)
       self.coverRange = floor(((1/self.b_capacity)*self.b_status*self.carRange))
       #print(">>",self.coverRange)
       return int(self.coverRange)
 
 
   def drive(self): #it will drive the car 3
       #d=self.canGo(0)
       print("---Driving----")
       if(self.b_status>2):   
           dist=random.randint(5,self.coverRange)
           console=Console()
           with console.status("[bold green]Driving car...") as status:
               sleep(1)
           print("Distance traveled:",dist,"Km")
           print("Can go:",self.canGo(dist),"Km")
           print("Battery Status:",self.b_status,"kWh")
           print("--------------")
           #self.info()
       else:
           print("Not enough charge!!")
           time.sleep(random.randint(3,7))
           #self.paymentSettlement()
           print("=====================")
           self.info()
 
        

#--------------------- buy policy
   def buyPolicy(self):
       #self.transactionRecorder("Balance Before policy buying",0,0,self.toEther(self.w3.eth.get_balance(self.uAdd)))
       #============== Reading policies
       #record start time
       tx_hash=""
       policyList=[]
       start = time.time()
       policyList=self.newContract.functions.getPolicies().call()
       end=time.time()
       self.policyId=policyList[0][0]
       #difference between start end time in milli. secs
       print("policyList=",policyList[0][0])
       exeTime=(end-start) * 10**3
       #print("Policies reading time:",(end-start) * 10**3, "ms")
       self.transactionRecorder("Reading policy",exeTime,tx_hash,0)
       #return tx
       #self.transactionDetails("Reading policies",exeTime,tx,0)
       vehicleList=[]
       start = time.time()
       vehicleList=self.newContract.functions.getVehicle(self.uAdd,self.EV_id).call()
       end=time.time()
       #difference between start end time in milli. secs
       print("Vehicle Details=",vehicleList)
       exeTime=(end-start) * 10**3
       #print("Reading vehicle time:",(end-start) * 10**3, "ms")
       self.transactionRecorder("Reading vehicle",exeTime,tx_hash,0)
       
       #===================Reading policy buying
       start = time.time()       
       #record start time
       transaction = self.newContract.functions.buyPolicy(self.uAdd,self.EV_id,policyList[0][0]).build_transaction({
       'from': self.uAdd,
       'value': self.w3.to_wei(10, 'ether'),  # Amount of Ether to deposit (in wei)
       'gas': 2000000,  # Adjust the gas limit as needed
       'gasPrice': self.w3.to_wei('50', 'gwei'),  # Adjust the gas price as needed
       'nonce': self.w3.eth.get_transaction_count(self.uAdd),
       })

       # Sign the transaction
       signed_txn = self.w3.eth.account.sign_transaction(transaction, self.privKey)

        # Send the transaction
       try:
           tx_hash = self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
           end=time.time()
           #print("Buying policy:",(end-start) * 10**3, "ms")
       except Exception as e:
           print("Error in sending money.",e)
        # Wait for the transaction to be mined
       #tx_receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)
       #print("Transaction receipt:", tx_receipt)
       #self.getGasConsumed("Buying policy",tx_hash)
       exeTime=(end-start) * 10**3
       self.transactionRecorder("Buying policy",exeTime,tx_hash,10)

#========= check policy status [ 0: None, 1: Active, 2: Expired]
   def policyStatus(self):
       #============== Reading policies
       #record start time
       tx_hash=""
       start = time.time()
       try:
           policy_status=self.newContract.functions.getPolicyStatus(self.uAdd,self.EV_id).call()
       except Exception as e:
           print("Error while reading status..",e)
           policy_status=0
       end=time.time()
       #difference between start end time in milli. secs
       print("Policy status=",policy_status)
       exeTime=(end-start) * 10**3
       #print("Policies reading time:",(end-start) * 10**3, "ms")
       self.transactionRecorder("Checking policy status",exeTime,tx_hash,0)
       return policy_status
       
   def whoIam(self):
       tx_hash=""
       start = time.time()
       try:
           policy_status=self.newContract.functions.returnMe().call()
       except Exception as e:
           print("Error while reading status..",e)
           policy_status=0
       end=time.time()
       #difference between start end time in milli. secs
       print("My Address=",policy_status)
       exeTime=(end-start) * 10**3
       #print("Policies reading time:",(end-start) * 10**3, "ms")
       self.transactionRecorder("Address Checking",exeTime,tx_hash,0)
       return policy_status
       

#-------------------------- Renew policy
   def renewPolicy(self):
       #============== Reading policies
       #record start time
       tx_hash=""     
       #===================Reading policy buying
       start = time.time()       
       #record start time
       transaction = self.newContract.functions.renewPolicy(self.uAdd,self.EV_id,self.policyId).build_transaction({
       'from': self.uAdd,
       'value': self.w3.to_wei(10, 'ether'),  # Amount of Ether to deposit (in wei)
       'gas': 2000000,  # Adjust the gas limit as needed
       'gasPrice': self.w3.to_wei('50', 'gwei'),  # Adjust the gas price as needed
       'nonce': self.w3.eth.get_transaction_count(self.uAdd),
       })

       # Sign the transaction
       signed_txn = self.w3.eth.account.sign_transaction(transaction, self.privKey)

        # Send the transaction
       try:
           tx_hash = self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
           end=time.time()
           exeTime=(end-start) * 10**3
           #print("Buying policy:",(end-start) * 10**3, "ms")
       except Exception as e:
           print("Error in sending money.",e)
        # Wait for the transaction to be mined
       #tx_receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)
       #print("Transaction receipt:", tx_receipt)
       #self.getGasConsumed("Buying policy",tx_hash)
       self.transactionRecorder("Renewing policy",exeTime,tx_hash,10)



    #============================ for getting transaction details [ Normal File]
   def transactionRecorder(self,functionName,exeTime,tx,value):
        fPath="results/results"+str(self.nUsers)
        if functionName =="Claiming policy" or functionName=="Renewing policy":
            fPath1=fPath+"/Transactions.csv"
        else:
            fPath1=fPath+"/allTransactions.csv"
        data=[]
        if tx!="":
            data=self.w3.eth.wait_for_transaction_receipt(tx)
        else:
            data = {'from' : self.uAdd, 'to': self.cAdd, 'gasUsed':0}
        with open(fPath1, 'a') as f:
            print(functionName,",",data['from'],",",data['to'],",",exeTime,",",data['gasUsed'],",",value,",",self.toEther(self.w3.eth.get_balance(self.uAdd)),",",self.toEther(self.w3.eth.get_balance(self.cAdd)), file=f)

   
   
   

#-------------------- claiming for the insurance
# '''
# To claim for the insurance a user needs:
# 1. Address
# 2. Contract address
# 3. Electric vehicle id
# 4. Policy id
#- initiate claim
#- smart contract will identify 
# '''

   def claimInsurance(self,address,EV_id,policy_id):
       #============== Reading policies id
       #record start time
       tx_hash=""
       policyHolderList=[]
       start = time.time()
       #========================== Reading a public mapping
       policyHolderList=self.newContract.functions.policyHolder(self.uAdd,self.EV_id).call()
       end=time.time()
       #difference between start end time in milli. secs
       print("policy holder list=",policyHolderList)
       exeTime=(end-start) * 10**3
       #print("Policies reading time:",(end-start) * 10**3, "ms")
       self.transactionRecorder("Reading policy holder",exeTime,tx_hash,0)

       #record start time
       tx_hash=""
       start = time.time()
       try:
           tx_hash=self.newContract.functions.claim(self.uAdd,self.EV_id).transact()
       except Exception as e:
           print("Claiming error:",e)
       #difference between start end time in milli. secs
       #print("policyList=",tx_hash)
       end=time.time()
       exeTime=(end-start) * 10**3
       #print("Policies reading time:",(end-start) * 10**3, "ms")
       self.transactionRecorder("Claiming policy",exeTime,tx_hash,0)


#---------------- Transfering the ownership # updateOwner
   def transferInsuranceAsAsset(self):
       #============== 
       #record start time
       newAddress=input("Enter newowner address:")
       print("To transfer address:",newAddress)
       tx_hash=""
       start = time.time()
       #========================== Transferring the ownership
       try:
         trans=self.newContract.functions.updateOwner(self.uAdd,newAddress,self.vName,self.EV_id).transact()
       except Exception as e:
           print("Transfer errot:",e)
       
       end=time.time()
       #difference between start end time in milli. secs
       print("transaction=",trans)
       exeTime=(end-start) * 10**3
       #print("Policies reading time:",(end-start) * 10**3, "ms")
       self.transactionRecorder("OwnerTransfer",exeTime,tx_hash,0)

   def readingVehicles(self): 
       #-------------------- reading new owner list
       tx_hash=""
       vehicleList=[]
       vehicleList.clear()
       start = time.time()
       vehicleList=self.newContract.functions.vRegistere(self.uAdd,self.EV_id).call()
       end=time.time()
       #difference between start end time in milli. secs
       print("Updated vehicle list=",vehicleList)
       exeTime=(end-start) * 10**3
       #print("Reading vehicle time:",(end-start) * 10**3, "ms")
       self.transactionRecorder("Reading vehicle",exeTime,tx_hash,0)
   
       #============================ for getting transaction details [ CSV ]
   def transactionDetails(self,funcName,exeTime,tx,demand):
       fPath="results/results"+str(self.nUsers)
       fPath1=fPath+"/allTransactions.csv"
       data=self.w3.eth.wait_for_transaction_receipt(tx)
       if funcName=="evRegistration":
           fPath=fPath+"/evRegistration.csv"
       elif funcName=="requestCreation":
           #================================================ Recording the EV demands
           chargingDemand=fPath+"/chargingDemand.csv"
           with open(chargingDemand, 'a') as f:
               print(funcName,",",data['from'],",",data['to'],",",exeTime,",",data['gasUsed'],",",demand, file=f)
           fPath=fPath+"/requestCreation.csv"
       elif funcName=="parkingAllocation":
           fPath=fPath+"/parkingAllocation.csv"
       elif funcName=="vehicleParked":
           fPath=fPath+"/vehicleParked.csv"
       elif funcName=="parkingStatusUpdate":
           fPath=fPath+"/parkingStatusUpdate.csv"
       else: #funcName=="paymentSettlement"
           fPath=fPath+"/paymentSettlement.csv"
        
       with open(fPath, 'a') as f:
          print(funcName,",",data['from'],",",data['to'],",",exeTime,",",data['gasUsed'], file=f)
       
       #========================== All Transactions in a file
       with open(fPath1,'a') as f:
           if demand !=0:
               print(funcName,",",data['from'],",",data['to'],",",exeTime,",",data['gasUsed'], file=f)
           else:
               print(funcName,",",data['from'],",",data['to'],",",exeTime,",",data['gasUsed'],",",demand, file=f)
           
     
           
    #    with open('file.txt', 'a') as f:
    #        print(funcName,",",data['from'],",",data['to'],",",exeTime,",",data['gasUsed'], file=f)
    #        #print(funcName,",",data['transactionHash'],",",data['from'],",",data['to'],",",exeTime,",",data['gasUsed'], file=f)
    #        if self.ind == 0:
        #     print("Function ","| Transaction hash ","| from ","| to ","| execution time ","| Gas Used ")
        #     print(funcName,",",data['transactionHash'],",",data['from'],",",data['to'],",",exeTime,",",data['gasUsed'], file=f)
        #    else:
        #     print(funcName,",",data['transactionHash'],",",data['from'],",",data['to'],",",exeTime,",",data['gasUsed'], file=f)
            
           
       #print("Transaction details:", self.w3.eth.get_transaction_receipt(tx))
 
       #print("Transaction hash:",data)
       #print("Function:",funcName,"Transaction hash:",data['transactionHash'],"from: ",data['from'],"to: ",data['to'],"execution time:",exeTime,"ms","Gas Used:",data['gasUsed'])
   
   def writeToTextFile(self):
        # Append to file using the write() method
        with open('file.txt', 'a') as f:
            f.write('I am appended text\n')
            
   #========================== Generating Sensory data 
   def collectData(self):
        pass   
   


#============================================== Vehicle section
    #Number of times the EV will be drive
   def timesToDriveEv(self):
       self.info()
       self.evRegister()
       self.buyPolicy()
       self.info()
       lucky1=random.choice(range(0,30))
       while(lucky1>2): 
            lucky=random.choice(range(0,50))   
            if lucky<3:
                print("Claiming:")
                self.claimInsurance(self.uAdd,self.EV_id,0)
                sleep(random.choice(range(0,20)))
                self.info()
            if int(self.policyStatus())==2:
                self.renewPolicy() #self.uAdd,self.EV_id,self.policyId
                print("Policy renewed..")
                self.info()
            lucky1-=1

       transfer=input("Want to transfer(y/n):")
       if transfer=='y':
           self.transferInsuranceAsAsset()
       self.readingVehicles()
       self.whoIam()
       #self.paymentSettlement()
    #    print("Drive:", self.timeToRun)
    #    while(self.timeToRun>0):
    #        self.drive()
    #        self.timeToRun-=1
       #------------------------ Terminates the program[ Comment it if you want to see results]    
       exit() 


