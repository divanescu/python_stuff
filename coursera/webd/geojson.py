import urllib
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
#serviceurl = 'http://python-data.dr-chuck.net/json?'

while True:
    address = raw_input("Enter location: ")
    if len(address) < 1 : break

    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved', len(data), 'characters'

    try: js = json.loads(str(data))
    except: js = None
    if 'status' not in js or js['status'] != 'OK':
        print 'Failure to retrieve'
        print data
        continue

    print json.dumps(js, indent=4)

    print 'url', url
    print 'long name',js['results'][0]['address_components'][0]['long_name']
    print 'lat', js['results'][0]['geometry']['location']['lat']
    print 'lng', js['results'][0]['geometry']['location']['lng']
