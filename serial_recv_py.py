#! /usr/bin/env python3
import sys
import time
from time import strftime
import datetime
import serial

try:
    ser = serial.Serial(
              
        port='/dev/ttys002',
        baudrate = 9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
        )
    print "Connected to " + str(ser.port)
    print "Baud rate is " + str(ser.baudrate)
except:
    print "Failed to open serial port..."
    sys.exit(1)

          
      
while True:
    print "Listening to serial port for incoming data..."
    data = ser.readline()
    
    if data:
        print "Received data is " + str(data)

    else:
        print "No data found. Timeout reached. Trying again..."

ser.close()
print "Closed Serial port. Program terminates..."
