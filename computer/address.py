#!/usr/bin/python
# Get complete current location details about known lat/long from Google Maps API
# Kevin Hinds http://www.kevinhinds.com
# License: GPL 2.0
import time, json, string, cgi, subprocess
import includes.data as data
import includes.settings as settings
import info.LocaleDetails as LocaleDetails

# get local locale info every 1 minutes to file to be further processed
while True:
    try: 
        currentLocationInfo = data.getLastKnownLatLong()
        localeURL = 'https://maps.googleapis.com/maps/api/geocode/json?latlng=' + str(currentLocationInfo['latitude']) + ',' + str(currentLocationInfo['longitude']) + '&key=' + settings.googleMapsAPIKey
        localeInfo = json.loads(subprocess.check_output(['curl', localeURL]))
    
        # create serializeable class for use to save locale info to JSON file object
        localeDetails = LocaleDetails.LocaleDetails('address.data')
        localeDetails.address = str(localeInfo['results'][0]['formatted_address'])
        localeDetails.area = str(localeInfo['results'][1]['formatted_address'])
        localeDetails.city = str(localeInfo['results'][2]['formatted_address'])
        localeDetails.zipcode = str(localeInfo['results'][3]['formatted_address'])
        localeDetails.county = str(localeInfo['results'][4]['formatted_address'])
        localeDetails.country = str(localeInfo['results'][5]['formatted_address'])
        localeDetails.saveData()

    except (Exception):
        # GPS or network not available, wait 5 seconds
        time.sleep(5)
    time.sleep(60)
