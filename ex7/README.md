# Exercise 7: Jenkins CI Automation

## Objective

To understand Continuous Integration (CI), install Jenkins using Docker, and create a pipeline that automates a sample build, testing, and artifact archiving process.

## Tools and Technologies

- Jenkins
- Docker and Docker Desktop
- Ubuntu (WSL)
- Visual Studio Code
- Jenkins Pipeline

## Introduction

Continuous Integration is a software development practice in which code changes are integrated frequently and automatically validated through builds and tests.

Jenkins is an open-source automation server that helps automate build, test, and delivery workflows through jobs, pipelines, and plugins.

## Jenkins Installation

Jenkins was started using Docker with the following command:

```bash
docker run -d \
  --name jenkins \
  --restart unless-stopped \
  -p 8080:8080 \
  -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  jenkins/jenkins:lts
```

The Jenkins web interface was accessed at:

http://localhost:8080/

The initial administrator password was retrieved from the Jenkins container. Jenkins setup was completed by installing suggested plugins and creating an administrator account.

## CI Pipeline

A pipeline job named `Exercise-7-CI` was configured in Jenkins.

The pipeline consists of three stages:

1. **Build:** Creates a sample build artifact at `build-output/app.txt`.
2. **Test:** Verifies that the artifact exists and contains the expected text.
3. **Package:** Archives the generated artifact in Jenkins.

The pipeline also reports success or failure in the build logs.

## Execution and Verification

The pipeline was executed through the Jenkins dashboard. The console output was checked to verify that the build and tests completed successfully.

The archived artifact was verified through the Jenkins build page.

## Results

The exercise demonstrates a basic Jenkins CI workflow with automated build steps, validation, build logs, and artifact archiving.

## Screenshots

Screenshots of the Jenkins container, dashboard, pipeline configuration, successful build, console output, and archived artifact are stored in the `screenshots/` directory.

## Conclusion

This exercise provided practical experience with Jenkins installation using Docker, initial configuration, pipeline creation, automated testing, and build artifact archiving.

## Repository Structure

```text
ex7/
├── Jenkinsfile
├── README.md
└── screenshots/
    ├── jenkins-container.png
    ├── jenkins-dashboard.png
    ├── pipeline-configuration.png
    ├── pipeline-success.png
    ├── console-output.png
    └── archived-artifact.png
```