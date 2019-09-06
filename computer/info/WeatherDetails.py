#!/usr/bin/python
# Current Weather conditions
# Kevin Hinds http://www.kevinhinds.com
# License: GPL 2.0
import json
import includes.data as data

class WeatherDetails:
    '''Weather Information as class to persist as JSON information to file'''
    jsonFile = ''
    time = 0
    summary = ''
    nextHour = ''
    icon = ''
    apparentTemperature = 0
    humidity = 0
    precipIntensity = 0
    precipProbability = 0
    windSpeed = 0    
    isPrecip = False
    precipStopping = False
    precipStarting = False
    solidPrecip = False
    minute = 0

    def __init__(self, jsonFile):
        self.time = 0
        self.summary = ''
        self.nextHour = ''
        self.icon = ''
        self.apparentTemperature = 0
        self.humidity = 0
        self.precipIntensity = 0
        self.precipProbability = 0
        self.windSpeed = 0        
        self.isPrecip = False
        self.precipStopping = False
        self.precipStarting = False
        self.solidPrecip = False
        self.minute = 0
        self.jsonFile = jsonFile
        self.getData()

    def getData(self):
        '''hydrate from specific json file specified in the object constructor'''
        readings = data.getJSONFromDataFile(self.jsonFile)
        for attr, value in self.__dict__.iteritems():
            if attr != 'jsonFile':
                setattr(self, attr, readings[attr])

    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,sort_keys=True, indent=4)
