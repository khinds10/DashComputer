#!/usr/bin/python
# Current summarized driving statistics
# Kevin Hinds http://www.kevinhinds.com
# License: GPL 2.0
import json
import includes.data as data
import includes.settings as settings

class RPi:
    """Internal Raspberry PI environment values to save as class to persist as JSON information to file"""
    jsonFile = ''
    cpuPercent = 0
    cpuTemperature = 0    
    ramTotalMB = 0
    ramFreeMB = 0
    ramUsedMB = 0
    diskTotalMB = 0
    diskFreeMB = 0
    diskUsedPercent = 0
        
    def __init__(self, jsonFile):
        self.jsonFile = jsonFile
        self.cpuPercent = 0
        self.cpuTemperature = 0    
        self.ramTotalMB = 0
        self.ramFreeMB = 0
        self.ramUsedMB = 0
        self.diskTotalMB = 0
        self.diskFreeMB = 0
        self.diskUsedPercent = 0
        self.getData()

    def getData(self):
        '''hydrate from specific json file specified in the object constructor'''
        readings = data.getJSONFromDataFile(self.jsonFile)        
        for attr, value in self.__dict__.iteritems():
            setattr(self, attr, readings[attr])

    def to_JSON(self):
        """stringify object to JSON"""
        return json.dumps(self, default=lambda o: o.__dict__,sort_keys=True, indent=4)
        
    def saveData(self):
        """create or rewrite object to data file as JSON"""
        f = file(settings.logFilesLocation + self.jsonFile, "w")
        f.write(str(self.to_JSON()))
