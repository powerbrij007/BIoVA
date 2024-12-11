from solcx import compile_source, install_solc
install_solc("0.8.17")
compiled_solidity=compile_source('''
// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.0;

contract helloPython{

     struct vehicle{
        address vAdd; //address of vehicle
        uint demand; //demand of vehicle
        //uint lastReq; //last request made
        uint report_time; //report time of vrhivlr
    }

    //Event section
    event requester(address _uAdd, uint req);
    mapping(uint=>vehicle) public vehicles;
    uint public vehicleCount=0; //counts the number of vehicles
    
    //Vehicle request for charging with address and required amount
    function request(address _vAdd,uint req) public {            
            vehicles[vehicleCount]=vehicle(_vAdd,req,block.timestamp+50);
            emit requester(_vAdd,req);
    }
    function responseOfRequest() public returns(vehicle memory){
        vehicleCount+=1;
        return vehicles[vehicleCount-1];
    }


}
''',output_values=['abi','bin'])

#print(compiled_solidity)
print(compiled_solidity)
contract_id,contract_interface=compiled_solidity.popitem()

#print(contract_id)

#print(contract_interface)


#print(contract_interface['abi'])
abi=contract_interface['abi']

#print(contract_interface['bin'])
bin=contract_interface['bin']

#========= Writing abi to a file
import json
with open('abi.json', 'w') as f:
    json.dump(contract_interface['abi'], f)

f.close()
#========= Writing abi to a file End




#Web3 connection
from web3 import Web3
import os
w3=Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))
x=w3.isConnected()
print("Connection status....",x)
#====================================

#===Connecting to the network and getting first address
address1=w3.eth.accounts[0]
print("Address 1:",address1)
#===============================Setting default account
w3.eth.default_account=address1

#====Deploying contract
contract_hello=w3.eth.contract(abi=abi,bytecode=bin)
print("Deploying contract....\n",contract_hello)

#============calling the constructor
#[ To perform transaction default account is required.]
tx=contract_hello.constructor().transact()
print(tx)

#===== Transaction receipt
tx_receipt =w3.eth.wait_for_transaction_receipt(tx)
print(tx_receipt)

#print(tx_receipt['blockNumber'])
print("=========================")

#=====getting contract address
contract_address=tx_receipt['contractAddress']

#========= instantiating contract through the contract address
newContract=w3.eth.contract(address=contract_address,abi=abi)

msg=newContract.functions.request(address1,12).transact()
print(msg)
print("=========================Calling function====")

msg=newContract.functions.responseOfRequest().call()
print(msg[1])


msg=newContract.functions.vehicleCount().call()
print(msg)



#print(tx_receipt_request)

#msg=newContract.functions.report(address1).call()
#print(msg)

