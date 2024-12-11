#!/bin/bash
#- Extract the output of truffle deploye command
#- get smart contract address from it

truffle deploye>smartcontract.txt
#sAdd=$(cat smartcontract.txt| grep 'address:' | awk -F':' '{print $2}')

sAdd=`cat smartcontract.txt| grep 'address:' | awk -F':' '{print $2}'`
echo $sAdd

gas=`cat smartcontract.txt| grep 'used:' | awk -F':' '{print $2}'`
echo $gas