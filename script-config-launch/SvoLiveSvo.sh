#!/bin/bash
#Setting up ROS and Exporting the core
source catkin_ws/devel/setup.bash
export ROS_MASTER_URI=http://192.168.147.232:11311
export ROS_IP=192.168.147.232 

roslaunch svo_ros test.launch
