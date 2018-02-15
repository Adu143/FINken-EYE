#!/bin/bash
#Setting up ROS and Exporting the core
source catkin_workspace/devel/setup.bash
export ROS_MASTER_URI=http://odroid:11311
export ROS_IP=192.168.147.98  #use client system IP or hostname here
echo "ROS setup and core exported."
#rqt
rosrun rviz rviz -d ./working-svo.rviz
