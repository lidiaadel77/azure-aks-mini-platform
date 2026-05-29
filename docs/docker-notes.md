# Docker Notes

This file documents the Docker setup for the Azure AKS Mini Platform project.

## Purpose

Docker is used to package the Flask application with its dependencies into a container image.

This image can run locally, in GitHub Actions, and later inside Azure Kubernetes Service.

## Local Build

The image was built locally using:

`docker build -t azure-aks-mini-platform:local .`

## Local Run

The container was run locally using:

`docker run --rm -p 5000:5000 -e APP_VERSION=1.0.0 -e APP_ENV=docker azure-aks-mini-platform:local`

## Tested Endpoints

The following endpoints were tested:

- `/`
- `/health`
- `/version`

The `/version` endpoint confirmed that the app was running inside Docker.
