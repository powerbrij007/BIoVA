"""
Generating truffle configuration file....
"""
import os
import subprocess

s_path=os.getcwd()

# result = subprocess.run(['hostname', '-I'], capture_output=True, text=True)
# output = result.stdout.strip()
# myIp=output.split()
# if len(myIp)==1:
#     output=myIp[0]
# else:
#     output=myIp[0]

fhand = open('host.txt')
output=""
# Loop through each line via file handler
for line in fhand:
  output=line.strip()


print(output)
s1='''module.exports = {
    networks: {
    development: {
    host: "'''
s2=output
s3='''",   
    port: 8545,            
    network_id: "*",       
    },
  },
  mocha: {
    // timeout: 100000
  },
  // Configure your compilers
  compilers: {
    solc: {
      version: "0.8.10",   
    } 
  },
};'''

setting= s1 + s2 + s3
with open('truffle-config.js','w') as f:
    f.write(setting)
f.close()

