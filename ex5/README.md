# Exercise 5: Docker Security with AppArmor

## 1. Overview

This exercise demonstrates how to apply Linux AppArmor security policies to a Docker container. The goal is to restrict access to sensitive files and limit the execution of potentially dangerous commands.

## 2. Technologies Used

- Ubuntu Linux
- Docker
- AppArmor
- Python 3
- Docker Python SDK
- Flask

## 3. Project Structure

```text
ex5/
├── app.py
├── Dockerfile
├── my-apparmor-profile
├── apply_apparmor.py
├── test_restricted_actions.py
└── README.md
```

## 4. How It Works

1. A Flask application is packaged into a Docker image.
2. A custom AppArmor profile defines permitted and restricted operations.
3. The profile is loaded into the Linux security framework.
4. Docker runs the container with the custom AppArmor profile.
5. Python scripts test access to sensitive files and execution of shell commands.

## 5. Build the Docker Image

```bash
docker build -t flask-apparmor .
```

## 6. Load the AppArmor Profile

Ensure the profile exists at `/etc/apparmor.d/my-apparmor-profile`.

```bash
sudo apparmor_parser -r -W /etc/apparmor.d/my-apparmor-profile
```

Verify the profile:

```bash
sudo aa-status | grep my-apparmor-profile
```

## 7. Run the Container with AppArmor

```bash
sudo docker run --rm \
  --security-opt apparmor=my-apparmor-profile \
  flask-apparmor
```

## 8. Test Restricted Operations

Run the Python test script:

```bash
python3 test_restricted_actions.py
```

Test access to a sensitive file:

```bash
sudo docker run --rm \
  --security-opt apparmor=my-apparmor-profile \
  flask-apparmor cat /etc/passwd
```

Test shell-related restrictions:

```bash
sudo docker run --rm \
  --security-opt apparmor=my-apparmor-profile \
  --entrypoint /bin/sh \
  flask-apparmor -c 'ls -l /bin/bash'
```

The actual result depends on the loaded profile, its rules, and the container image. A permission-denied result demonstrates that the relevant operation is restricted.

## 9. Expected Results

- The custom AppArmor profile is loaded and enforced.
- Access to explicitly restricted files is denied.
- Operations prohibited by the profile are blocked.
- Test containers are stopped and removed after execution.

**Note:** Verify each restriction using the actual terminal output before reporting it as successful.

## 10. Security Benefits

- Restricts a container's access to sensitive files.
- Limits executable access according to defined policy rules.
- Provides an additional layer of defense alongside Docker isolation.
- Helps reduce the impact of compromised applications.

## 11. Conclusion

This exercise demonstrates how a custom AppArmor profile can strengthen Docker container security through mandatory access control. The effectiveness of the restrictions should be confirmed using profile status checks and negative tests.