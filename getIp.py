import subprocess

class getIp:
    def myIp(self):
       result = subprocess.run(['hostname', '-I'], capture_output=True, text=True)
       output = result.stdout.strip()
       myIp=output.split() #------------ It works in both cases wirless and wired
       print(myIp)
       if len(myIp)==1:
            output=myIp[0]
       else:
            output=myIp[0]
       
       return output

myIp=getIp()
print("IP=",myIp.myIp())