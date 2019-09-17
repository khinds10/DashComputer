#!/usr/bin/python
# Get local temp from DHT11 humidistat 
# Kevin Hinds http://www.kevinhinds.com
# License: GPL 2.0
import Adafruit_DHT
import os, time, json
import includes.data as data
import info.CurrentReadings as CurrentReadings

# set to use DHT11 sensor
sensor = Adafruit_DHT.DHT22
pin = 22

# start logging temp
while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:

        # convert to imperial units, save to JSON file and wait one second
        temperature = 9.0/5.0 * temperature + 32
        currentReadings = CurrentReadings.CurrentReadings('temp.data')
        currentReadings.temp = str(int(temperature))
        currentReadings.hmidty = str(int(humidity))
        currentReadings.saveData()
    time.sleep(1)
