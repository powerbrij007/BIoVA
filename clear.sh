#1/bin/bash
#------------- For clering all the ports 
fuser -k 5051/tcp
p=`ps -A| grep 'runSp.sh'| awk '{print $1}'`
kill $p  #=== Killing PID
fuser -K $p/tcp
#p=`ps -A| grep 'ganacheCli.sh'| awk '{print $1}'`
#kill $p  #=== Killing PID
clear
