
import docker

client = docker.from_env()
container = None

try:
    print("Building image...")
    client.images.build(path=".", tag="flask-apparmor")

    print("Starting container with AppArmor profile...")
    container = client.containers.run(
        "flask-apparmor",
        ports={"5000/tcp": 5000},
        security_opt=["apparmor=my-apparmor-profile"],
        detach=True,
    )

    print(f"Container started: {container.short_id}")

    info = client.api.inspect_container(container.id)
    print("Requested security options:",
          info["HostConfig"]["SecurityOpt"])

finally:
    if container is not None:
        container.stop()
        container.remove()
        print("Container stopped and removed.")

