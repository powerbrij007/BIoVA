import os

s_path=os.getcwd()

#Reading all contract names
contractAddress=s_path+"/contracts"
contractNames=os.listdir(contractAddress)
#print(contractAddress)
#print(contractNames)

#migration section
migrateAt=s_path+"/migrations"

varString="" #for storing variables
deployString="" #For storing Strings

migrationString=""

#========= Writing abi to a file
import json
for contract in contractNames:
    cName = contract.split(".") #extracting only contract name
    varString= varString + '''const {0} = artifacts.require("{0}"); \n'''.format(cName[0])
    deployString= deployString + '''deployer.deploy({0});\n'''.format(cName[0])
   

migrationString= varString + " module.exports = function (deployer){\n" + deployString + " };"

os.chdir(migrateAt)  
with open('1_initial_migration.js', 'w') as f:
  f.write(migrationString)

f.close()
