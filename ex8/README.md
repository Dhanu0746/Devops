# Exercise 8: Creating a Hello World Jenkins Job

## Objective
To create a shell script, store it in a GitHub repository, and configure a Jenkins Freestyle job to retrieve and execute the script automatically.

## Tools and Technologies
- Ubuntu (WSL)
- Git and GitHub
- Jenkins
- Bash Shell
- Visual Studio Code

## Project Structure

```text
ex8/
├── hello-world.sh
├── README.md
└── screenshots/
    ├── 01-github-repository.png
    ├── 02-hello-world-script.png
    ├── 03-jenkins-configuration.png
    ├── 04-jenkins-success.png
    └── 05-console-output.png
```

## Step 1: Create the Shell Script

Created a file named `hello-world.sh` with the following content:

```bash
#!/bin/bash
echo "Hello, Jenkins!"
```

Made the script executable and tested it in Ubuntu.

```bash
chmod +x hello-world.sh
./hello-world.sh
```

**Output:**

```text
Hello, Jenkins!
```

## Step 2: Upload the Script to GitHub

Uploaded `hello-world.sh` to the `ex8` directory of the GitHub repository.

Repository: https://github.com/Dhanu0746/Devops

## Step 3: Configure Jenkins

Created a Freestyle project named `HelloWorld` and configured the following settings:

- **Source Code Management:** Git
- **Repository URL:** `https://github.com/Dhanu0746/Devops.git`
- **Branch Specifier:** `*/main`
- **Build Step:** Execute shell
- **Build Command:** `sh ex8/hello-world.sh`

Jenkins retrieves the source code from GitHub before executing the build step.

## Step 4: Execute the Jenkins Job

Saved the configuration and selected **Build Now** to execute the job.

Opened the build's Console Output to verify the execution result.

**Expected Output:**

```text
Hello, Jenkins!
Finished: SUCCESS
```

## Result

Successfully created and tested the Hello World shell script in Ubuntu, uploaded it to GitHub, and configured a Jenkins Freestyle project to retrieve and execute the script. The expected output was verified in the Jenkins Console Output.

## Screenshots

The following screenshots provide evidence of the completed exercise:

1. GitHub repository containing the shell script.
2. Contents of `hello-world.sh`.
3. Jenkins job configuration.
4. Jenkins job showing a successful build.
5. Jenkins Console Output displaying `Hello, Jenkins!` and `Finished: SUCCESS`.