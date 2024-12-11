import os
import json

#Get current working directory
s_path=os.getcwd()

#Reading all contracts
contractAddress=s_path+"/build/contracts"
#Reading all contract names
contractNames=os.listdir(contractAddress)


#====Writing ABIs
abiStorePath=s_path+"/abis"

#Checking is directory already exist
if os.path.isdir(abiStorePath):
    pass
else:
    os.mkdir(abiStorePath)

for contract in contractNames:
    addr=s_path+'/build/contracts/'+contract
    f=open(addr)
    abis=json.load(f)
    fname=contract.split(".")
    fName=fname[0] + ".json"
    os.chdir(abiStorePath)
    with open(fName,'w') as f1:
        json.dump(abis['abi'],f1)
    f.close()
    f1.close()
    os.chdir(s_path)