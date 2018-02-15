#!/bin/bash
#Setting up ROS and Exporting the core

#export ROS_MASTER_URI=http://192.168.147.221:11311
#export ROS_IP=192.168.147.221

export ROS_MASTER_URI=http://odroid:11311
export ROS_IP=odroid
source catkin_ws/devel/setup.bash
#roslaunch usb_cam usb_cam-test.launch &
#source catkin_ws/devel/setup.bash
rosbag play airground_rig_s3_2013-03-18_21-38-48.bag &
roslaunch svo_ros test_rig3.launch 

#rosrun svo_analysis benchmark.py sin2_tex2_h1_v8_d
