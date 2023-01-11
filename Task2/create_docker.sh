#! /bin/bash
echo "Write user name"
read user_name
docker volume create volume1
docker network create new_network
docker build -t python_image .\
             --build-arg ARG_VAR=$user_name
docker run --name=python_container\
           --mount source=volume1,target=/src/share_volume\
           --mount type=bind,source=/home/whale/bind_directory,target=/src/share_bind\
           --network=new_network\
           python_image