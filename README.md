# Pepper GPT

## What is this project?
This is a ROS project that allows the user to have a conversation with Pepper through a text client. The project connects with Pepper over the `naoqi_driver` ros package.

## How to run it.
The project is built entirely with docker containers. This allows it to be run on any operating system that can run Docker Engine (not just Ubuntu 20.04). The docker images that make up this project are all orchestrated via the `docker-compose.yml` file in this repository.

To get started with the project follow the next steps:

1. Build the compose file
```
docker compose up --build
```

2. Start up the `naoqi_driver`.

The naoqi_driver docker container is now running, however, the actual driver ros node inside it is not. We need to start this up. To do so, open a terminal inside the naoqi_driver container and run the following commands.

Build driver from source.
```
cd ~/catkin_ws/
source /opt/ros/noetic/setup.bash
catkin_make
source ./devel/setup.bash
```

Launch the driver node.
```
roslaunch naoqi_driver naoqi_driver.launch nao_ip:=10.0.0.4 nao_port:=9503 roscore_ip:=127.0.0.1 network_interface:=eth0 username:=nao password:=nao
```

If you have any troubles, please check the documentation on starting up a naoqi_driver node [here](https://github.com/rosielab/ROStoNAO-Bridge-Docker-Setup).

3. Open your development environment.

When developing on this project you will be editing code within the `gpt-development` container. This container has also been started up with the `docker compose up` command. In order to access it, you can use the [VSCode Dev Containers](https://code.visualstudio.com/docs/devcontainers/tutorial) extension to connect to the container.

The linked tutorial will show you how to get started with this extension, however instead of selecting "New Dev Container" we will be selecting "Attach to a Running Container" from the command palette.

Once you have attached to the container, you should have a VSCode window that is running inside of the `gpt-development` container. From here you can edit source code, build the project, and run it.