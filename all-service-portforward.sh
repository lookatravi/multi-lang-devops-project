#!/bin/bash

# Port-forward java-service
kubectl port-forward svc/java-service 8080:80 &
echo "Port-forwarding java-service on localhost:8080"

# Port-forward python-service
kubectl port-forward svc/python-service 5001:80 &
echo "Port-forwarding python-service on localhost:5001"

# Port-forward go-service
kubectl port-forward svc/go-service 5002:80 &
echo "Port-forwarding go-service on localhost:5002"

# Wait so script doesn't exit immediately
wait
