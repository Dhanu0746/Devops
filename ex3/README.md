# 🚀 Flash Sale Flask App — Kubernetes ReplicaSet

A hands-on Kubernetes lab demonstrating how a Flask application can be **scaled horizontally using Kubernetes ReplicaSets** and exposed through a Kubernetes Service.

The project simulates an **e-commerce flash sale**, where traffic can suddenly increase from normal levels to thousands of requests. Multiple replicas of the Flask application are deployed to improve scalability and resilience.

---

## 📌 Project Overview

During an e-commerce flash sale, application traffic can increase dramatically.

Instead of running the application in a single Pod:

```text
             Users
                |
                v
             1 Pod
                |
          High traffic
                ↓
             Crash ❌
```

Kubernetes ReplicaSets allow multiple identical Pods to run simultaneously:

```text
                 Users
                   |
                   v
             Flash Sale Service
                   |
        +----------+----------+
        |          |          |
        v          v          v
      Pod 1      Pod 2      Pod 3
        |          |          |
        +----------+----------+
                   |
              ReplicaSet
```

The number of replicas can be increased during high traffic and reduced when demand decreases.

---

## 🎯 Objectives

* Understand Kubernetes Pods and ReplicaSets
* Deploy a Flask application inside Kubernetes
* Scale the application from 3 to 5 replicas
* Expose the application using a Kubernetes Service
* Observe traffic distribution across Pods
* Demonstrate ReplicaSet self-healing
* Understand basic Kubernetes health probes
* Observe Pod IP and node information

---

## 🛠️ Technologies Used

* Python 3.11
* Flask
* Gunicorn
* Docker
* Kubernetes
* Minikube
* kubectl
* Docker Desktop
* PowerShell

---

## 📁 Project Structure

```text
ex3/
│
├── app.py
├── Dockerfile
├── flashsale-replicaset.yaml
└── README.md
```

---

# 🐍 Flask Application

The application provides three endpoints.

### `/`

Returns a welcome message and the hostname of the Pod serving the request.

Example:

```json
{
  "message": "Welcome to Big Sale!",
  "pod": "flashsale-rs-xxxxx",
  "ts": 1234567890
}
```

### `/buy`

Simulates a flash-sale purchase.

Example:

```text
/buy?user=123
```

Response:

```json
{
  "status": "success",
  "item": "Laptop",
  "user": "123",
  "served_by_pod": "flashsale-rs-xxxxx",
  "time": "20:10:15"
}
```

The `served_by_pod` field makes it possible to observe which Pod handled the request.

### `/health`

Used for Kubernetes health checks.

```json
{
  "status": "healthy",
  "pod": "flashsale-rs-xxxxx"
}
```

---

# 🐳 Docker Configuration

The Flask application is packaged using Docker.

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY app.py .

RUN pip install --no-cache-dir flask gunicorn

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app", "--workers", "1", "--threads", "2"]
```

---

# ☸️ Kubernetes Configuration

The Kubernetes configuration contains:

* ReplicaSet
* Flask application Pods
* Readiness probe
* Liveness probe
* Kubernetes Service

Initial configuration:

```yaml
replicas: 3
```

The ReplicaSet maintains three identical Pods.

The Service selects Pods using:

```yaml
selector:
  app: flashsale
```

The Service exposes port `80` and forwards traffic to the Flask application running on port `5000`.

---

# 🚀 Running the Project

## 1. Start Minikube

```bash
minikube start --nodes=1
```

Verify the node:

```bash
kubectl get nodes
```

Expected:

```text
NAME       STATUS   ROLES
minikube   Ready    control-plane
```

---

## 2. Build the Docker Image

Build the image directly into Minikube:

```bash
minikube image build -t flashsale:1.0 .
```

Verify:

```bash
minikube image ls
```

---

## 3. Deploy the ReplicaSet and Service

```bash
kubectl apply -f flashsale-replicaset.yaml
```

Verify:

```bash
kubectl get rs
```

and:

```bash
kubectl get pods
```

Initially, three Pods should be running.

---

# 📈 Scaling the Application

The ReplicaSet can be manually scaled from 3 to 5 replicas.

```bash
kubectl scale rs flashsale-rs --replicas=5
```

Verify:

```bash
kubectl get rs
```

Expected:

```text
NAME           DESIRED   CURRENT   READY
flashsale-rs   5         5         5
```

Then:

```bash
kubectl get pods
```

Five Flask application Pods should be running.

---

# 🔄 ReplicaSet Self-Healing

ReplicaSets maintain the desired number of replicas.

For example, with five replicas:

```text
Desired = 5
Current = 5
```

If one Pod is manually deleted:

```bash
kubectl delete pod <pod-name>
```

the number temporarily becomes:

```text
Desired = 5
Current = 4
```

The ReplicaSet detects this difference and automatically creates a replacement Pod.

After the replacement starts:

```text
Desired = 5
Current = 5
```

This demonstrates Kubernetes self-healing.

---

# 🌐 Accessing the Application

Since the Service is a `ClusterIP`, Minikube can expose it locally using:

```bash
minikube service flashsale-svc --url
```

The command provides a local URL.

Example:

```text
http://127.0.0.1:<port>
```

The terminal running this command must remain open when using the Minikube Docker driver on Windows.

---

# 🔍 Testing the Application

### Homepage

```text
http://127.0.0.1:<port>/
```

### Buy request

```text
http://127.0.0.1:<port>/buy?user=123
```

### Health check

```text
http://127.0.0.1:<port>/health
```

Repeated requests can return different Pod hostnames, demonstrating that requests can be handled by different replicas.

---

# 📊 Observing Pod Distribution

Run:

```bash
kubectl get pods -o wide
```

Example:

```text
NAME                 READY   STATUS    IP            NODE
flashsale-rs-xxxxx   1/1     Running   10.244.0.10   minikube
flashsale-rs-yyyyy   1/1     Running   10.244.0.7    minikube
flashsale-rs-zzzzz   1/1     Running   10.244.0.11   minikube
flashsale-rs-aaaaa   1/1     Running   10.244.0.9    minikube
flashsale-rs-bbbbb   1/1     Running   10.244.0.6    minikube
```

Since this lab uses a **single-node Minikube cluster**, all Pods run on the `minikube` node.

Each Pod still receives its own Kubernetes Pod IP.

---

# ❤️ Health Probes

The application uses two Kubernetes probes.

### Readiness Probe

```yaml
readinessProbe:
  httpGet:
    path: /health
    port: 5000
```

The readiness probe determines whether a Pod is ready to receive traffic.

### Liveness Probe

```yaml
livenessProbe:
  httpGet:
    path: /health
    port: 5000
```

The liveness probe allows Kubernetes to determine whether the application is still running correctly.

---

# 📸 Screenshots

Screenshots demonstrating the completed lab are included below.

## 1. Three Flask Pods Running

![Three Pods Running](screenshots/01-three-pods-running.png)

## 2. ReplicaSet Scaled to Five

![Scaled ReplicaSet](screenshots/02-scaled-to-five.png)

## 3. ReplicaSet Self-Healing

![ReplicaSet Self Healing](screenshots/03-replica-self-healing.png)

## 4. Pod Distribution

![Pod Distribution](screenshots/04-pod-distribution.png)

## 5. Flask Flash Sale Request

![Flash Sale Request](screenshots/05-flask-buy-request.png)

> Update the screenshot filenames above if your actual filenames are different.

---

# 🧠 Key Learnings

### Pod Replication

Each Pod is an identical instance of the Flask application.

### Scalability

The application can be scaled horizontally by increasing the number of replicas:

```text
3 Pods → 5 Pods
```

### Resilience

If a Pod fails or is deleted, the ReplicaSet automatically creates a replacement.

### Service Discovery

The Kubernetes Service provides a stable endpoint for accessing the application while the individual Pod IPs can change.

### Health Monitoring

Readiness and liveness probes allow Kubernetes to monitor application health.

### Real-World Application

The same basic scaling concept is used in large-scale distributed systems to handle changing traffic demands.

---

# 📌 Useful Kubernetes Commands

```bash
# Check nodes
kubectl get nodes

# Check Pods
kubectl get pods

# Check Pods with IP and node
kubectl get pods -o wide

# Check ReplicaSets
kubectl get rs

# Check Services
kubectl get svc

# Check all resources
kubectl get all

# Scale ReplicaSet
kubectl scale rs flashsale-rs --replicas=5

# Delete a Pod
kubectl delete pod <pod-name>

# Describe ReplicaSet
kubectl describe rs flashsale-rs

# Get Service URL
minikube service flashsale-svc --url
```

---

# 🏁 Conclusion

This lab demonstrates how Kubernetes ReplicaSets can be used to run multiple instances of a Flask application, scale the application horizontally, distribute requests through a Service, and automatically recover from Pod failures.

The exercise provides a practical introduction to **container orchestration, scalability, service discovery, health monitoring, and self-healing in Kubernetes**.
