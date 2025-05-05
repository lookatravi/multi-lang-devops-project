# Multi-Language DevOps Project

## Overview
This project demonstrates a multi-language application setup with a complete DevOps pipeline. It includes CI/CD workflows, containerization, and automated cleanup processes. The project is designed to showcase best practices for managing multi-language applications in a DevOps environment.

## Features
- **Multi-Language Support**: Combines applications written in different programming languages.
- **CI/CD Workflows**: Automated pipelines for building, testing, and deploying the application.
- **Containerization**: Uses Docker to containerize the application for consistent deployment.
- **Image Cleanup**: Automated cleanup of old Docker images to optimize storage.

## Repository Structure
.github/ workflows/ ci.yaml # CI/CD pipeline configuration cleanup-old-images.yaml # Workflow for cleaning up old Docker images src/ <language-specific folders> # Application source code for each language Dockerfile # Docker configuration for the application terraform/ # Infrastructure as Code (IaC) for deployment
## Workflows
### CI Workflow (`ci.yaml`)
- Triggers on every push or pull request.
- Builds and tests the application.
- Pushes Docker images to a container registry.

### Cleanup Workflow (`cleanup-old-images.yaml`)
- Scheduled to run periodically.
- Removes unused or old Docker images from the container registry.

## Prerequisites
- Docker
- Kubernetes (optional for deployment)
- Terraform (for infrastructure setup)
- GitHub Actions (for CI/CD workflows)

## How to Use
1. Clone the repository:

git clone https://github.com/lookatravi/multi-lang-devops-project.git
  cd multi-lang-devops-project  

## Build and run the application locally:

# Java
cd java-service && ./mvnw package

# Python
cd python-service && pip install -r requirements.txt

# Go
cd go-service && go build

# Docker build and run locally

docker build -t multi-lang-app .
docker run -p 8080:8080 multi-lang-app

Configure GitHub Actions secrets for CI/CD:

DOCKER_USERNAME: Docker Hub username.
DOCKER_PASSWORD: Docker Hub password.
REGISTRY_URL: URL of the container registry.
Deploy the application using Terraform:

# Deploy to Kubernetes

kubectl apply -f k8s-manifest-all/

#  Port Forwarding (Local Testing)

chmod +x port-forward.sh
./port-forward.sh  # Access on localhost:8080, 5001, 5002

📝 Troubleshooting
Issue: Health checks failing
Fix:

kubectl describe pod <pod-name>  # Check logs

Issue: Port forwarding not working
ps aux | grep port-forward  # Kill stale processes

# Contributing
Contributions are welcome!

Fork the repository
Create a new branch (git checkout -b feature)
Commit changes (git commit -am 'Add feature')
Push to branch (git push origin feature)
Open a Pull Request
