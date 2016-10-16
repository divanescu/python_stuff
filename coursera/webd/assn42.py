# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program
import re
import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
all_tags = list()
all_links = list()
count = int(raw_input("Enter count: "))
position = int(raw_input("Enter position: "))
# Retrieve all of the anchor tags
tags = soup('a')
#print tags
for tag in tags:
    #print tag.get('href', None)
    #print tag
    all_tags.append(tag)
    all_links = (tag.get('href', None))
    
    print str(all_links)#.splitlines()
    print type(all_links)
    for string in tag:    
        print string
        new_link = re.findall('href="(.+)"', str(tag))
        all_tags.append(str(tag.get('href', None)))

#print "Tag[position]: ", all_tags
print str(new_link)
print "Retrieving: ", url
print "Retrieving: ", all_tags[position]
