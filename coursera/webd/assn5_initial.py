import urllib
import xml.etree.ElementTree as ET

#serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'
serviceurl = 'http://python-data.dr-chuck.net/comments_42.xml'

#while True:
    #address = raw_input('Enter location: ')
    #if len(address) < 1 : break

    #url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
#    print 'Retrieving ', url
#    uh = urllib.urlopen(url)
#    data = uh.read()
#    print 'Retrieved ', len(data), 'characters'
#    print data
#    tree = ET.fromstring(data)
#
#    results = tree.findall('result')
#    lat = results[0].find('geometry').find('location').find('lat').text
#    lng = results[0].find('geometry').find('location').find('lng').text
#    location = results[0].find('formatted_address').text
#
#    print 'lat', lat, 'lng', lng
#    print location
uh = urllib.urlopen(serviceurl)
data = uh.read()
counts_list = list()
print 'Data:', data
commentinfo = ET.fromstring(data)
print 'Comment info:', commentinfo
lst = commentinfo.findall('comments/comment')
#print "lst", lst

for item in lst:
    #print 'Name: ', item.find('name').text
    counts = item.find('count').text
    print 'Count: ', counts
    counts_list.append(counts)

print counts_list
int_list = [int(x) for x in counts_list]
print sum(int_list)
