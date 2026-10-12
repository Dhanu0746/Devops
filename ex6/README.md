# Exercise 6: Real-Time Operations Monitoring and Alerting

## Project Overview

This project implements a real-time monitoring and alerting system for a simulated quick-commerce delivery service called **ZAPPTTO**. It uses Python to generate delivery metrics, Prometheus to collect and evaluate metrics, Grafana to visualize operational performance, Docker to containerize services, and Jenkins to automate validation and image building.

## Objectives

- Simulate real-time delivery operations using Python.
- Expose application metrics for Prometheus scraping.
- Monitor delivery counts and average delivery time.
- Configure Prometheus alert rules for operational issues.
- Visualize metrics using a Grafana dashboard.
- Automate project validation and Docker image building with Jenkins.

## Technologies Used

- Python 3
- Prometheus
- Grafana
- Docker
- Docker Compose
- Jenkins
- `prometheus-client`

## Architecture

```text
Python Delivery Simulator
          |
          | Metrics on port 8000
          v
      Prometheus
          |
          | PromQL queries
          v
       Grafana
          |
          v
   Monitoring Dashboard

Jenkins Pipeline
       |
       +--> Validate Project Files
       +--> Validate Prometheus Configuration
       +--> Build Docker Image
       +--> Verify Running Services
```

## Project Structure

```text
delivery_monitoring/
├── delivery_metrics.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── prometheus.yml
├── alert_rules.yml
├── Jenkinsfile
├── .gitignore
├── README.md
├── jenkins/
│   └── Dockerfile
└── screenshots/
    ├── 01-metrics-endpoint.png
    ├── 02-prometheus-targets.png
    ├── 03-grafana-dashboard.png
    ├── 04-pending-alert.png
    ├── 05-delivery-time-alert.png
    └── 06-jenkins-pipeline.png
```

## Application Metrics

The Python application simulates delivery activity and exposes metrics through the `/metrics` endpoint.

| Metric | Description |
|---|---|
| `total_deliveries` | Total simulated deliveries |
| `pending_deliveries` | Number of pending deliveries |
| `on_the_way_deliveries` | Number of deliveries in transit |
| `average_delivery_time_seconds` | Simulated average delivery time in seconds |

## Prometheus Configuration

Prometheus scrapes metrics from the delivery application every five seconds.

- Prometheus UI: http://localhost:9090
- Metrics endpoint: http://localhost:8000/metrics
- Targets page: http://localhost:9090/targets

The Prometheus configuration loads alert rules from `alert_rules.yml`.

## Alert Rules

### 1. High Pending Deliveries

- Expression: `pending_deliveries > 10`
- Duration: 15 seconds
- Severity: Warning

This alert fires when pending deliveries remain above the configured threshold for 15 seconds.

### 2. High Average Delivery Time

- Expression: `average_delivery_time_seconds > 30`
- Duration: 15 seconds
- Severity: Critical

This alert fires when the simulated average delivery time remains above 30 seconds for 15 seconds.

## Grafana Dashboard

Grafana connects to Prometheus using the Docker Compose service URL:

`http://prometheus:9090`

The dashboard contains four panels:

1. Total Deliveries
2. Pending Deliveries
3. On-the-Way Deliveries
4. Average Delivery Time

Grafana UI: http://localhost:3000

For a local first-time Grafana setup, the default credentials may be `admin` / `admin`. Use your configured credentials if they have been changed.

## Jenkins Pipeline

The Jenkins pipeline validates the project, checks the Prometheus configuration, builds the delivery application image, and verifies the running Docker services.

Pipeline stages:

1. Validate Project Files
2. Validate Prometheus Configuration
3. Build Delivery Application
4. Verify Running Services

Jenkins UI: http://localhost:8080

The pipeline requires Jenkins to have Python, Docker CLI, and access to the Docker daemon.

## Setup and Execution

### Prerequisites

- Docker Desktop with a working Docker Engine.
- Docker Compose.
- VS Code.
- Python 3 for local development.
- Jenkins for pipeline execution.

### Start the Monitoring Stack

Open the project directory in VS Code and run the following commands in a terminal with Docker access:

```bash
docker compose config
docker compose up -d --build
docker compose ps
```

### Verify Application Metrics

```bash
curl http://localhost:8000/metrics
```

### Verify Prometheus Targets

Open http://localhost:9090/targets and confirm that the Prometheus and delivery service targets are healthy.

### Access Grafana

Open http://localhost:3000, configure Prometheus as the data source using `http://prometheus:9090`, and create the dashboard panels listed above.

### Run the Jenkins Pipeline

Open http://localhost:8080, select the `Delivery-Monitoring-Pipeline` job, and click **Build Now**. Review the build's Console Output to verify each stage.

## Alert Testing

To test the pending-deliveries alert, temporarily modify the Python simulator:

```python
pending = random.randint(50, 100)
```

To test the average delivery-time alert, temporarily use:

```python
avg_time = random.uniform(40, 50)
```

Rebuild the delivery application after each change:

```bash
docker compose up -d --build delivery-app
```

Wait for the alert's configured duration and check the Prometheus Alerts page.

Restore the normal metric ranges after testing and rebuild the application again.

## Cleanup

Stop the containers:

```bash
docker compose down
```

To also remove persisted Prometheus, Grafana, and Jenkins data, use:

```bash
docker compose down -v
```

**Warning:** The `-v` option deletes the named volumes, including Jenkins configuration and build history.

## Screenshots

Place genuine screenshots of your running application, Prometheus targets, Grafana dashboard, alert tests, and Jenkins build results in the `screenshots/` directory.

## Conclusion

This project demonstrates how application metrics, monitoring dashboards, alert rules, containerization, and CI automation can work together to improve visibility into quick-commerce delivery operations and help identify performance issues.
