#!/bin/bash
#Setting up ROS and Exporting the core
source catkin_ws/devel/setup.bash
export ROS_MASTER_URI=http://192.168.147.232:11311 #use odroid's IP or hostname here
export ROS_IP=192.168.147.232 #Odroid's IP

sleep 5 #delay of 5 sec to allow usb_cam to run before svo launch

roslaunch svo_ros test.launch
