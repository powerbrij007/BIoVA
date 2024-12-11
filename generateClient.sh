#!/bin/bash
echo "Deleting older fiels.."
rm -r clientSystem/abis
echo "status..."$?
echo "copying abi...."
cp -r abis clientSystem
echo "status..."$?
echo "Getting system IP..."
#host=$(hostname -I)
host=`(hostname -I)|awk -F' ' '{print $1}'`
echo $host
echo "System IP:"$host
echo $host>clientSystem/host.txt
echo "reading....runCar.sh"
file="runCar.sh"

# while read -r line; do
# echo -e "$line\n"
# done <$file
rm clientSystem/runCar.sh
echo "runCar.sh deleted..."$?
touch clientSystem/runCar.sh
echo "#!/bin/bash">clientSystem/runCar.sh
echo "python genconfig.py">>clientSystem/runCar.sh
#tail -n 1 runCar.sh|`awk -F';' '{print $0}'`>>clientSystem/runCar.sh
data=`tail -n 1 runCarPi.sh|awk -F';' '{print $0}'`
echo $data>>clientSystem/runCar.sh
echo "Writing status..."$?
#echo "Adding IP...."
#val=" "$host" ;"
# replace=$(sed -i "s/;/${val}/g" clientSystem/runCar.sh)
# echo $replace
# echo "Status...."$?