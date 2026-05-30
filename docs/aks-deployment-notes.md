
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
