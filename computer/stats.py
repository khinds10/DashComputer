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

        #        latestTripStartID = postgres.getLatestTripStartID()
        #        latestIdleStartID = postgres.getLatestIdleStartID()

        #        idleStatus = Idle.Statistics('idle.data')
        #        if idleStatus.isIdle == 'yes':
        #            if isIdle == True:
        #                latestTripStartID = postgres.getLatestTripStartID()
        #                isIdle = False
        #        else:
        #            if isIdle == False:
        #                latestIdleStartID = postgres.getLatestIdleStartID()
        #                isIdle = True
        #                
        #        stats.data
        #        
        #            averageAltitude
        #                current trip
        #                last idle
        #                last trip
        #                
        #            averageSpeeds
        #                current trip
        #                last idle
        #                last trip
        #                
        #            drivingTimes
        #                current trip
        #                last idle
        #                last trip
        #                
        #            inTrafficTimes
        #                current trip
        #                last idle
        #                last trip
        #                
        #            milesTravelled
        #                current trip
        #                last idle
        #                last trip

	    drivingStatistics = Statistics.Statistics('stats.data')
	    drivingTimes = postgres.getDrivingTimes(thisTripStartID)
	    avgSpeeds = postgres.getAverageSpeeds(thisTripStartID)
	    drivingStatistics.drivingTimes = map(data.convertHumanReadable, drivingTimes)
	    drivingStatistics.inTrafficTimes = map(data.convertHumanReadable, postgres.getInTrafficTimes(thisTripStartID))
	    drivingStatistics.averageSpeeds = map(data.convertToString, map(data.convertToInt, avgSpeeds))
	    drivingStatistics.averageAltitude = map(data.convertToString, map(data.convertToInt, postgres.getAverageAlt(thisTripStartID)))
	    drivingStatistics.milesTravelled = [data.convertToInt(avgSpeeds[0]/60/60 * drivingTimes[0]), data.convertToInt(avgSpeeds[1]/60/60 * drivingTimes[1])]    
	    drivingStatistics.saveData()
	    time.sleep(30)

    except (Exception):
    
        # data issue, wait 5 seconds
	    drivingStatistics.saveData()
	    time.sleep(5)
