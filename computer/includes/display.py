#! /usr/bin/python
# Display helper functions to set/clear and show data on the digole display
# Kevin Hinds http://www.kevinhinds.com
# License: GPL 2.0
import time, json, string, cgi, subprocess, os
import includes.settings as settings

class Display:
    '''Digole display controller object'''
    screen = ''
    cachedValues = {}
    digoleDisplayDrivers = {}
    
    def __init__(self, screen, driverFileFolder):
        """set display screen to use and init object to use it"""
        self.digoleDisplayDrivers = { "center" : driverFileFolder + "center-display", "left" : driverFileFolder + "left-display", "right" : driverFileFolder + "right-display" }
        self.screen = self.digoleDisplayDrivers[screen]
    
    def resetScreen(self):
        """clear and rotate screen"""
        subprocess.call([self.screen, "clear"])
        subprocess.call([self.screen, "setRot90"])

    def setFont(self, fontSize):
        """set font size for screen"""
        subprocess.call([self.screen, "setFont", str(fontSize)])
        
    def setColor(self, fontColor):
        """set font color for screen"""
        subprocess.call([self.screen, "setColor", str(fontColor)])

    def drawBox(self, x, y, z, w):
        """draw box on the screen"""
        subprocess.call([self.screen, "drawBox", str(x), str(y), str(z), str(w)])

    def drawLine(self, x, y, z, w):
        """draw line on the screen"""
        subprocess.call([self.screen, "drawLine", str(x), str(y), str(z), str(w)])

    def drawCircle(self, x, y, r, f):
        """draw circle on the screen"""
        subprocess.call([self.screen, "drawCircle", str(x), str(y), str(r), str(f)])

    def displayIcon(self, icon, x, y):
        """show icon from prepared icons built in to the driver itself (compiled from C)"""
        subprocess.call([self.screen, str(icon), str(x), str(y)])
        
    def printByFontColorPosition(self, fontSize, fontColor, x, y, text, callFromLine):
        """erase existing text and print at x,y"""

        # cachekey is based on the which script / line number called the print function
        cacheKey = str(callFromLine.filename) + '-' + str(callFromLine.lineno)
        self.setFont(fontSize)
        
        # print the previous text in black to then print the new text if a previous value detected
        if cacheKey in self.cachedValues:
        
            # if there's nothing new to print then just return
            if str(text) == str(self.cachedValues[cacheKey]):
                return

            self.setColor("0")
            subprocess.call([self.screen, "printxy_abs", str(x), str(y), str(self.cachedValues[cacheKey])])
        
        # print the new text at the desired color, x, y and font size
        self.setColor(fontColor)
        subprocess.call([self.screen, "printxy_abs", str(x), str(y), str(text)])
        self.cachedValues[cacheKey] = str(text)
