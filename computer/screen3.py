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

# setup the display and initial icons
digoleDisplay = display.Display('center', settings.digoleDisplayDriverLocation)
digoleDisplay.resetScreen()
digoleDisplay.displayIcon('driving', 10, 175)

currentIcon = ''
def getCurrentWeather():
    """get current weather"""
    global currentIcon
    weatherDetails = WeatherDetails.WeatherDetails('weather.data')
    if currentIcon != str(weatherDetails.icon):
        print weatherDetails.icon
        digoleDisplay.displayIcon(str(weatherDetails.icon), 10, 10)
        currentIcon = str(weatherDetails.icon)    
    digoleDisplay.printByFontColorPosition(18, 255, 10, 100, weatherDetails.summary[0:30], getframeinfo(currentframe()))
    digoleDisplay.printByFontColorPosition(18, 255, 20, 130, weatherDetails.nextHour[0:25], getframeinfo(currentframe()))
    digoleDisplay.printByFontColorPosition(18, 255, 25, 150, weatherDetails.nextHour[25:50] + '...', getframeinfo(currentframe()))
    digoleDisplay.printByFontColorPosition(18, 223, 85, 30, str(int(weatherDetails.apparentTemperature)) + chr(176) + " / " + str(int(weatherDetails.humidity * 100)) + "%", getframeinfo(currentframe()))
    digoleDisplay.printByFontColorPosition(18, 223, 35, 188, str(int(weatherDetails.windSpeed)) + ' mph', getframeinfo(currentframe()))
    showHourlyColorCodes(weatherDetails.upcomingConditions)

def getCabinConditions():
    """get current conditions inside the car/cabin"""
    currentReadings = CurrentReadings.CurrentReadings('temp.data')    
    digoleDisplay.printByFontColorPosition(18, 254, 90, 55, "Inside: " + str(int(currentReadings.temp)) + chr(176) + " / " + str(int(currentReadings.hmidty)) + "%", getframeinfo(currentframe()))
    
def showHourlyColorCodes(hourlyConditions):
    """show hourly sky conditions"""
    stepCount = 22
    currentStep = 10
    for hourlyMeasurement in hourlyConditions:
        digoleDisplay.setColor('146')
        if hourlyMeasurement["icon"] == "clear-day":
            digoleDisplay.setColor('146')
        if hourlyMeasurement["icon"] == "clear-night":
            digoleDisplay.setColor('146')
        if hourlyMeasurement["icon"] == "rain":
            digoleDisplay.setColor('7')
        if hourlyMeasurement["icon"] == "sleet":
            digoleDisplay.setColor('7')
        if hourlyMeasurement["icon"] == "snow":
            digoleDisplay.setColor('7')        
        digoleDisplay.drawBox(str(currentStep), "210", "20", "20")
        currentStep = currentStep + stepCount

while True:
    getCurrentWeather()
    getCabinConditions()
    time.sleep(1)

