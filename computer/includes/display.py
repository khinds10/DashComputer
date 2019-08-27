#! /usr/bin/python
# Display helper functions to set/clear and show data on the digole display
# Kevin Hinds http://www.kevinhinds.com
# License: GPL 2.0
import time, json, string, cgi, subprocess, os
import includes.settings as settings
digoleDisplayDrivers = { "center" : "/home/pi/DashComputer/computer/digole/center-display", "left" : "/home/pi/DashComputer/computer/digole/left-display", "right" : "/home/pi/DashComputer/computer/digole/right-display" }
screen = "center"

def resetScreen():
    """clear and rotate screen"""
    global screen
    subprocess.call([digoleDisplayDrivers[screen], "clear"])
    subprocess.call([digoleDisplayDrivers[screen], "setRot90"])

def setFont(fontSize):
    """set font size for screen"""
    global screen
    subprocess.call([digoleDisplayDrivers[screen], "setFont", str(fontSize)])
    
def setColor(fontColor):
    """set font color for screen"""
    global screen
    subprocess.call([digoleDisplayDrivers[screen], "setColor", str(fontColor)])

def printByFontColorPosition(fontSize, fontColor, x, y, text, previousText):
    """erase existing text and print at x,y """
    global screen
    setFont(fontSize)
    
    # print the previous text in black to then print the new text
    setColor("0")
    subprocess.call([digoleDisplayDrivers[screen], "printxy_abs", str(x), str(y), str(previousText)])
    
    # print the new text at the desired color, x, y and font size
    setColor(fontColor)
    subprocess.call([digoleDisplayDrivers[screen], "printxy_abs", str(x), str(y), str(text)])
