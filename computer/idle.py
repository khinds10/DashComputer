#!/usr/bin/python
# Check if the car power is on or off based on relay status
# Kevin Hinds http://www.kevinhinds.com
# License: GPL 2.0
import os, time, json
import RPi.GPIO as GPIO
import includes.data as data
import includes.postgres as postgres
import info.Idle as Idle

# pin 18/24 setup for high low detection from the relay (which shows the car power on)
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# start idle tracker, we're just starting up so the car must be not idle / started
idleStatus = Idle.Idle('idle.data')
idleStatus.isIdle = "no"
idleStatus.saveData()
isIdle = False
while True:
    try:
        # button pressed
        input_state = GPIO.input(24) 
        if input_state == False: 
            if isIdle == True:
                postgres.startNewTrip()
                isIdle = False
                idleStatus.isIdle = "no"
                idleStatus.saveData()
        else:
            if isIdle == False:
                postgres.startNewIdle()   
                isIdle = True
                idleStatus.isIdle = "yes"
                idleStatus.saveData()
        time.sleep(0.2)
    except (Exception):
        pass
