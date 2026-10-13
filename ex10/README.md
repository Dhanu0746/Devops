# Exercise 10: Multi-Node Kubernetes Deployment with Minikube

## Overview

This exercise demonstrates deploying two Python Flask applications on a multi-node Kubernetes cluster using Minikube. The applications are deployed using Kubernetes Deployments and Services, with pod anti-affinity rules to distribute replicas across different nodes.

## Objectives

- Create a three-node Minikube cluster.
- Deploy a Product Catalog application with two replicas.
- Deploy a Shopping Cart application with three replicas.
- Configure pod anti-affinity to distribute replicas across nodes.
- Expose applications using Kubernetes NodePort Services.
- Test application endpoints using HTTP requests.

## Technologies Used

- Python
- Flask
- Docker
- Kubernetes
- Minikube
- YAML
- PowerShell / curl

## Project Structure

```text
ex10/
├── product_catalog.py
├── shopping_cart.py
├── Dockerfile.product
├── Dockerfile.shopping
├── product_catalog_deployment.yaml
├── shopping_cart_deployment.yaml
├── product_catalog_service.yaml
├── shopping_cart_service.yaml
├── README.md
└── screenshots/
```

## Applications

### 1. Product Catalog

The Product Catalog application provides a list of sample products through the `/products` endpoint.

Sample products:

- Laptop — 1200
- Phone — 800
- Headphones — 150

**Endpoint:** `/products`

**Replicas:** 2

### 2. Shopping Cart

The Shopping Cart application provides endpoints to retrieve the cart and add items.

- `GET /cart` — Retrieves the cart contents.
- `POST /cart` — Adds an item to the cart.

**Replicas:** 3

Note: If the application stores cart data only in memory, the cart contents may differ between replicas and may reset when a pod restarts.

## Minikube Cluster Setup

Create a three-node Minikube cluster:

```powershell
minikube start --nodes=3 -p devops-multinode --driver=docker
```

Check the cluster nodes:

```powershell
kubectl --context=devops-multinode get nodes -o wide
```

All three nodes should report `Ready`.

## Build and Load Docker Images

Build the application images from the project directory:

```powershell
docker build -f Dockerfile.product -t product-catalog:latest .
docker build -f Dockerfile.shopping -t shopping-cart:latest .
```

Load the images into the Minikube cluster:

```powershell
minikube -p devops-multinode image load product-catalog:latest
minikube -p devops-multinode image load shopping-cart:latest
```

## Deploy the Applications

Apply the Kubernetes Service manifests:

```powershell
kubectl --context=devops-multinode apply -f product_catalog_service.yaml
kubectl --context=devops-multinode apply -f shopping_cart_service.yaml
```

Apply the Deployment manifests:

```powershell
kubectl --context=devops-multinode apply -f product_catalog_deployment.yaml
kubectl --context=devops-multinode apply -f shopping_cart_deployment.yaml
```

Check deployment status:

```powershell
kubectl --context=devops-multinode get deployments
kubectl --context=devops-multinode get pods -o wide
kubectl --context=devops-multinode get services
```

Expected deployment replicas:

| Application | Desired Replicas |
|---|---:|
| Product Catalog | 2 |
| Shopping Cart | 3 |

The pod anti-affinity rules are configured to spread replicas across the available nodes.

## Testing the Applications

### Product Catalog

Start the Service tunnel:

```powershell
minikube -p devops-multinode service product-catalog-service
```

Keep this terminal open. Use the localhost URL printed by Minikube, replacing the example port below with the actual port:

```powershell
curl.exe http://127.0.0.1:<PRODUCT_PORT>/products
```

Expected response:

```json
[
  {"id": 1, "name": "Laptop", "price": 1200},
  {"id": 2, "name": "Phone", "price": 800},
  {"id": 3, "name": "Headphones", "price": 150}
]
```

### Shopping Cart

Start the Service tunnel in another terminal:

```powershell
minikube -p devops-multinode service shopping-cart-service
```

Keep the tunnel terminal open. Use the actual localhost port printed by Minikube.

Retrieve the cart:

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:<CART_PORT>/cart" -Method Get
```

An empty cart may return:

```json
[]
```

Add an item using PowerShell:

```powershell
$body = @{
    id = 1
    name = "Laptop"
    quantity = 1
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://127.0.0.1:<CART_PORT>/cart" -Method Post -ContentType "application/json" -Body $body
```

Expected response contains the item details:

```json
{
    "id": 1,
    "name": "Laptop",
    "quantity": 1
}
```

Replace `<CART_PORT>` with the actual port printed by Minikube. Keep the relevant tunnel running while testing.

## Verification

Run the following commands to verify the cluster and applications:

```powershell
kubectl --context=devops-multinode get nodes -o wide
kubectl --context=devops-multinode get deployments
kubectl --context=devops-multinode get pods -o wide
kubectl --context=devops-multinode get services
```

Verify that:

- All three nodes are Ready.
- Product Catalog has two available replicas.
- Shopping Cart has three available replicas.
- Pods are distributed across the nodes according to the anti-affinity configuration.
- Both Services are available.
- The `/products` and `/cart` endpoints respond as expected.

## Screenshots

Save the actual screenshots from your completed run in the `screenshots/` directory.

Recommended screenshots:

1. Three-node Minikube cluster.
2. Deployments and replica counts.
3. Pods distributed across the three nodes.
4. Kubernetes Services and NodePort configuration.
5. Product Catalog `/products` response.
6. Shopping Cart GET response.
7. Shopping Cart POST response.

## Conclusion

This exercise demonstrates containerized application deployment on Kubernetes using a three-node Minikube cluster. The Product Catalog and Shopping Cart applications are deployed with multiple replicas, exposed through Kubernetes Services, and tested through HTTP endpoints. Pod anti-affinity helps distribute replicas across different nodes, improving workload distribution and availability.

