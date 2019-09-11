#!/usr/bin/python
# Current Phone Notification
# Kevin Hinds http://www.kevinhinds.com
# License: GPL 2.0
import time, json, string, cgi, subprocess, json
import includes.data as data
import includes.settings as settings

class Notification:
    '''Phone Notification as class to persist as JSON information to file'''
    jsonFile = ''
    message = ''

    def __init__(self, jsonFile):
        self.message = ''
        self.jsonFile = jsonFile
        self.message = self.getMessage()
        self.saveData()
        self.getData()

    def getData(self):
        '''hydrate from specific json file specified in the object constructor'''
        readings = data.getJSONFromDataFile(self.jsonFile)        
        for attr, value in self.__dict__.iteritems():
            setattr(self, attr, readings[attr])

    def getMessage(self):
        """get latest phone message that may have occurred"""
        latestMessage = json.loads(unicode(subprocess.check_output(['curl', settings.dashboardServer + "/message"]), errors='ignore'))
        latestMessage = str(latestMessage['message'])
        return latestMessage    

    def messageChanged(self):
        """check for new notifications updating object, else False"""
        latestMessage = self.getMessage()
        if self.message != latestMessage:
            self.message = latestMessage
            self.saveData()
            return True
        else:
            return False
        
    def to_JSON(self):
        """stringify object to JSON"""
        return json.dumps(self, default=lambda o: o.__dict__,sort_keys=True, indent=4)
        
    def saveData(self):
        """create or rewrite object to data file as JSON"""
        f = file(settings.logFilesLocation + self.jsonFile, "w")
        f.write(str(self.to_JSON()))
