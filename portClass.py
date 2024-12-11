'''
portClass: Write port to a file
- Read all ports
- Selects a random RSU to connect 
'''


import os
import csv
import random


class portClass:
    rsuPorts=[]

    def __init__(self):
        pass

    #Writing port to file
    def writePortRsu(self,rsuPort):
        try:
            with open('rsuPort.csv', 'w') as f1:
                print(rsuPort,file=f1)
        except OSError as error:
            print(error)

    #Writing port to file
    def clearPortrsu(self):
        try:
            with open('rsuPort.csv', 'w') as f1:
                f1.close()
        except OSError as error:
            print(error)


    #Writing port to file
    def writePortEv(self,evPort):
        try:
            with open('evPort.csv', 'w') as f1:
                print(evPort,file=f1)
        except OSError as error:
            print(error)

    #Writing port to file
    def clearPortEv(self):
        try:
            with open('evPort.csv', 'w') as f1:
                f1.close()
        except OSError as error:
            print(error)

    #========== Getting a random RSU Port

    def getRsuPort(self):
        #------------------ Reading function names
        with open('rsuPort.csv',newline='') as csvfile:
        #-- Reading csv file
            csvFile=csv.reader(csvfile)
            for line in csvFile:
                #print(line)
                self.rsuPorts.append(line[0])

        #print("All ports:",self.rsuPorts)
        p=random.choices(self.rsuPorts)
        #print("Slected port:",p[0])
        return int(p[0])