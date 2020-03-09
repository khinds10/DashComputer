#!/usr/bin/python
# Show current trip info and summarized/other trip info (by button presses) to Digole display
# Kevin Hinds http://www.kevinhinds.com
# License: GPL 2.0
import datetime as dt
import pytz
from inspect import currentframe, getframeinfo
import time, json, string, cgi, subprocess, json
import includes.data as data
import includes.display as display
import includes.settings as settings
import info.LocaleDetails as LocaleDetails
import info.Statistics as Statistics
import info.RPi as RPi
import info.Idle as Idle

# setup display and icons
digoleDisplay = display.Display('left', settings.digoleDisplayDriverLocation)
digoleDisplay.resetScreen()
digoleDisplay.displayIcon('driving', 10, 10)
digoleDisplay.displayIcon('driving', 175, 12)
digoleDisplay.displayIcon('idleClock', 175, 43)
digoleDisplay.displayIcon('speed', 10, 55)
digoleDisplay.displayIcon('traffic', 10, 85)
digoleDisplay.displayIcon('nissan', 230, 160)

def showTime():
    digoleDisplay.printByFontColorPosition(120, 223, 10, 200, dt.datetime.now(pytz.timezone('US/Eastern')).strftime('%-I:%M %p'), getframeinfo(currentframe()))

def getLocale():
    localeInfo = LocaleDetails.LocaleDetails('address.data')
    digoleDisplay.printByFontColorPosition(18, 222, 120, 230, localeInfo.county[0:20], getframeinfo(currentframe()))

def showZeros(tripValue):
    if tripValue == "":
        return "0m"
    return tripValue
    
def getTripStats():
    """show driving / idle status for current trip you're in"""
    statisticsInfo = Statistics.Statistics('stats.data')
    idleInfo = Idle.Idle('idle.data')
    drivingMessage = 'Trip: '
    if idleInfo.isIdle == "yes":
        drivingMessage = 'Idle: '
    digoleDisplay.printByFontColorPosition(18, 255, 35, 23, drivingMessage + showZeros(str(statisticsInfo.drivingTimes[0])), getframeinfo(currentframe()))

    # only show in-traffic % / miles travelled if you're currently driving, also switch out the last and idle records to show the correct most recent driving or idling amount
    if idleInfo.isIdle == "no":
        digoleDisplay.printByFontColorPosition(18, 255, 35, 68, str(statisticsInfo.milesTravelled[0]) + ' mi', getframeinfo(currentframe()))
        digoleDisplay.printByFontColorPosition(18, 255, 35, 98, data.calculateInTrafficPercent(str(statisticsInfo.inTrafficTimes[0]), str(statisticsInfo.drivingTimes[0])) + '%', getframeinfo(currentframe()))

    # show the last idle, last trip and current idle or trip time depending on if car is on or off
    drivingTimesOne = showZeros(str(statisticsInfo.drivingTimes[1]))
    drivingTimesTwo = showZeros(str(statisticsInfo.drivingTimes[2]))
    if idleInfo.isIdle == "no":
        drivingTimesOne = showZeros(str(statisticsInfo.drivingTimes[2]))
        drivingTimesTwo = showZeros(str(statisticsInfo.drivingTimes[1]))
    digoleDisplay.printByFontColorPosition(18, 222, 200, 23, 'Last: ' + drivingTimesOne, getframeinfo(currentframe()))
    digoleDisplay.printByFontColorPosition(18, 254, 200, 55, 'Idle: ' + drivingTimesTwo, getframeinfo(currentframe()))

def getRPIStats():
    RPiInfo = RPi.RPi('rpi.data')
    digoleDisplay.printByFontColorPosition(10, 255, 180, 115, "Raspberry PI", getframeinfo(currentframe()))
    digoleDisplay.printByFontColorPosition(10, 255, 200, 130, str(RPiInfo.cpuTemperature) + chr(176) + 'f', getframeinfo(currentframe()))
    digoleDisplay.printByFontColorPosition(10, 255, 235, 130,  '/ ' + str(RPiInfo.diskUsedPercent) + "% disk", getframeinfo(currentframe()))
    digoleDisplay.printByFontColorPosition(10, 255, 205, 145,  'RAM: ' + str(int(float(RPiInfo.ramUsedMB) / float(RPiInfo.ramTotalMB) * 100)) + "% used", getframeinfo(currentframe()))

# get routine display info each second - show stats from JSON files
while True:
    try:
        showTime()
        getLocale()
        getTripStats()
        getRPIStats()
    except (Exception):
        pass
    time.sleep(1)
