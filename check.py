# Checking the connection of Ganache

#Web3 connection
from web3 import Web3
import subprocess

result = subprocess.run(['hostname', '-I'], capture_output=True, text=True)
output = result.stdout.strip()
myIp=output.split() #------------ It works in both cases wirless and wired
if len(myIp)==1:
    output=myIp[0]
else:
    output=myIp[0]
link="http://"+output+':8545'
print(link)
#-------------------------------------
w3=Web3(Web3.HTTPProvider(link))
x=w3.is_connected()
print("Connection status....",x)