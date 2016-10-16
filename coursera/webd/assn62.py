import urllib
import json

serviceurl = 'http://python-data.dr-chuck.net/geojson?'

while True:
    address = raw_input("Enter location: ")
    if len(address) < 1 : break
    if address == 'stop' : break
    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved', len(data), 'characters'

    js = json.loads(str(data))
    try: js = json.loads(str(data))
    except: js = None
    if 'status' not in js or js['status'] != 'OK':
        print 'Failure to retrieve'
        print data
        continue

    print 'Place id', js['results'][0]['place_id']
