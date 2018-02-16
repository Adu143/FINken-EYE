#!/bin/bash
#Setting up ROS and Exporting the core

#export ROS_MASTER_URI=http://192.168.147.221:11311
#export ROS_IP=192.168.147.221

export ROS_MASTER_URI=http://odroid:11311
export ROS_IP=odroid
source catkin_ws/devel/setup.bash
roslaunch usb_cam usb_cam-test.launch &
#source catkin_ws/devel/setup.bash
roslaunch svo_ros test.launch
