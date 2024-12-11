#! /bin/bash

# if [ $# -eq 0 ]; then
# #Normal Start
# ganache>info.txt
# else
# #Special Start
# ganache --miner.blockTime=15>info.txt
# fi
echo "Ganache started..."
# #Special Start [ number of account ]
# #---------- 10 Accounts
# ganache --miner.blockTime=15 --wallet.totalAccounts=10 >info.txt

# echo "Enter number of users:"
# read nUser  #---------------- Number of users
nUser=$1
gnome-terminal --tab -- bash -c "./readAdd.sh $nUser" #; exec bash -i"
clear #To clear the screen
echo "Ganache is running with $nUser"

#Normal Start
#ganache --miner.blockTime=5 --wallet.totalAccounts=$nUser >ganacheCli.txt
#Starting with specific Ip
#host=$(hostname -I) #works only for lan
host=`(hostname -I)|awk -F' ' '{print $1}'`
echo $host

ganache -h $host --miner.blockTime=5 --wallet.totalAccounts=$nUser >ganacheCli.txt

#gnome-terminal --tab -- bash -c "python getPkey.py -n $nUser; exec bash -i"
#gnome-terminal --tab -- bash -c "./readAdd.sh $nUser; exec bash -i"
#---------- 20 Accounts
#gnome-terminal --tab -- bash -c "ganache --miner.blockTime=15 --wallet.totalAccounts=$nUser >info.txt; exec bash -i"
#./readAdd.sh $nUser
#ganache --miner.blockTime=15 --wallet.totalAccounts=$nUser >info.txt

# #---------- 30 Accounts
# ganache --miner.blockTime=15 --wallet.totalAccounts=30 >info.txt

# #----------- 40 Accounts
# ganache --miner.blockTime=15 --wallet.totalAccounts=40 >info.txt

# #------------- 50 Accounts
# ganache --miner.blockTime=15 --wallet.totalAccounts=50 >info.txt

# #Special Start [ number of account ]
#ganache --miner.blockTime=15>info.txt