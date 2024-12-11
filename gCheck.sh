#! /bin/bash

#Starting with specific Ip
#host=$(hostname -I)
#------ for both wifi and LAN
host=`(hostname -I)|awk -F' ' '{print $1}'`  
echo $host
ganache -h $host --miner.blockTime=5 --wallet.totalAccounts=5 >ganacheCli.txt
