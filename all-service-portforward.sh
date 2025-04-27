#!/bin/bash

# Stop all port-forwards when script is killed
trap "echo 'Stopping port-forwarding...'; kill 0" SIGINT SIGTERM EXIT

# Port-forward java-service
nohup kubectl port-forward svc/java-service 8080:80 > java.log 2>&1 &
echo "Port-forwarding java-service on localhost:8080"

# Port-forward python-service
nohup kubectl port-forward svc/python-service 5001:80 > python.log 2>&1 &
echo "Port-forwarding python-service on localhost:5001"

# Port-forward go-service
nohup kubectl port-forward svc/go-service 5002:80 > go.log 2>&1 &
echo "Port-forwarding go-service on localhost:5002"

# Wait for background jobs
wait
