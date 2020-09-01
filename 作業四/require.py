# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import serial
import time
import urllib


ser = serial.Serial("com4", 9600,timeout=0.5)
time.sleep(3)

try:
    while True:
        response = urllib.request.urlopen("http://192.168.0.101/msg.txt")
        lines = response.readlines()
        choice = str(lines[0])
        ser.write(str.encode(choice))
        time.sleep(1)
except KeyboardInterrupt:
    ser.close()
        