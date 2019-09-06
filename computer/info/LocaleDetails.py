#!/usr/bin/python
# Current location specific information 
# Kevin Hinds http://www.kevinhinds.com
# License: GPL 2.0
import json
import includes.data as data

class LocaleDetails:
    '''Locale Information as class to persist as JSON information to file'''
    jsonFile = ''
    address = ''
    area = ''
    city = ''
    zipcode = ''
    county = ''
    country = ''

    def __init__(self, jsonFile):
        self.address = ''
        self.area = ''
        self.city = ''
        self.zipcode = ''
        self.county = ''
        self.country = ''
        self.jsonFile = jsonFile
        self.getData()

    def getData(self):
        '''hydrate from specific json file specified in the object constructor'''
        readings = data.getJSONFromDataFile(self.jsonFile)
        for attr, value in self.__dict__.iteritems():
            if attr != 'jsonFile':
                setattr(self, attr, readings[attr])

    def to_JSON(self):
        '''get json data representing this class'''
        return json.dumps(self, default=lambda o: o.__dict__,sort_keys=True, indent=4)
