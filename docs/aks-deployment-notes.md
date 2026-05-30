
## AKS Deployment

The Flask Docker image was pushed to Azure Container Registry and deployed to Azure Kubernetes Service.

Created Kubernetes resources:

- Deployment: `aks-flask-api`
- Service: `aks-flask-api-service`
- Service type: `LoadBalancer`

Docker image:

`acraksgh97b.azurecr.io/aks-flask-api:1.0.0`

AKS cluster:

`aks-aks-mini-platform-gh97b`

External service IP:

`20.19.66.91`

Tested endpoints:

- `/health`
- `/version`

The pod was successfully running inside AKS.

The LoadBalancer service exposed the application publicly using an external IP.

The `/version` endpoint confirmed:

- environment: `aks`
- version: `1.0.0`

Screenshots captured:

- `aks-pod-running.png`
- `aks-service-loadbalancer.png`
- `aks-health-endpoint.png`
- `aks-version-endpoint.png`

## AKS GitHub Actions CI/CD

GitHub Actions was configured to automatically deploy the Flask application to Azure Kubernetes Service.

Workflow file:

`.github/workflows/test-build.yml`

The workflow performs these steps:

- Checks out the repository
- Sets up Python
- Installs dependencies
- Runs Pytest tests
- Logs into Azure using OIDC
- Logs into Azure Container Registry
- Builds a Docker image
- Pushes the image to Azure Container Registry
- Connects to AKS
- Applies Kubernetes manifests
- Updates the AKS deployment image
- Waits for rollout completion

Azure Container Registry:

`acraksgh97b.azurecr.io`

AKS Cluster:

`aks-aks-mini-platform-gh97b`

Kubernetes Deployment:

`aks-flask-api`

Kubernetes Service:

`aks-flask-api-service`

The deployed image tag uses the GitHub commit SHA.

The `/version` endpoint confirms the app was deployed by GitHub Actions.

Expected environment value:

`github-actions`

This completes the AKS CI/CD pipeline.
