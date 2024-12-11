#!/bin/sh
#starts the services
#echo "reading ganache...."
#./readAdd.sh
#python getPkey.py

#=========== Cleaning
# fuser -k 5051/tcp 
# p=`ps -A| grep 'runSp.sh'| awk '{print $1}'`
# kill $p   #=== Killing PID
# fuser -K $p/tcp
# p=`ps -A| grep 'ganacheCli.sh'| awk '{print $1}'`
# kill $p #=== Killing PID

echo "Enter no of network elements:"
read u

echo "First address will be Trusted Authority"
echo "Enter number of RSU:"
read rsu


    #===================== Ganache
    gnome-terminal --tab -- bash -c "./ganacheCli.sh $u"
    #==========================
    sleep 10 #============= So that ganacheCli can prepare

    echo "Creating truffle settings..."
    python getTruffleConfig.py
    echo ".....Starting Truffle"
    truffle compile
    python migrate.py
    python getAbiByteCode.py
    #----------------------------- reset and again migrate after any change
    truffle migrate --reset

    #--------------------------------------------
    start=`date +%s%N` #To calculate start and end time
    truffle deploye>smartcontract.txt
    #sAdd=$(cat smartcontract.txt| grep 'address:' | awk -F':' '{print $2}')
    end=`date +%s%N`
    echo Execution time was `expr $end - $start` nanoseconds.
    #gnome-terminal --tab -- bash -c "python server.py"
    #=============== Writing deployment time in a text file 
    echo "\nExecution time was" `expr $end - $start` nanoseconds.>>1_DeploymentTime.txt
    sAdd=`cat smartcontract.txt| grep 'address:' | awk -F':' '{print $2}'`
    echo $sAdd

    gas=`cat smartcontract.txt| grep 'used:' | awk -F':' '{print $2}'`
    echo $gas
    #====================== 
    # start=`date +%s%N` #To calculate start and end time
    # truffle deploye
    # end=`date +%s%N`
    # echo Execution time was `expr $end - $start` nanoseconds.
    # #gnome-terminal --tab -- bash -c "python server.py"
    # #=============== Writing deployment time in a text file 
    # echo "\nExecution time was" `expr $end - $start` nanoseconds.>>1_DeploymentTime.txt
    #prepares the runCar file
    echo "\nPreparing .TA...RSU..and Vehicles.."
    #=====================================================ready will ask for contract address
    python readyPi.py -c $sAdd -r $rsu
    echo "Smart parking and Vehicles Created."

    #===================== Ganache
    echo "Starting server..."
    gnome-terminal --tab -- bash -c "./runSp.sh"
    sleep 5
    echo "Starting vehicles.....Manually........Run....Vehicles"
    #
    ./runRsu.sh
    ./runCar.sh
    
    # #============ Sleep to keep system task complete
    # sleep 100
    # #============== Killing and free port
    # #------- Get the PID
    # p=`ps -A| grep 'runSp.sh'| awk '{print $1}'`
    # kill $p  #=== Killing PID
    # fuser -K $p/tcp
    # p=`ps -A| grep 'ganacheCli.sh'| awk '{print $1}'`
    # kill $p  #=== Killing PID