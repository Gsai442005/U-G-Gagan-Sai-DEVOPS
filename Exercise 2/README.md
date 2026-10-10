# Exercise 2: Deploy Flask App on Minikube

## Goal

Build a Flask application image, deploy it to Minikube with `kubectl`, and expose it using a NodePort service.

## Files

- `app.py`: Flask app listening on port `15000`.
- `requirements.txt`: Python dependency list.
- `Dockerfile`: Container image definition.
- `flask-deployment.yaml`: Kubernetes Deployment and Service.

## Important Commands

```bash
minikube start
minikube docker-env
# Linux/macOS/WSL:
eval $(minikube docker-env)
# PowerShell:
minikube docker-env | Invoke-Expression
docker build -t flask-app:latest .
kubectl apply -f flask-deployment.yaml
kubectl get deployments
kubectl get pods -l app=flask-app
kubectl get services
minikube service flask-app-service --url
```

`minikube docker-env` points Docker at Minikube's internal Docker daemon so `imagePullPolicy: Never` can use the locally built image. `kubectl apply` creates or updates the app resources.

## Verification

Expected result: the URL from `minikube service flask-app-service --url` returns `Hello from Flask on Kubernetes!`.

Actual result in this environment: the local Flask endpoint test passes with HTTP 200. Run the repeatable test with `python -m unittest discover -s "Exercise 2" -v` from the repository root. The real terminal run is captured in [screenshots/flask-local-test.png](./screenshots/flask-local-test.png). Docker and a working Minikube cluster are unavailable, so the container build and Kubernetes deployment remain `NOT VERIFIED`.
