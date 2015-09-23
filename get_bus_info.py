import csv
import json
import sys
import urllib2

if __name__=='__main__':
	url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (sys.argv[1], sys.argv[2])
	request = urllib2.urlopen(url)
	data = json.load(request)
	activity = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

	with open(sys.argv[3], 'wb') as csvfile:
		writer = csv.writer(csvfile) 
		writer.writerow(['Latitude', 'Longitude', 'Stop Name', 'Stop Status'])

		for b in activity: 
			busLat = b['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
			busLong = b['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
			busStop = b['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
			busStatus = b['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
			
			if bool(busStop) == True and bool(busStatus) == True: 
				row = [busLat, busLong, busStop, busStatus]
				writer.writerow(row)
			else:
				row = [busLat, busLong, 'N/A', 'N/A']
				writer.writerow(row)