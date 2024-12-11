#this program reads all private keys from
#add1.txt and convert into required format

#--------------- For automatically giving the number of accounts
import optparse
import time
#create a parser object
parser = optparse.OptionParser()

#adding argument
parser.add_option("-n",dest="a",type="int", help="Number of accounts.") #======= number of account

(options, args)=parser.parse_args()

#-------- Private Keys
privateKeys=[]

#Showing a meaningful address
if not options.a:
   #print("No argument is provided")
   parser.error("No argument is provided")
else:
    a1=options.a
    print(int(a1))
    time.sleep(4) #--------- creating a delay from ganache initialization
    with open('privateKeys.txt') as f:
        contents=f.readlines()
        print(len(contents))
        for i in range(int(a1)):
            pk=contents[i].split(" ")
            pk2=pk[1].strip() #removes \n
            privateKeys.append(pk2)

    
# j=0;    
# for i in privateKeys:
#     j+=1
# print(j)
print(privateKeys)





# contents=[]
# with open('add1.txt') as f:
#     contents.append(f.readlines())
#     # print(contents)

# print(contents)