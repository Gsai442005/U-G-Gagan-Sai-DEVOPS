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

Actual result in this environment: `kubectl` client v1.37.1 is available, but the current Kubernetes context is not set, so the pod and service deployment is `NOT VERIFIED`. See [terminal-output.txt](./terminal-output.txt) for the actual command output, [screenshots/kubectl-client-version.png](./screenshots/kubectl-client-version.png) for the client version, and [screenshots/cluster-unavailable.png](./screenshots/cluster-unavailable.png) for the current-context check. Neither screenshot shows a running pod.

The manual's full success output requires a working Minikube cluster. Minikube cannot run on this host: its installed executable is not valid for Windows, Docker is unavailable, firmware virtualization is disabled, and this session has no administrator privileges to enable or install the required runtime. Do not treat the client-version check as a deployment result.
