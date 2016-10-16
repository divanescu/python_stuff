# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *
import re

url = raw_input("Enter url: ")
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

#Get all of the anchor tags

tags = soup('span')
numbers = list()
tag_count = 0
total = 0

for tag in tags:
    tag_count += 1
    #Look at the parts of a tag
    #print 'TAG:', tag
    #print 'URL:', tag.get('href', None)
    numbers_in_tag = re.findall('[0-9]+', str(tag))
    #print numbers_in_tag
    numbers.append(numbers_in_tag)

#print numbers
print tag_count

real_numbers = list()
for item in numbers:
    #print item[0]
    total = total + int(item[0])
    real_numbers.append(item[0])
#print real_numbers
print total
