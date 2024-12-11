'''
This program is used to find all the files and send it one-by-one for uploading

./runIpfs.sh fileName
'''
import os
import csv
import subprocess

#Step 1: Get current working directory
s_path=os.getcwd()
results=s_path+"/results"

#Step 2: Read all folder names
folders= os.listdir(results)
print("All folders:",folders)

#Step 3: Go inside each folder
for f in folders:
    folder=f
    fPath="results/"+str(folder)
    print("\n------------------------")
    print(fPath)
    files=os.listdir(fPath)
    print("------------------------")
    #print(files)
    for file in files:
        #print(file) #filename
        fadd=file
        add=fPath+"/"+fadd
        qury="./runIpfs.sh "+add
        subprocess.run(qury)

