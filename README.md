# DevOps Exercises

This repository contains the first three DevOps lab exercises, each in its own numbered folder. The Kubernetes manifests and commands follow the corresponding topics in [SunagP/DevOps-Lab](https://github.com/SunagP/DevOps-Lab/tree/main/Exercises).

## Exercises

| Folder | Topic | Evidence |
| --- | --- | --- |
| [Exercise 1](./Exercise%201/) | Kubernetes Nginx pod and NodePort service | [terminal output](./Exercise%201/terminal-output.txt); [screenshots](./Exercise%201/screenshots/); Kubernetes deployment not verified |
| [Exercise 2](./Exercise%202/) | Flask application for Minikube | [terminal output](./Exercise%202/terminal-output.txt); [screenshots](./Exercise%202/screenshots/); Kubernetes deployment not verified |
| [Exercise 3](./Exercise%203/) | Flask flash-sale API and Kubernetes ReplicaSet | [terminal output](./Exercise%203/terminal-output.txt); [screenshots](./Exercise%203/screenshots/); ReplicaSet scaling not verified |

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

Each exercise folder contains screenshots and a `terminal-output.txt` record of commands actually run on the capture machine, with the capture time and observed command results. The Flask outputs show local app/tests, not a Docker or Minikube deployment. This Windows host currently has no working Kubernetes context or Docker runtime; the installed Minikube binary cannot run on this OS, firmware virtualization is disabled, and administrator privileges are unavailable. Therefore, successful pod, Deployment, NodePort, or ReplicaSet output cannot truthfully be produced here yet. Follow each exercise README to run those steps after configuring a supported local cluster.
