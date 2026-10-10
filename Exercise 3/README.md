# Exercise 3: Scaling Flask App with ReplicaSets

## Goal

Run a flash-sale Flask API with three replicas, scale it to five replicas, and observe Kubernetes replacing failed pods.

## Files

- `app.py`: Flash-sale API with `/`, `/buy`, and `/health`.
- `requirements.txt`: Python dependency list.
- `Dockerfile`: Image definition for `flashsale:1.0`.
- `flashsale-replicaset.yaml`: ReplicaSet and ClusterIP Service.

## Important Commands

```bash
minikube stop
minikube delete
minikube start --nodes=1
minikube docker-env | Invoke-Expression
docker build -t flashsale:1.0 .
kubectl apply -f flashsale-replicaset.yaml
kubectl get pods
kubectl get rs
kubectl scale rs flashsale-rs --replicas=5
kubectl get pods -o wide
kubectl delete pod <pod-name>
kubectl get pods
```

`kubectl scale` changes the desired replica count. Deleting a pod demonstrates that the ReplicaSet controller creates a replacement.

## Verification

Expected result: `flashsale-rs` initially has 3 pods, scales to 5 pods, and returns to 5 pods after one pod is deleted.

Actual result in this environment: repeatable local tests for `/`, `/health`, and `/buy` pass with HTTP 200. Run `python -m unittest discover -s "Exercise 3" -v` from the repository root. The real terminal run is captured in [screenshots/flashsale-local-tests.png](./screenshots/flashsale-local-tests.png). Kubernetes replicas, scaling, and pod replacement remain `NOT VERIFIED` because no cluster or Docker runtime is available.
