#!/bin/bash

# Build the Docker image
docker build -t python-service .

# Run the Docker container
docker run -p 5000:5000 python-service
