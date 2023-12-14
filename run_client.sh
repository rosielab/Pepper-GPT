
source /opt/ros/noetic/setup.bash
cd /workdir/catkin_ws/
catkin_make
source ./devel/setup.bash
export ROS_MASTER_URI=http://naoqi_driver:11311
rosrun chat-client client_node.py