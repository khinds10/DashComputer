#!/usr/bin/python
# Summarize driving statistics to file once per minute
# Kevin Hinds http://www.kevinhinds.com
# License: GPL 2.0
import os, time, json
import includes.data as data
import includes.postgres as postgres
import info.Statistics as Statistics
import info.Idle as Idle

isIdle = False
while True:
    try:
        drivingStatistics = Statistics.Statistics('stats.data')
        recentTripTimes = postgres.getRecentTripTimes()
        recentTripSpeeds = postgres.getRecentTripSpeeds()
        drivingStatistics.drivingTimes = map(data.convertHumanReadable, recentTripTimes)
        drivingStatistics.averageSpeeds = map(data.convertToString, map(data.convertToInt, recentTripSpeeds))
        drivingStatistics.inTrafficTimes = map(data.convertHumanReadable, postgres.getRecentTrafficTimes())
        drivingStatistics.averageAltitude  = map(data.convertToString, map(data.convertToInt, postgres.getRecentTripAltitudes()))
        drivingStatistics.milesTravelled = map(data.convertToString, [data.convertToInt(recentTripSpeeds[0]/60/60 * recentTripTimes[0]), data.convertToInt(recentTripSpeeds[1]/60/60 * recentTripTimes[1]), data.convertToInt(recentTripSpeeds[2]/60/60 * recentTripTimes[2])])	       
        drivingStatistics.saveData()
        time.sleep(30)

    except (Exception):
    
        # data issue, wait 5 seconds
        drivingStatistics.saveData()
        time.sleep(5)
