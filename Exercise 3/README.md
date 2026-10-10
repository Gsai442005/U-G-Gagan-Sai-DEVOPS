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

Actual result in this environment: the Flask app was started locally; live requests to `/`, `/health`, and `/buy?user=student` returned the expected API responses. The actual command output is in [terminal-output.txt](./terminal-output.txt), with the live requests and passing local tests also captured in [screenshots/flashsale-live-http.png](./screenshots/flashsale-live-http.png) and [screenshots/flashsale-local-tests.png](./screenshots/flashsale-local-tests.png). Repeatable local tests for all three routes pass with `python -m unittest discover -s "Exercise 3" -v` from the repository root. These checks use one local Flask process, not Kubernetes. Docker and a working cluster are unavailable, so image build, initial three replicas, scaling to five, service traffic, and pod replacement remain `NOT VERIFIED`.
