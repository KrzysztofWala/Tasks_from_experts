#! /bin/bash
# The current time in format hh:mm:ss
echo Actual time:
echo $(date) | grep -o "\b[0-9][0-9]:[0-9][0-9]:[0-9][0-9]\b"

echo " "

# ivp4 address
echo ivp4 address:
echo $(ip -4 addr) | grep -o "inet [0-9]*\.[0-9]*\.[0-9]*\.[0-9]*" | grep -o "[0-9]*\.[0-9]*\.[0-9]*\.[0-9]*"

echo " "

# Searching for whole text paragraph which includes given  word
echo "Write word:"
read word
grep "$word" file.txt
