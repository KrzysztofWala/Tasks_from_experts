#! /bin/bash
#1 CPUs
cpu=(`lscpu | grep "^CPU(s)" | egrep -o "[0-9]+"`)
echo "Number of CPU cores: $cpu"

echo " "

#2 Disk space
disk=(`df --total -h | grep "^total" | egrep -o "[0-9]+[A-Z | %]"`)
echo "Disk size: ${disk[0]}"
echo "Used space: ${disk[1]}"
echo "Available space: ${disk[2]}"
echo "Used space: ${disk[3]}"

echo " "

#3 Size of RAM
ram=(`free --mega | egrep -o "^Mem:[[:blank:]]+[0-9]+" | egrep -o "[0-9]+"`)
echo "Size of RAM: $ram MB"

echo " "

#4 Last logged user
user=(`last -1 |egrep -o "[a-z]+"`)
echo "Last user which were login: $user"

echo " "

#5 Number of active process
num=(`ps aux | wc -l`)
echo "Number of active process: $num"


