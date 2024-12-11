#Web3 connection
from web3 import Web3
import os
import subprocess
result = subprocess.run(['hostname', '-I'], capture_output=True, text=True)
output = result.stdout.strip()
myIp=output.split() #------------ It works in both cases wirless and wired
if len(myIp)==1:
    output=myIp[0]
else:
    output=myIp[0]

link="HTTP://"+output+":8545"
w3=Web3(Web3.HTTPProvider(link))
x=w3.is_connected()
print("Connection status....",x)

print(w3.eth.accounts)

#===== Getting all transactions done by an account
print(w3.eth.getTransactionCount(w3.eth.accounts[0]))

#====getting block numbers
print(w3.eth.block_number)
