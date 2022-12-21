#! /bin/bash
# The current time in format hh:mm:ss   
echo Actual time:
echo $(date) | egrep -o "([0-1][0-9]|[2][0-3]):[0-5][0-9]:[0-5][0-9]"

echo " "

# ivp4 address
echo ivp4 address:
echo $(ip -4 addr) | egrep -o "inet ([0-9]{1,2}|1[0-9][0-9]|2[0-4][0-9]|25[0-9])\.([0-9]{1,2}|1[0-9][0-9]|2[0-4][0-9]|25[0-9])\.([0-9]{1,2}|1[0-9][0-9]|2[0-4][0-9]|25[0-9])\.([0-9]{1,2}|1[0-9][0-9]|2[0-4][0-9]|25[0-9])" | egrep -o "[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}"

echo " "

# Searching for whole text paragraph which includes given  word
echo "Write word:"
read word
#grep "$word" file.txt
egrep $word file.txt 
