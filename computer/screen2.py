#!/usr/bin/python
# Show current trip info and summarized/other trip info (by button presses) to Digole display
# Kevin Hinds http://www.kevinhinds.com
# License: GPL 2.0
import datetime as dt
import pytz
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

# setup the display and initial icons
digoleDisplay = display.Display('center', settings.digoleDisplayDriverLocation)
digoleDisplay.resetScreen()
digoleDisplay.displayIcon(driving, 10, 12)
digoleDisplay.displayIcon(speed, 10, 180)

while True:
    
    # driving stats
    statisticsInfo = Statistics.Statistics('stats.data')
    display.printByFontColorPosition(18, 255, 40, 25, 'Avg. ' + statisticsInfo.averageSpeeds[0] + ' mph', 'statisticsInfoAverageSpeeds')
    display.printByFontColorPosition(18, 255, 10, 45, '[' + statisticsInfo.milesTravelled[0] + ' miles]', 'statisticsInfoAverageSpeeds')
    
    # driving info
    gpsInfo = GPSInfo.GPSInfo('gps.data')    
    display.printByFontColorPosition(18, 255, 10, 85, 'Alt. ' + str(int(gpsInfo.altitude)) + ' ft', 'gpsInfoAltitude')
    display.printByFontColorPosition(18, 255, 10, 105, 'Climb ' + gpsInfo.climb + '', 'gpsInfoClimb')
    display.printByFontColorPosition(18, 255, 40, 195, str(int(gpsInfo.speed)) + ' mph', 'gpsInfoClimb')
    
    time.sleep(1)





    





