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
import info.CurrentReadings as CurrentReadings

# setup the display and initial icons
digoleDisplay = display.Display('right', settings.digoleDisplayDriverLocation)
digoleDisplay.resetScreen()
digoleDisplay.displayIcon('flag', 10, 175)

currentIcon = ''
def getCurrentWeather():
    """get current weather"""
    global currentIcon
    weatherDetails = WeatherDetails.WeatherDetails('weather.data')
    if currentIcon != str(weatherDetails.icon):
        digoleDisplay.displayIcon(str(weatherDetails.icon), 10, 10)
        currentIcon = str(weatherDetails.icon)        
    digoleDisplay.printByFontColorPosition(18, 255, 10, 100, weatherDetails.summary[0:30], getframeinfo(currentframe()))
    digoleDisplay.printByFontColorPosition(18, 255, 20, 130, weatherDetails.nextHour[0:25], getframeinfo(currentframe()))
    if len(weatherDetails.nextHour) > 25:
        digoleDisplay.printByFontColorPosition(18, 255, 25, 150, weatherDetails.nextHour[25:50] + '...', getframeinfo(currentframe()))
    digoleDisplay.printByFontColorPosition(18, 223, 85, 30, str(int(weatherDetails.apparentTemperature)) + chr(176) + " / " + str(int(weatherDetails.humidity * 100)) + "%", getframeinfo(currentframe()))
    digoleDisplay.printByFontColorPosition(18, 223, 35, 188, str(int(weatherDetails.windSpeed)) + ' mph', getframeinfo(currentframe()))
    
    # show daily high and low
    digoleDisplay.printByFontColorPosition(18, 250, 110, 188, 'High: ' + str(int(weatherDetails.apparentTemperatureHigh)) + chr(176), getframeinfo(currentframe()))
    digoleDisplay.printByFontColorPosition(18, 223, 220, 188, 'Low: ' + str(int(weatherDetails.apparentTemperatureLow)) + chr(176), getframeinfo(currentframe()))
    showHourlyColorCodes(weatherDetails.upcomingConditions)
    showPrecipAlert(weatherDetails)
    
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

def showPrecipAlert(weatherDetails):
    ''' show any alerts about upcoming rain/snow based on time temperature '''
   
    # show rain or snow based on temperature
    precipType = 'rainIcon'
    if int(weatherDetails.upcomingConditions[0]['temperature']) < 32:
        precipType = 'snowIcon'
    
    # if alert present then show, solid precip, just say so
    if weatherDetails.isPrecip:
        if weatherDetails.solidPrecip:
            digoleDisplay.displayIcon(precipType, 180, 85)
        else:        
            # show precip ending or starting and number of minutes
            if weatherDetails.precipStarting:
                digoleDisplay.printByFontColorPosition(18, 223, 210, 105, "in", getframeinfo(currentframe()))
            else:
                digoleDisplay.printByFontColorPosition(18, 223, 210, 105, "end", getframeinfo(currentframe()))
            digoleDisplay.displayIcon(precipType, 180, 85)
        digoleDisplay.printByFontColorPosition(18, 223, 250, 105, str(weatherDetails.minute) + ' min', getframeinfo(currentframe()))

while True:
    try:
        getCurrentWeather()
        getCabinConditions()
    except (Exception):
        pass
    time.sleep(5)
