#! /bin/bash

#Arguments $1

#This script will extracts private keys from the ganache starting page.
# frm=6
# # sed -n "$frm p" info.txt
# while [ $frm -lt 17  ]
# do
# sed -n "$frm p" info.txt 
# frm=`expr $frm + 1`
# done >privateKeys.txt

# #--------- For 10 Users
# # Starts from line 19 to 30
# frm=19      
# # sed -n "$frm p" info.txt
# while [ $frm -lt 30  ]
# do
# sed -n "$frm p" info.txt 
# frm=`expr $frm + 1`
# done >privateKeys.txt

nUser=$1
sleep 5
#echo $nUser
#--------- For 20 Users
# Starts from line 19+10 to 30+20
frm=$(($nUser+9))
to=$(($nUser+$frm))      
echo $frm
echo $to
# sed -n "$frm p" info.txt
while [ $frm -lt $to  ]
do
sed -n "$frm p" ganacheCli.txt 
frm=`expr $frm + 1`
done >privateKeys.txt

#nUser=$1
#echo $nUser
#========================= Getting private keys
gnome-terminal --tab -- bash -c "python getPkey.py -n $nUser" #; exec bash -i"


# frm=109
# while [ $frm -lt 209  ]
# do
# sed -n "$frm p" info.txt 
# frm=`expr $frm + 1`
# done >privateKeys.txt