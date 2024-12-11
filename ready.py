""" 
Automatic runCar.sh generator for the blockchain
What it needed:
1) Contract address
2) All user address
====
Car info
#-n for car name [BMW, Bez, AUDI,SUZ]
#-p for 4 integer values capacity status range timesToDrive 
# [BatteryCapacity, BatteryStatus, range,TimesToDrive]
#-u user address []
#-c contract address

[   n: network members
    1 Smart Parking
    n-1: vehicles]

 """



import os

#Web3 connection
from web3 import Web3
import subprocess
#===================================
import optparse

#create a parser object
parser = optparse.OptionParser()

#adding argument
parser.add_option("-c")

(options, args)=parser.parse_args()

#------------------- Contract address variable declaration
contractAddress=""

#Showing a meaningful address
if not options.c:
   #print("No argument is provided")
   parser.error("No argument is provided")
else:
    contractAddress=options.c
    

result = subprocess.run(['hostname', '-I'], capture_output=True, text=True)
output = result.stdout.strip()
myIp=output.split() #------------ It works in both cases wirless and wired
if len(myIp)==1:
    output=myIp[0]
else:
    output=myIp[0]
link="http://"+output+":8545"
#-------------------------------------
w3=Web3(Web3.HTTPProvider(link))
x=w3.is_connected()
print("Connection status....",x)
#====================================

#===Connecting to the network and getting first address
address=w3.eth.accounts
#print(len(address))

#============ Reading all private keys
privateKeys=[]
with open('privateKeys.txt') as f:
    contents=f.readlines()
    print(len(contents))
    for i in range(len(contents)):
        pk=contents[i].split(" ")
        pk2=pk[1].strip() #removes \n
        privateKeys.append(pk2)


#Get current working directory
s_path=os.getcwd()
cname=["BMW", "Bez", "AUDI","SUZ"]
#lst=[[30,15,250,12],[25,12,200,10],[40,20,300,9],[20,15,150,10]]
# [-p BatteryCapacity, BatteryStatus, range,TimesToDrive, groundClearance]
lst=['-p 30 15 250 20 200','-p 25 12 200 15 180','-p 40 20 300 15 230','-p 20 15 150 10 190']

#------------ pi
lstPi=['--p 30 15 250 20 200','--p 25 12 200 15 180','--p 40 20 300 15 230','--p 20 15 150 10 190']

#============== Contract Address Section
#contractAddress=input("Enter contract address:")
cAdd=" -c '"+contractAddress+"'"

#cAdd=" -c '0x1540b595885dF4022Cf9e0E9B03B12e48De171B9'"
cmd=""
initial1="#!/bin/bash"

#------ Smart Parking 
#====================== SmartParking
# Number of parking lots: z
# Number of parkonly: p
# ESC : Energy Storage Capacity: e
# SoC : Current Power Status: s
# Public key: u
# Private Key: k
# Smart Contract Address: c

#Private key is not included
#=======================
for i in range(1):
    spInitial="python SmartParking.py -z "+'30'+" -p "+'10'+" -e "+'200'+" -s "+'200'+" -u "+address[i]
    #spLast="; exec bash -i\"\n"
    cmd1=cmd+spInitial+cAdd+" -k "+ privateKeys[i]
#===================================== Server Script
initialSp=initial1+"\n"+cmd1
with open('runSp.sh','w') as f:
         f.write(initialSp)
f.close()

#  here len(address)-1: represents that the last address will be for pi 
for i in range(1,len(address)-1):
    firtsC="gnome-terminal --tab -- bash -c \"python cars.py -n "+str(cname[i%4])+" "+str(lst[i%4])+" -u "+address[i]+" -q "+ str(len(address) )
    lastC="; exec bash -i\"\n"
    cmd=cmd+firtsC+cAdd+" -k "+ privateKeys[i]+ lastC

#cmd=firtsC+cAdd+lastC
initial=initial1+"\n"+cmd
with open('runCar.sh','w') as f:
         f.write(initial)
f.close()

#=============================== Generating code for Pi
for i in range(len(address)-1,len(address)):
    firtsC="python cars.py -n "+str(cname[i%4])+" "+str(lstPi[i%4])+" -u "+address[i]+" -q "+ str(len(address) )
    lastC="\n"
    cmd=cmd+firtsC+cAdd+" -k "+ privateKeys[i]+ lastC

#cmd=firtsC+cAdd+lastC
initial=initial1+"\n"+cmd
with open('runCarPi.sh','w') as f:
         f.write(initial)
f.close()


#===================== Writing number of users to file
with open('1_DeploymentTime.txt', 'a') as f1:
     msg="\n Nodes:"+str(len(address))
     f1.write(msg)
     f1.close()

#=============Creating result folder
try: 

    os.mkdir("results")
except OSError as error: 
     #pass
     print(error)  
fName= "results"+str(len(address))
try:
    os.chdir("results")  
    os.mkdir(fName) 
except OSError as error: 
     #pass
     print(error)  