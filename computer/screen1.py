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

# setup display and icons
digoleDisplay = display.Display('center', settings.digoleDisplayDriverLocation)
digoleDisplay.resetScreen()
digoleDisplay.displayIcon('driving', 10, 10)
digoleDisplay.displayIcon('driving', 175, 12)
digoleDisplay.displayIcon('driving', 175, 43)
digoleDisplay.displayIcon('speed', 10, 55)
digoleDisplay.displayIcon('traffic', 10, 85)

# start tracking notifications
data.removeJSONFile('notification.data')
previousMessage = "Welcome to Kevin's Car"
firstRun = True

def showTime():
    digoleDisplay.printByFontColorPosition(120, 223, 10, 200, dt.datetime.now(pytz.timezone('US/Eastern')).strftime('%-I:%M %p'), 'currentTime')

def getLocale():
    localeInfo = LocaleDetails.LocaleDetails('address.data')
    digoleDisplay.printByFontColorPosition(18, 222, 120, 230, localeInfo.city, 'localeInfoCity')

def getTripStats():
    statisticsInfo = Statistics.Statistics('stats.data')
    digoleDisplay.printByFontColorPosition(18, 255, 35, 23, 'Trip: ' + str(statisticsInfo.drivingTimes[0]), 'statisticsInfoAverageSpeeds')
    digoleDisplay.printByFontColorPosition(18, 255, 35, 68, str(statisticsInfo.milesTravelled[0]) + ' mi', 'statisticsInfoAverageSpeeds')
    digoleDisplay.printByFontColorPosition(18, 255, 35, 98, str(statisticsInfo.inTrafficTimes[0]) + '%', 'statisticsInfoAverageSpeeds')
    digoleDisplay.printByFontColorPosition(18, 222, 200, 23, 'Last: ' + str(statisticsInfo.drivingTimes[1]), 'statisticsInfoAverageSpeeds')
    digoleDisplay.printByFontColorPosition(18, 254, 200, 55, 'Idle: Xh Xm', 'statisticsInfoAverageSpeeds')    

def showMessage():
    digoleDisplay.printByFontColorPosition(18, 255, 20, 140, 'Welcome to Kevin\'s Car', 'statisticsInfoAverageSpeeds')

# each 5 seconds check for new messages
while True:
    showTime()
    getLocale()
    getTripStats()

    #showMessage()
    firstRun = False
    time.sleep(5)

#def checkForMessage():
#    """check for new messages"""
#    incomingMessage = json.loads(unicode(subprocess.check_output(['curl', settings.dashboardServer + "/message"]), errors='ignore'))
#    return str(incomingMessage["message"])

#def saveMessageToFile(message):
#    """save new notification message to file for gauge to display"""
#    notification = Notification.Notification()
#    notification.message = message
#    data.saveJSONObjToFile('notification.data', notification)
#    
## save the initial welcome message
#saveMessageToFile(previousMessage)


#while True:
#    try:
#        # if we're running the first time, no need to display an old message I already have read
#        if (firstRun):
#            previousMessage = checkForMessage()
#        else:
#            # if message has changed, then save the new one to the file
#            message = checkForMessage()
#            if (previousMessage != message):
#                saveMessageToFile(message)
#                previousMessage = message





























