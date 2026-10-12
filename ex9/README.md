# Jenkins Multi-Stage Pipeline: Python Flask Application

## 1. Objective

To implement a Jenkins CI/CD pipeline that automates the build, testing, deployment, and verification of a Python Flask application using a Jenkins Declarative Pipeline.

## 2. Technologies Used

- Jenkins
- Docker
- Python 3
- Flask
- Git and GitHub
- Jenkins Declarative Pipeline
- Python unittest

## 3. Project Structure

```text
Devops/
└── ex9/
    ├── app.py
    ├── requirements.txt
    ├── test_app.py
    ├── Jenkinsfile
    ├── README.md
    └── screenshots/
```

## 4. Application Description

The project contains a simple Flask web application with a home route (`/`).

When accessed, the application returns:

```text
Hello, Jenkins Multi-Stage Pipeline!
```

### Files

- **app.py:** Implements the Flask web application.
- **requirements.txt:** Specifies the Python dependencies.
- **test_app.py:** Contains unit tests for the application's home route.
- **Jenkinsfile:** Defines the automated CI/CD pipeline.
- **README.md:** Documents the project and execution steps.
- **screenshots/:** Stores screenshots of the pipeline execution and results.

## 5. Pipeline Stages

### Stage 1: Build

- Checks the installed Python version.
- Creates a Python virtual environment.
- Upgrades pip.
- Installs the dependencies specified in `requirements.txt`.

### Stage 2: Test

- Executes unit tests using Python's unittest framework.
- Verifies that the home route returns HTTP status code 200.
- Checks that the response matches the expected message.

### Stage 3: Deploy

- Creates a deployment directory named `python-app-deploy`.
- Copies `app.py` and `requirements.txt` into the deployment directory.
- Verifies that the deployment files exist.

### Stage 4: Run and Verify Application

- Starts the Flask application.
- Sends an HTTP request to the home route.
- Verifies the HTTP status code and response body.
- Cleans up the application process after verification.

## 6. Setup and Execution

1. Install Docker Desktop and start the Jenkins container.
2. Ensure Python 3, pip, and Python virtual-environment support are available in the Jenkins container.
3. Push the project files to the GitHub repository.
4. Open the Jenkins dashboard.
5. Create a Pipeline job named `Python-MultiStage-Pipeline`.
6. Select **Pipeline script from SCM**.
7. Choose Git and enter the repository URL:

   `https://github.com/Dhanu0746/Devops.git`

8. Set the branch to `*/main`.
9. Set the Script Path to `ex9/Jenkinsfile`.
10. Save the configuration and click **Build Now**.
11. Open Console Output to monitor the pipeline execution.

## 7. Expected Results

A successful pipeline should:

- Install the required Python dependencies.
- Execute the unit tests successfully.
- Copy the application files to the deployment directory.
- Start and verify the Flask application.

Expected console output:

```text
Ran 1 test

OK

HTTP status: 200
Response: Hello, Jenkins Multi-Stage Pipeline!
Application verification successful

Pipeline completed successfully!
Finished: SUCCESS
```

## 8. Deployment Output

The pipeline creates the following directory inside the Jenkins workspace:

```text
python-app-deploy/
├── app.py
├── requirements.txt
├── app.log
└── app.pid
```

The log and PID files are generated when the application starts. The process is cleaned up after verification.

## 9. Screenshots

The `screenshots/` directory can contain the following evidence:

1. Jenkins pipeline stage view.
2. Successful pipeline console output.
3. Unit test results.
4. Project files in VS Code.
5. GitHub repository showing the committed files.

## 10. Conclusion

This exercise demonstrates how Jenkins automates a multi-stage CI/CD workflow for a Python Flask application. The pipeline installs dependencies, executes unit tests, prepares deployment files, and verifies application functionality through an HTTP request.

The exercise provides practical experience with Jenkins Declarative Pipelines, Python testing, GitHub integration, and basic deployment automation.

## Author

DevOps Lab Exercise — Jenkins Multi-Stage Pipeline
