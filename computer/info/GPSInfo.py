#!/usr/bin/python
# Current GPS readings
# Kevin Hinds http://www.kevinhinds.com
# License: GPL 2.0
import json
import includes.data as data

class GPSInfo:
    '''GPS info as class to persist as JSON information to file'''
    jsonFile = ''
    latitude = 0
    longitude = 0
    altitude = 0
    speed = -1
    climb = 0
    track = 0
    mode = 0
    timeSet = False

    def __init__(self, jsonFile):
        self.latitude = 0
        self.longitude = 0
        self.altitude = 0
        self.speed = 0
        self.climb = 0
        self.track = 0
        self.mode = 0
        self.timeSet = False
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
