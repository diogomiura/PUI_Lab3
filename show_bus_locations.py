import json
import sys
import urllib2

if __name__=='__main__':
	url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (sys.argv[1], sys.argv[2])
	request = urllib2.urlopen(url)
	data = json.load(request)
	activity = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
	index = 0
		
	print 'Bus Line : %s' % sys.argv[2]
	print 'Number of Active Buses: %d' % len(activity)

	for b in activity: 
		index += 1 
		busLat = b['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
		busLong = b['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
		print 'Bus %s is at latitude %s and longitude %s' % (index, busLat, busLong)