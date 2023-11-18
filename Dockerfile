FROM arm64v8/ros:noetic-robot

RUN sudo apt-get update
RUN sudo apt-get install -y ros-noetic-ros-tutorials
RUN sudo apt-get install -y ros-noetic-naoqi-bridge-msgs

WORKDIR /workdir

COPY . /workdir/
