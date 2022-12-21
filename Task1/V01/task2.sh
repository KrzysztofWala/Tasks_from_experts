#! /bin/bash

# Extracting all PID numbers
data1=$(ps ux)
pattern="^[a-z]+[[:blank:]]+[0-9]+"
echo "PID numbers:"
echo "$data1" | egrep -o $pattern | egrep -o "[0-9]+"

echo " "

# Extracting all ip addresses in alphabetical order
echo "IP addresses: "
data2=$(ifconfig)
pattern2="inet[[:blank:]][0-9]+.[0-9]+.[0-9]+.[0-9]+"
pattern3="[0-9]+.[0-9]+.[0-9]+.[0-9]+"
echo "$data2" | egrep -o $pattern2 | egrep -o $pattern3 | sort
