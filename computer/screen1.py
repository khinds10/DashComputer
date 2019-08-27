#!/usr/bin/python
# Show current trip info and summarized/other trip info (by button presses) to Digole display
# Kevin Hinds http://www.kevinhinds.com
# License: GPL 2.0
import datetime as dt
import pytz
import time, json, string, cgi, subprocess, json
import includes.data as data
import includes.display as display

screen = "center"
display.resetScreen()

def showTime():
    display.printByFontColorPosition(120, 223, 10, 200, dt.datetime.now(pytz.timezone('US/Eastern')).strftime('%-I:%M %p'), "        ")

showTime()
    

#../digole/right-display setFont 18
#../digole/right-display setColor 222
#../digole/right-display printxy_abs 120 230 "Andover, MA, USA"

#../digole/right-display setFont 18
#../digole/right-display setColor 255
#../digole/right-display printxy_abs 20 140 "Welcome to Kevin's Car"

#../digole/right-display setColor 255
#../digole/right-display driving 10 10
#../digole/right-display printxy_abs 35 25 "Trip: 1h 24m"

#../digole/right-display setColor 255
#../digole/right-display speed 10 55
#../digole/right-display printxy_abs 35 65 "12mi"

#../digole/right-display setColor 255
#../digole/right-display traffic 10 85
#../digole/right-display printxy_abs 35 95 "13%"

#../digole/right-display setColor 222
#../digole/right-display driving 175 12
#../digole/right-display printxy_abs 200 25 "Last: 2h 13m"

#../digole/right-display setColor 254
#../digole/right-display driving 175 43
#../digole/right-display printxy_abs 200 55 "Idle: 2h 13m"


