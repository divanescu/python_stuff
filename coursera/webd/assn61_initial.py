import urllib
import json


#serviceurl = "http://python-data.dr-chuck.net/comments_42.json" 
serviceurl = raw_input("Enter location: ")
print 'Retrieving', serviceurl
url_handle = urllib.urlopen(serviceurl)
data = url_handle.read()
print 'Retrieved', len(data)
count = list()
count_sum = list()
#print data

js = json.loads(str(data))
#print json.dumps(js, indent=4)

#print 'js comments', js['comments']
for item in js['comments']:
    #print item
    #print "name", item['name']
    #print 'count', item['count']
    count.append(item['count'])
   
#print count
for item in count:
    count_sum.append(int(item))
print 'Count:', len(count_sum)
print 'Sum:', sum(count_sum)
#for item in js:
    #print 'Name', item['comments'][]['name']
#    print 'item:', item
#    print 'item.note', item['note']
