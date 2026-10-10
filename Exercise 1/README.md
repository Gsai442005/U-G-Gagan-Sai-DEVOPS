# Exercise 1: Hello Pod

## Goal

Deploy an Nginx pod on a local Kubernetes cluster and expose it through a NodePort service.

## Files

- `hello-pod.yaml`: Kubernetes Pod and Service manifest equivalent to the faculty commands.

## Important Commands

```bash
minikube start
kubectl apply -f hello-pod.yaml
kubectl get pods
kubectl get services
minikube service hello-k8s
```

`minikube start` creates the local Kubernetes cluster. `kubectl apply` creates the pod and service. `minikube service` opens or prints the local service URL.

## Verification

Expected result: `kubectl get pods` shows `hello-k8s` as `Running`, and the service URL displays the Nginx welcome page.

Actual result in this environment: `kubectl` client v1.37.1 is available, but a usable Kubernetes cluster and credentials are not available, so the pod and service deployment is `NOT VERIFIED`. The current client-version check is captured in [screenshots/kubectl-client-version.png](./screenshots/kubectl-client-version.png); it verifies the client only, not a running pod.
