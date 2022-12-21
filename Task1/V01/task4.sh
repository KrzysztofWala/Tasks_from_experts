#! /bin/bash

############################################################
# Help                                                     #
############################################################
Help()
{
   # Display Help
   echo "Add description of the script functions here."
   echo
   echo "Syntax: scriptTemplate [-a|c|d|r|u|p|h]"
   echo "options:"
   echo "a     All option"  
   echo "c     Number of CPU cores"
   echo "d     Disk space"
   echo "r     Size of RAM"
   echo "u     Last logged user"
   echo "p     Number of active process"
   echo "h     Help"   
   echo
}

############################################################
# Functions                                                #
############################################################

Cpu_check()
{
	cpu=(`lscpu | grep "^CPU(s)" | egrep -o "[0-9]+"`)
	echo "Number of CPU cores: $cpu"
}

Disk_check()
{
	disk=(`df --total -h | grep "^total" | egrep -o "[0-9]+[A-Z | %]"`)
	echo "Disk size: ${disk[0]}"
	echo "Used space: ${disk[1]}"
	echo "Available space: ${disk[2]}"
	echo "Used space: ${disk[3]}"
}

Ram_check()
{
	ram=(`free --mega | egrep -o "^Mem:[[:blank:]]+[0-9]+" | egrep -o "[0-9]+"`)
	echo "Size of RAM: $ram MB"
	
}

User_check()
{
	user=(`last -1 |egrep -o "[a-z]+"`)
	echo "Last logged user: $user"
}

Process_check()
{
	num=(`ps aux | wc -l`)
	echo "Number of active process: $num"
}

############################################################
# Main                                                     #
############################################################

while getopts 'acdruph' options 
  do
   case $options in
      a)
      	 Cpu_check
      	 Disk_check
      	 Ram_check
      	 User_check
      	 Process_check
      	 exit
      	 ;;
      c) 
         Cpu_check
         exit
         ;;
         
      d) 
      	 Disk_check
      	 exit
         ;;
      r) 
      	 Ram_check
      	 exit
         ;;
      u) 
      	 User_check
      	 exit
         ;;
      p) 
      	 Process_check
      	 exit
         ;;
      h) 
      	 Help
      	 exit
         ;;                        
      \?)
      	 echo "Wrong input"
      	 exit
      	 ;;

   esac
done

Cpu_check
Disk_check
Ram_check
User_check
Process_check

exit 0;
