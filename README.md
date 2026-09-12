
# Flask Application Deployment on Minikube

A simple Flask application deployed on a local Kubernetes cluster using
Docker, Minikube, and Kubernetes Deployment and Service resources.

## 📌 Objective

The objective of this project is to learn the basics of Kubernetes by deploying
a Python Flask application on a single-node Minikube cluster.

The application is containerized using Docker and deployed using Kubernetes
YAML configuration.

## 🛠️ Technologies Used

- Python
- Flask
- Docker
- Kubernetes
- Minikube
- kubectl
- YAML
- Git & GitHub

## 📁 Project Structure

```text
ex2/
│
├── app.py
├── Dockerfile
├── flask-deployment.yaml
└── README.md
````

## 🚀 Application

The Flask application provides a simple endpoint:

```text
/
```

When accessed, it returns:

```text
Hello from Flask on Kubernetes!
```

The Flask application runs on port `15000`.

### `app.py`

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask on Kubernetes!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=15000)
```

## 🐳 Docker

The Flask application is containerized using the following Dockerfile:

```dockerfile
FROM python:3.8-slim

WORKDIR /app

COPY . /app

RUN pip install flask

CMD ["python", "app.py"]
```

### Build the Docker Image

```bash
docker build -t flask-app .
```

This creates the Docker image:

```text
flask-app:latest
```

## ☸️ Minikube Setup

Start the Minikube cluster using the Docker driver:

```bash
minikube start --driver=docker
```

Verify the cluster:

```bash
minikube status
```

Expected status:

```text
host: Running
kubelet: Running
apiserver: Running
kubeconfig: Configured
```

## 📦 Load Docker Image into Minikube

The locally built Docker image is loaded into Minikube:

```bash
minikube image load flask-app:latest
```

Verify that the image is available:

```bash
minikube image ls
```

## ☸️ Kubernetes Deployment

The application is deployed using `flask-deployment.yaml`.

The Deployment:

* Creates one replica of the Flask application.
* Uses the `flask-app:latest` Docker image.
* Uses `imagePullPolicy: Never` so Kubernetes uses the locally available image.
* Exposes container port `15000`.

Apply the Deployment:

```bash
kubectl apply -f flask-deployment.yaml
```

Check the Deployment:

```bash
kubectl get deployments
```

Expected result:

```text
NAME        READY   UP-TO-DATE   AVAILABLE
flask-app   1/1     1            1
```

## 🔍 Verify the Pod

Check the running Pod:

```bash
kubectl get pods
```

Expected:

```text
NAME                         READY   STATUS    RESTARTS
flask-app-xxxxxxxxxx-xxxxx   1/1     Running   0
```

The Pod should have:

```text
STATUS: Running
```

## 📝 Describe the Deployment

Detailed information about the Deployment can be viewed using:

```bash
kubectl describe deployment flask-app
```

This displays information such as:

* Number of replicas
* Pod template
* Container image
* Container port
* Deployment conditions
* Deployment events

## 📋 Application Logs

To view the Flask application's logs:

```bash
kubectl logs <pod-name>
```

The logs confirm that Flask is running and listening on port `15000`.

Example:

```text
* Serving Flask app 'app'
* Debug mode: off
* Running on all addresses (0.0.0.0)
* Running on http://127.0.0.1:15000
```

## 🌐 Kubernetes Service

A Kubernetes `NodePort` Service is used to expose the Flask application.

The Service configuration maps:

```text
Service Port: 15000
        ↓
Target Port: 15000
        ↓
Flask Container: 15000
```

Apply the Service configuration:

```bash
kubectl apply -f flask-deployment.yaml
```

Check the Service:

```bash
kubectl get services
```

## 🔗 Access the Application

Minikube can provide a URL for accessing the NodePort Service:

```bash
minikube service flask-app-service --url
```

Example:

```text
http://127.0.0.1:xxxxx
```

The actual port may be different depending on the Minikube environment.

Test the application using:

```bash
curl http://127.0.0.1:<PORT>
```

Expected response:

```text
Hello from Flask on Kubernetes!
```

## 🔄 Application Architecture

```text
                    Minikube Cluster
                           |
                           |
                    Kubernetes Deployment
                           |
                           |
                    Flask Application Pod
                           |
                    Container Port 15000
                           |
                           |
                  flask-app-service
                       NodePort
                           |
                           |
                     External Request
                           |
                           ↓
             Hello from Flask on Kubernetes!
```

## 🧪 Verification Commands

The following commands can be used to verify the deployment:

```bash
minikube status
```

```bash
kubectl get deployments
```

```bash
kubectl get pods
```

```bash
kubectl get services
```

```bash
kubectl describe deployment flask-app
```

```bash
kubectl logs <pod-name>
```

```bash
minikube service flask-app-service --url
```

## ✅ Result

The Flask application was successfully:

1. Created using Python and Flask.
2. Containerized using Docker.
3. Built as the `flask-app:latest` Docker image.
4. Loaded into Minikube.
5. Deployed as a Kubernetes Deployment.
6. Run successfully inside a Kubernetes Pod.
7. Exposed using a Kubernetes NodePort Service.
8. Accessed successfully through Minikube.

### Final Output

```text
Hello from Flask on Kubernetes!
```

## 👩‍💻 Author

**Dhanushree C S **

---

## 📚 References

* Minikube Documentation
* Kubernetes Documentation
* Flask Documentation
* Docker Documentation


