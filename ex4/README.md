# Docker Networking with Multiple Containers

## Objective

To understand Docker networking concepts and configure a multi-container application using a user-defined bridge network.

## Overview

This lab demonstrates how to create a custom Docker bridge network and connect three containers to it:

- **Flask:** A Python-based REST API.
- **MySQL:** A relational database container.
- **Redis:** An in-memory cache container.

The containers communicate over the same Docker network using their container names.

## Technologies Used

- Docker
- Python
- Flask
- MySQL
- Redis
- Docker Bridge Networking

## Project Structure

```text
ex4/
├── app.py
├── requirements.txt
├── Dockerfile
├── README.md
└── screenshots/
```

## Implementation

### 1. Create a Bridge Network

```bash
docker network create --driver bridge my-bridge-net
```

### 2. Verify and Inspect the Network

```bash
docker network ls
docker network inspect my-bridge-net
```

### 3. Build the Flask Docker Image

```bash
docker build -t flask-api .
```

The Flask application exposes a REST endpoint at `/about`, which returns the API name, version, and description in JSON format.

### 4. Launch the Containers

Start MySQL:

```bash
docker run -d --name mysql --network my-bridge-net -e MYSQL_ROOT_PASSWORD=LabRoot123! mysql:latest
```

Start Redis:

```bash
docker run -d --name redis --network my-bridge-net redis:latest
```

Start Flask:

```bash
docker run -d --name flask --network my-bridge-net -p 5001:5001 flask-api
```

Verify running containers:

```bash
docker ps
```

### 5. Test the Flask API

Open the following URL in a browser:

```text
http://localhost:5001/about
```

Alternatively, use PowerShell:

```powershell
Invoke-RestMethod http://localhost:5001/about
```

The API returns a JSON response containing the application name, version, and description.

### 6. Test Container Connectivity

Resolve the MySQL container name:

```bash
docker exec flask python -c "import socket; print(socket.gethostbyname('mysql'))"
```

Resolve the Redis container name:

```bash
docker exec flask python -c "import socket; print(socket.gethostbyname('redis'))"
```

Test the MySQL service port:

```bash
docker exec flask python -c "import socket; s=socket.create_connection(('mysql',3306),5); print('MySQL connection successful'); s.close()"
```

Test the Redis service port:

```bash
docker exec flask python -c "import socket; s=socket.create_connection(('redis',6379),5); print('Redis connection successful'); s.close()"
```

These tests demonstrate container-name resolution and network connectivity between services.

## Key Concepts Learned

- Creating and inspecting user-defined bridge networks.
- Connecting multiple containers to a common network.
- Using Docker DNS to resolve container names.
- Publishing container ports using the `-p` option.
- Building a Docker image for a Flask application.
- Testing connectivity between containers.

## Cleanup

Stop and remove the containers:

```bash
docker stop mysql redis flask
docker rm mysql redis flask
```

Remove the custom bridge network:

```bash
docker network rm my-bridge-net
```

## Conclusion

This lab demonstrates how Docker bridge networking enables communication between multiple containers on a shared network. The Flask API can be accessed from the host machine through port mapping, while MySQL and Redis are reachable by their container names over the internal Docker network.