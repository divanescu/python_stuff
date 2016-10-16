import urllib
import json


serviceurl = raw_input("Enter location: ")
print 'Retrieving', serviceurl
url_handle = urllib.urlopen(serviceurl)
data = url_handle.read()
print 'Retrieved', len(data)
count = list()
count_sum = list()

js = json.loads(str(data))

for item in js['comments']:
    count.append(item['count'])
   
for item in count:
    count_sum.append(int(item))
print 'Count:', len(count_sum)
print 'Sum:', sum(count_sum)
