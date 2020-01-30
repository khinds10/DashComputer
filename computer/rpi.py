#!/usr/bin/python
# Get local RPI stats such CPU temp / mem used
# Kevin Hinds http://www.kevinhinds.com
# License: GPL 2.0
import Adafruit_DHT
import os, time, json, urllib2
import includes.data as data
import info.RPi as RPi

def getCPUtemperature():
    '''Return CPU temperature as a character string'''
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=","").replace("'C\n",""))

def getRAMinfo():
    '''Return RAM information (unit=kb) in a list - Index 0: total RAM - Index 1: used RAM - Index 2: free RAM'''
    p = os.popen('free')
    i = 0
    while 1:
        i = i + 1
        line = p.readline()
        if i==2:
            return(line.split()[1:4])

def getCPUuse():
    '''Return % of CPU used by user as a character string'''
    cpu = os.popen("top -n5 | awk '/Cpu\(s\):/ {print $8}'").readlines().pop().strip()
    return int(100-float(cpu))

def getDiskSpace():
    '''Return information about disk space as a list (unit included) - Index 0: total disk space - Index 1: used disk space - Index 2: remaining disk space - Index 3: percentage of disk used'''
    p = os.popen("df -h /")
    i = 0
    while 1:
        i = i +1
        line = p.readline()
        if i==2:
            return(line.split()[1:5])

# start logging Raspberry PI internal stats
rpi = RPi.RPi('rpi.data')
while True:
    try:
        ramStats = getRAMinfo()
        diskStats = getDiskSpace()    
        rpi.cpuPercent = int(getCPUuse())
        rpi.cpuTemperature = int(9.0/5.0 * float(getCPUtemperature()) + 32)
        rpi.ramTotalMB = int(int(ramStats[0]) / 1000)
        rpi.ramFreeMB = int(int(ramStats[2]) / 1000)
        rpi.ramUsedMB = int(int(ramStats[1]) / 1000)
        rpi.diskTotalMB = int(float(diskStats[0].strip('G')))
        rpi.diskFreeMB = int(float(diskStats[1].strip('G')))
        rpi.diskUsedPercent = int(diskStats[3].strip('%'))
        rpi.saveData()
    except (Exception):
        pass
    time.sleep(5)
