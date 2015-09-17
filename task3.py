import datetime
import json
import sys
import urllib2

if __name__=='__main__':
    url = 'http://nycopendata.socrata.com/views/%s' % sys.argv[1]
    request = urllib2.urlopen(url)
    metadata = json.load(request) 
    print datetime.datetime.fromtimestamp(metadata['createdAt'])
