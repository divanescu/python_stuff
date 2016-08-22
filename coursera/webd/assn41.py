import urllib
import re
from BeautifulSoup import *

url = raw_input("Enter URL: ")
html = urllib.urlopen(url).read()
#now we have the full document 
soup = BeautifulSoup(html)
#get all the tab tags
tags = soup('span')
tag_count = 0
total = 0

numbers = list()
for tag in tags:
        #print tag
        tag_count += 1
        number_in_tag = re.findall('[0-9]+', str(tag))
        numbers.append(number_in_tag)
#        print number_in_tag


#print "Numbers: ", numbers

for item in numbers:
    for string in item:
        total = total + int(string)
print "Count:", tag_count
print "Total: ", total
