#!/usr/bin/env python
import rospy
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import TwistStamped
import threading
import serial
import struct
# import test_decoder_odroid.py as fun1
import receiver.py as rd
import time

tLock = threading.Lock()
EVENT = chr(0x00)
START_BYTE = chr(0x99)
END_BYTE = chr(0x55)
ESC_BYTE = chr(0xD3)
# serPort = serial.Serial('/dev/ttyUSB0', 9600)

def sendData(dataToSend):
	# code to write data	
	serPort.write(START_BYTE)
	serPort.flush()
	for eachByte in dataToSend:
		if eachByte == START_BYTE or eachByte == END_BYTE or eachByte == ESC_BYTE:
			serPort.write(ESC_BYTE)
			serPort.write(chr(ord(eachByte) ^ ord(ESC_BYTE)))
			serPort.flush()
		else:
			serPort.write(eachByte)
			serPort.flush()
	serPort.write(END_BYTE)
	serPort.flush()

def velocity_callback(data):
	EVENT = chr(0x11)
	velocityData = ''
	velocityData += EVENT
	velocityData += struct.pack('>d', data.twist.linear.x)
	velocityData += struct.pack('>d', data.twist.linear.y)
	velocityData += struct.pack('>d', data.twist.linear.z)
	sendData(velocityData)

def position_callback(data):
	EVENT = chr(0x22)
	positionData = ''	
	positionData += EVENT
	positionData += struct.pack('>d', data.pose.position.x)
	positionData += struct.pack('>d', data.pose.position.y)
	positionData += struct.pack('>d', data.pose.position.z)
	# print(struct.unpack('>B3d', positionData))
	sendData(positionData)
		
if __name__== "__main__":
	rospy.init_node("communication")
	while not rospy.is_shutdown():
		try:
			rospy.Subscriber("/copters/1/VelocityGoal", TwistStamped, velocity_callback)
			rospy.Subscriber("/copters/1/PoseGoal", PoseStamped, position_callback)	
		#	background = AsyncWrite()
		#	background.start()
			rospy.spin()
		except Exception as e:
			rospy.loginfo(e)


# def sendData(dataToSend):
# 	# code to write data
# 	data = ''	
# 	data += START_BYTE
# 	for eachByte in dataToSend:
# 		if (eachByte == START_BYTE or eachByte == END_BYTE or eachByte == ESC_BYTE):
# 			data += ESC_BYTE
# 			data += (chr(ord(eachByte) ^ ord(ESC_BYTE)))
# 		else:
# 			data += eachByte
# 	data += END_BYTE
# 	print(data)
# 	print(len(data))
