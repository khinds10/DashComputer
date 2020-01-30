#!/usr/bin/python
# Show current trip info and summarized/other trip info (by button presses) to Digole display
# Kevin Hinds http://www.kevinhinds.com
# License: GPL 2.0
import datetime as dt
from math import cos, sin, pi, radians
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
import info.Wifi as Wifi
import info.Idle as Idle

# setup the display and initial icons
digoleDisplay = display.Display('center', settings.digoleDisplayDriverLocation)
digoleDisplay.resetScreen()
digoleDisplay.displayIcon('speed', 155, 72)
digoleDisplay.displayIcon('driving', 155, 102)

def showMessage(message):
    print message
    digoleDisplay.printByFontColorPosition(18, 252, 20, 165, str(message), getframeinfo(currentframe()))

def setCompass(x,y, color):
    """ for x,y direction coordinates and color draw the compass with needle """
    digoleDisplay.setColor(255)  
    digoleDisplay.drawCircle("75","60","38","0")
    digoleDisplay.drawCircle("75","60","37","0")
    digoleDisplay.drawCircle("75","60","36","0")
    digoleDisplay.setColor(color)   
    digoleDisplay.drawLine("76", "61", str(x), str(y))
    digoleDisplay.drawLine("75", "60", str(x), str(y))
    digoleDisplay.drawLine("74", "59", str(x), str(y))
    digoleDisplay.drawLine("73", "58", str(x), str(y))

# save previous direction to keep compass refresh rate down
trackPrevious = 0
southPX = 0
southPY = 0
northPX = 0
northPY = 0

# show screen and loop each second
notification = Notification.Notification('notification.data')
messageCheckedWait = 0
showMessageWait = 0
messageToggled = False

while True:
    # every 10 seconds see if the message has changed
    try:        
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
        
        # get if driving or idle
        idleInfo = Idle.Idle('idle.data')
        
        # driving stats
        statisticsInfo = Statistics.Statistics('stats.data')
        digoleDisplay.printByFontColorPosition(18, 255, 180, 115, 'Avg. ' + str(statisticsInfo.averageSpeeds[0]) + ' mph', getframeinfo(currentframe()))
        digoleDisplay.printByFontColorPosition(18, 255, 210, 140, '[' + str(statisticsInfo.milesTravelled[0]) + ' miles]', getframeinfo(currentframe()))
        
        # driving info
        gpsInfo = GPSInfo.GPSInfo('gps.data')
        digoleDisplay.setColor(255)  
        digoleDisplay.printByFontColorPosition(18, 255, 10, 220, 'Alt. ' + str(int(gpsInfo.altitude)) + ' ft', getframeinfo(currentframe()))
        digoleDisplay.printByFontColorPosition(18, 255, 10, 195, 'Climb ' + str(int(gpsInfo.altitude)) + '', getframeinfo(currentframe()))
        if idleInfo.isIdle == "yes":
            digoleDisplay.printByFontColorPosition(18, 255, 180, 85, 'Idle', getframeinfo(currentframe()))
        else:
            digoleDisplay.printByFontColorPosition(18, 255, 180, 85, str(int(gpsInfo.speed)) + ' mph', getframeinfo(currentframe()))

        # get weather details for headlights indicator
        weatherDetails = WeatherDetails.WeatherDetails('weather.data')

        # update compass
        if (int(gpsInfo.speed) > 5):
            if gpsInfo.track != trackPrevious:
                digoleDisplay.printByFontColorPosition(18, 255, 25, 120, str(data.getHeadingByDegrees(gpsInfo.track)), getframeinfo(currentframe()))

                # clear heading
                setCompass(southPX, southPY, "0")
                setCompass(northPX, northPY, "0")

                # radians based on where true north is
                r = radians(360 - gpsInfo.track)
                radius = 38

                # show south
                southPX = round(75 - radius * sin(r))
                southPY = round(60 + radius * cos(r))
                setCompass(southPX, southPY, "255")

                # show north
                northPX = round(75 + radius * sin(r))
                northPY = round(60 - radius * cos(r))
                setCompass(northPX,northPY, "224")
                
            trackPrevious = gpsInfo.track

        # get Wifi connected or not to toggle icon
        wifiConnectedInfo = Wifi.Wifi('wifi.data')    
        if wifiConnectedInfo.isConnected == 'yes':
            digoleDisplay.displayIcon('wifi', 234, 20)
        else:
            digoleDisplay.setColor(0)
            digoleDisplay.drawBox(234, 20, 20, 20)
            
        if weatherDetails.useHeadlights:
            digoleDisplay.displayIcon('beam', 230, 205)
            digoleDisplay.setColor(11)
            digoleDisplay.printByFontColorPosition(10, 11, 190, 190, 'Headlights', getframeinfo(currentframe()))
        else:
            digoleDisplay.setColor(0)
            digoleDisplay.drawBox(230, 200, 24, 25)
            digoleDisplay.printByFontColorPosition(10, 0, 190, 190, 'Headlights', getframeinfo(currentframe()))
    except (Exception):
        pass
    time.sleep(2)
