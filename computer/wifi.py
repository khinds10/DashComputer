#!/usr/bin/python
# Get local internet connected status
# Kevin Hinds http://www.kevinhinds.com
# License: GPL 2.0
import Adafruit_DHT
import os, time, json, urllib2
import includes.data as data
import info.Wifi as Wifi

# start logging temp
wifi = Wifi.Wifi('wifi.data')
while True:
    try:
        urllib2.urlopen('http://www.kevinhinds.net', timeout=1)
        wifi.isConnected = 'yes'
        isInternetConnected = True
    except urllib2.URLError as err:
        wifi.isConnected = 'no'
        isInternetConnected = False
    wifi.saveData()
    time.sleep(5)
