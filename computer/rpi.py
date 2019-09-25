#!/usr/bin/python
# Get local RPI stats such CPU temp / mem used
# Kevin Hinds http://www.kevinhinds.com
# License: GPL 2.0
import Adafruit_DHT
import os, time, json, urllib2
import includes.data as data
import info.RPi as RPi

# start logging Raspberry PI internal stats
rpi = RPi.RPi('rpi.data')
while True:
    rpi.cpuPercent = 0
    rpi.memUsedPercent = 0
    rpi.cpuTemperature = 0
    rpi.saveData()
    time.sleep(5)
