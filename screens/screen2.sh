#!/bin/bash
# def resetScreen():
#    """clear and rotate screen"""
#    subprocess.call([digoleDriveLocation, "clear"])
#    subprocess.call([digoleDriveLocation, "setRot90"])

# def setFont(fontSize):
#    """set font size for screen"""
#    subprocess.call([digoleDriveLocation, "setFont", fontSize])
#    
# def setColor(fontColor):
#    """set font color for screen"""
#    subprocess.call([digoleDriveLocation, "setColor", fontColor])

# def printByFontColorPosition(fontSize, fontColor, x, y, text, previousText):
#    """erase existing text and print at x,y """
#    setFont(fontSize)
#    
#    # print the previous text in black to then print the new text
#    setColor("0")
#    subprocess.call([digoleDriveLocation, "printxy_abs", x, y, previousText])
#    
#    # print the new text at the desired color, x, y and font size
#    setColor(fontColor)
#    subprocess.call([digoleDriveLocation, "printxy_abs", x, y, text])

# fonts[] = {6, 10, 18, 51, 120, 123};

# Light Colors

#    FF = 255 (white)
#    FA = 250 (orange)
#    FE = 254 (yellow)
#    DF = 223 (blue)
#    DE = 222 (green)
#    FB = 251 (purple)
#    
# Bright Colors

#    1C = 28 (green)
#    F9 = 249 (orange)
#    FC = 252 (yellow)
#    E0 = 224 (red)
#    0B = 11 (blue)
#    EB = 235 (purple)
#    F0 = 240 (orange)

# ICONS
# driving 10 10
# calendar 10 10
# compass 10 10
# gps 10 10
# speed 10 10
# traffic 10 10
# temp 10 10
# noWifi 10 10
# wifi 10 10
# rainIcon 10 10
# snowIcon 10 10
# snow 10 10
# rain 10 10
# clearDay 10 10
# clearNight 10 10
# cloudy 10 10
# fog 10 10
# partlyCloudyDay 10 10
# partlyCloudyNight 10 10
# sleet 10 10
# wind 10 10

../digole/center-display clear
../digole/center-display setRot90
../digole/center-display setFont 18

../digole/center-display setColor 255
../digole/center-display driving 10 12
../digole/center-display printxy_abs 40 25 "Avg. 10 mph"
../digole/center-display printxy_abs 10 45 "[9 miles]"

../digole/center-display driving 10 12
../digole/center-display printxy_abs 10 85 "Alt. 193 ft"
../digole/center-display printxy_abs 10 105 "Climb /"

../digole/center-display speed 10 180
../digole/center-display printxy_abs 40 195 "20 mph"

