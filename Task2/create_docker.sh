#! /bin/bash
docker build -t python_image .
docker run --name=python_container python_image