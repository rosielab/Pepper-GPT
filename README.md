# Pepper GPT

## What is this project?
This is a ROS project that allows the user to have a conversation with [a Pepper robot](https://us.softbankrobotics.com/pepper) through a text client. The project connects with Pepper over the [naoqi_driver](https://github.com/ros-naoqi/naoqi_driver) ROS package and uses a local installation of the [mistral](https://mistral.ai/product/) LLM model supplied by [ollama](https://ollama.ai/).

## The Project Components

This project is comprised of 3 main components. 

1. **The Custom ROS Application:** This is the "custom" component that was created specifically for the Pepper GPT application. This application is a ROS package that asks the user to prompt Pepper and then runs that prompt through an LLM and sends it to Pepper. The source code for this component is in this repository.
2. **The Naoqi Driver:** This is a officially supported ROS package that creates a bridge between the Naoqi OS Pepper runs on any ROS application that wants to connect to it. Within the context of the Pepper GPT project, the only functionality being used from this bridge is the `/speech` topic that it provides. This topic is used to access Pepper's TTS capabilities.
3. **A Local LLM Model:** This component is just a local LLM running on the same machine as the rest of this ROS application. It is run using ollama and can be accessed via HTTP requests. Within the context of Pepper GPT it is used to process the prompts given by the user to Pepper.

## Getting Started
WARNING: Some docker containers are specific to CPU architecture. The containers pulled in this repository are based on an ARM CPU and therefore may have troubles on x86 chips.

This project was made to be fully containerized using Docker.

NOTE: Since this version of the project run fully in Docker, you can run this on any operating system you want. I am running it on MacOS currently.

### 1. Install Docker

Docker is required for the following instructions. If you haven't yet, install it [here](https://docs.docker.com/get-docker/).

### 2. Launch the Containers

All three containers are orchestrated using the `docker-compose.yml` file in this repository. To launch these containers run:
```
docker compose up --build
```
This will launch `ros-app`, `ollama`, and `naoqi_driver`. 

### 3. Run Naoqi Driver

The `naoqi_driver` is run through entering the docker container and running the entrypoint script. 

Open a new terminal and enter the container:
```
docker exec -it naoqi_driver bash
```

Run the entrypoint script to connect to build and launch the naoqi_driver node.
```
source entrypoint.sh
```

If the above entrypoint script does not work, you may have to launch it by hand and change some of the roslaunch arguments. Here is the command:
```
roslaunch naoqi_driver naoqi_driver.launch nao_ip:=10.0.0.4 nao_port:=9503 roscore_ip:=127.0.0.1 network_interface:=eth0 username:=nao password:=nao
```
For more information on what these arguments mean, see this [repo](https://github.com/rosielab/ROStoNAO-Bridge-Docker-Setup).

### 4. Run GPT Client and Server

Once you have the naoqi_driver connected, open up two more terminals. These terminals are where you will run the client and server.
In each new terminal connect to the `ros-app` container.

```
docker exec -it ros-app bash
```

In one terminal, run the client.
```
source run_client.sh
```

In the other, run the server.
```
source run_server.sh
```

## Extra Resources

### Naoqi Driver

- #### [Source](https://github.com/ros-naoqi/naoqi_driver)
- #### [Extra Tutorial](https://github.com/rosielab/ROStoNAO-Bridge-Docker-Setup)

### Ollama (Mistral LLM)

- #### [Documentation](https://ollama.ai/library/mistral)
- #### [Model Library](https://ollama.ai/library)

### ROS

- #### [Tutorials](https://wiki.ros.org/ROS/Tutorials)

### Docker Containers
- #### [My Dockerhub](https://hub.docker.com/repository/docker/benled1/pepper-ros/general)



