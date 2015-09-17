import csv
import json
import sys

if __name__=='__main__':
    jsonFile = open(sys.argv[1], 'r')
    data = json.load(jsonFile)
    stations = data['stationBeanList']
    
    for s in stations:
        if s['statusKey'] != 1 and s['stationName'].startswith('Coming soon'):
            stationName = s['stationName'][13:]
            stationLat = s['latitude']
            stationLon = s['longitude']
            print '%s : %s,%s' % (stationName, stationLat, stationLon)
