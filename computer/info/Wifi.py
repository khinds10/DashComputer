#!/usr/bin/python
# Wifi Connection Status
# Kevin Hinds http://www.kevinhinds.com
# License: GPL 2.0
import json
import includes.data as data

class Wifi:
    '''Wifi connection status as class to persist as JSON information to file'''
    jsonFile = ''
    isConnected = 'no'

    def __init__(self):
        self.isConnected = 'no'
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
