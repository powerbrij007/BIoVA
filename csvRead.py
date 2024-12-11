#========== This file will read the All the CSVs in folder results
'''
Step 1: Go inside folder : results
Step 2: Read all folder names
Step 3: Go inside each folder
Step 4: Read each file
Step 5: Calculate average of [ executionTime, gasBurn]
'''
import os
import csv

#Step 1: Get current working directory
s_path=os.getcwd()
results=s_path+"/results"

#Step 2: Read all folder names
folders= os.listdir(results)
print("All folders:",folders)

#====================
def transactionRecorder(fileName,functionName,time_max,gas_max):
        fPath1="rs/ressult.csv"
        with open(fPath1, 'a') as f:
            print(fileName,",",functionName,",",time_max,",",gas_max,",",file=f)


functionName=[]
#Step 3: Go inside each folder
for f in folders:
    folder=f
    fPath="results/"+str(folder)
    print("FilePAth:",fPath)
    print("\n------------------------")
    #print(fPath)
    files=os.listdir(fPath)
    print(files)
    print("------------------------")
    # #print(files)
    for file in files:
        #print(file) #filename
        fadd=file
        add=fPath+"/"+fadd
        #------------------ Reading function names
        with open(add,newline='') as csvfile:
            #-- Reading csv file
            csvFile=csv.reader(csvfile)
            for line in csvFile:
                if line[0] not in functionName:
                    functionName.append(line[0])
    #print("Function Name=",functionName)

        #print(files)

    for file in files:
        # time_max=0.0
        # time_mini=0.0
        # gas_max=0.0
        # gas_mini=0.0
        for name in functionName:
            with open(add,newline='') as csvfile:
                #reading each line
                    csvFile=csv.reader(csvfile)  #-- Reading csv file
                    time_max=0.0
                    time_mini=0.0
                    gas_max=0.0
                    gas_mini=0.0
                    for line in csvFile:
                        # print(line[3]) #Time
                        # print(line[4]) #Gas
                        #print("For name",name)
                        if name==line[0]:
                            #print(name)
                            if float(line[3])>time_max:
                                time_max=float(line[3])

                            if float(line[4])>gas_max:
                                gas_max=float(line[4])

                    print("functin:",name)
                    print("time_Max:",time_max)
                    print("gas_Max:",gas_max)
                    transactionRecorder(str(folder),name,time_max,gas_max)







