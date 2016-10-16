import urllib
import xml.etree.ElementTree as ET

serviceurl = raw_input('Enter location: ')
print 'Retrieving ', serviceurl
counter = 0
uh = urllib.urlopen(serviceurl)
data = uh.read()
print 'Retrieved ', len(data), 'characters'
counts_list = list()
commentinfo = ET.fromstring(data)
lst = commentinfo.findall('comments/comment')

for item in lst:
    counts = item.find('count').text
    counts_list.append(counts)
    counter += 1
print 'Count: ', counter
int_list = [int(x) for x in counts_list]
print 'Sum: ', sum(int_list)
