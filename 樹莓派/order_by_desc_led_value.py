#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 20:51:30 2020

@author: pi
"""


import RPi.GPIO as GPIO
import time
import pymysql

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

GPIO.setup(23,GPIO.OUT)

servo1 = GPIO.PWM(23,50)
servo1.start(0)

while (True):
    
    try:
        con=pymysql.connect(host='192.168.0.101',
                    user='lihen',
                    password='12345678',
                    db='light_control'
                   )
        a=con.cursor()
        a.execute('SELECT answer FROM light_control_table order by time desc limit 1')
        target=a.fetchall()
        targets=target[0]
        if (targets==('turn_on',)):
            print(targets)
            GPIO.output(18, GPIO.LOW)
        else:
            print(targets)
            GPIO.output(18, GPIO.HIGH) 
        a.execute('SELECT answer FROM rc_server order by time desc limit 1')  
        angle=a.fetchall()
        angle=angle[0]
        print(angle)
        if (angle==('open',)):
            servo1.ChangeDutyCycle(2+(90/18))
            time.sleep(4)
            servo1.ChangeDutyCycle(2+(0/18))
            time.sleep(0.5)
            servo1.ChangeDutyCycle(0)
            angle='close'
            a.execute("INSERT INTO rc_server(answer) VALUES ('%s')"%(angle))
            con.commit()
        time.sleep(2)
    except KeyboardInterrupt:
        servo1.stop()
        GPIO.cleanup()
        break
GPIO.cleanup()