#! /bin/bash
pattern="^[0-9]+.[0-9]+.[0-9]+.[0-9]+"
file=access.log
Array=(`egrep -o $pattern $file | sort -n | uniq -c `)
len=${#Array[@]} 
for i in $(seq 1 2 $len)
do 
	if ((${Array[$i-1]} <2))
	then
		echo "From IP adress" ${Array[$i]} "there was sent" ${Array[$i-1]}  "request."
	else 
		echo "From IP adress" ${Array[$i]} "there were sent" ${Array[$i-1]}  "requests."
	fi
done
