import car
import threading
import time

import optparse


# a: [-p BatteryCapacity, BatteryStatus, range,TimesToDrive, groundClearance]

#create a parser object
parser = optparse.OptionParser()

#adding argument
parser.add_option("-n")
parser.add_option("-p",dest="a",type="int",nargs=5, help="Car parameters")
parser.add_option("-u", help="User address")
parser.add_option("-k", help="User private address")
parser.add_option("-c", help="Contract address")
parser.add_option("-q", help="Number of users")
#parser.add_option("-t", help="Times to run vehicle")


(options, args)=parser.parse_args()

#Showing a meaningful address
if not options.a:
   #print("No argument is provided")
   parser.error("No argument is provided")
else:
    a1=options.a
    print(a1)
    obj= car.E_car(options.n,a1[0],a1[1],a1[2],a1[3],a1[4],options.u,options.k,options.c,options.q)
    # obj.info()
    # obj.evRegister()
    # print("Driving Times:",a1[3])
    # rep=10 #a1[3] #number of times to drive
    # while(rep>0):
    #     obj.evRegister()
    #     obj.drive()
    #     rep=rep-1
    #     print("Driving Times:",rep)
 
    


