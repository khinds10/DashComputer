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
import info.CurrentReadings as CurrentReadings
import info.WeatherDetails as WeatherDetails
import info.GPSInfo as GPSInfo
import info.CurrentReadings as CurrentReadings
import info.LocaleDetails as LocaleDetails
import info.Statistics as Statistics
import info.Notification as Notification

# setup display and icons
digoleDisplay = display.Display('center', settings.digoleDisplayDriverLocation)
digoleDisplay.resetScreen()
digoleDisplay.displayIcon('driving', 10, 10)
digoleDisplay.displayIcon('driving', 175, 12)
digoleDisplay.displayIcon('driving', 175, 43)
digoleDisplay.displayIcon('speed', 10, 55)
digoleDisplay.displayIcon('traffic', 10, 85)

def showTime():
    digoleDisplay.printByFontColorPosition(120, 223, 10, 200, dt.datetime.now(pytz.timezone('US/Eastern')).strftime('%-I:%M %p'), getframeinfo(currentframe()))

def getLocale():
    localeInfo = LocaleDetails.LocaleDetails('address.data')
    digoleDisplay.printByFontColorPosition(18, 222, 120, 230, localeInfo.city, getframeinfo(currentframe()))

def getTripStats():    
    statisticsInfo = Statistics.Statistics('stats.data')
    digoleDisplay.printByFontColorPosition(18, 255, 35, 23, 'Trip: ' + str(statisticsInfo.drivingTimes[0]), getframeinfo(currentframe()))
    digoleDisplay.printByFontColorPosition(18, 255, 35, 68, str(statisticsInfo.milesTravelled[0]) + ' mi', getframeinfo(currentframe()))
    digoleDisplay.printByFontColorPosition(18, 255, 35, 98, str(statisticsInfo.inTrafficTimes[0]) + '%', getframeinfo(currentframe()))
    digoleDisplay.printByFontColorPosition(18, 222, 200, 23, 'Last: ' + str(statisticsInfo.drivingTimes[1]), getframeinfo(currentframe()))
    
    digoleDisplay.printByFontColorPosition(18, 254, 200, 55, 'Idle: Xh Xm', getframeinfo(currentframe()))

def showMessage(message):
    digoleDisplay.printByFontColorPosition(18, 255, 20, 140, str(message), getframeinfo(currentframe()))

# get routine display info each second
notification = Notification.Notification('notification.data')
messageCheckedWait = 0
showMessageWait = 0
messageToggled = False
while True:
    
    # show stats from JSON files
    showTime()
    getLocale()
    getTripStats()
    
    # every 10 seconds see if the message has changed
    messageCheckedWait = messageCheckedWait + 1
    if messageCheckedWait > 10:
        if notification.messageChanged():
            showMessageWait = 10
        messageCheckedWait = 0

    # if message flagged as changed show it for 10 seconds toggling the first 60 chars    
    if showMessageWait > 0:
        messageToggled = not messageToggled
        showMessageWait = showMessageWait - 1
        if messageToggled:
            showMessage(notification.message[0:30])
        else:
            showMessage(notification.message[30:60])
    else:
        showMessage('')
    time.sleep(1)

