# DevOps Exercises

This repository contains the first three DevOps lab exercises, each in its own numbered folder.

## Exercises

| Folder | Topic | Evidence |
| --- | --- | --- |
| [Exercise 1](./Exercise%201/) | Kubernetes Nginx pod and NodePort service | `kubectl` client check; cluster deployment unavailable on the capture machine |
| [Exercise 2](./Exercise%202/) | Flask application for Minikube | Local Flask endpoint returned HTTP 200; Kubernetes deployment not verified |
| [Exercise 3](./Exercise%203/) | Flask flash-sale API and Kubernetes ReplicaSet | Local API endpoints returned HTTP 200; replicas and scaling not verified |

## Running the local Flask checks

The checks shown in the screenshots exercise the Flask applications locally. They do not claim to be Kubernetes deployments.

From the repository root, install each exercise's Python dependencies and run its app:

```powershell
python -m pip install -r "Exercise 2/requirements.txt"
python "Exercise 2/app.py"
```

```powershell
python -m pip install -r "Exercise 3/requirements.txt"
python "Exercise 3/app.py"
```

To deploy the manifests, first start and configure a working Minikube cluster and Docker runtime, then follow the command sequence in the corresponding exercise README.

## Screenshot evidence

Each exercise folder contains genuine PowerShell terminal captures of commands actually run on the capture machine. The timestamp in each capture uses the machine's current time and timezone. A local endpoint check or Kubernetes client-version check is not presented as proof of a cluster deployment.
