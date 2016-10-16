# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *


url = raw_input('Enter - ')
count = int(raw_input("Count: "))
position = int(raw_input("Position: "))

for i in range(count):

    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)

#for i in range(3):
    
    # Retrieve all of the anchor tags
    tags = soup('a')

    list_of_urls = list()
    for tag in tags:
        urls = tag.get('href', None)
        names = tag.contents[0]
        #print 'names: ',names
        #print 'urls: ',urls
        #print 'names: ',names
        #print 'tag:' ,tag
        strings = str(urls)
        list_of_urls.append(strings.split())

    #print 'url on position ',position,":", list_of_urls[position - 1]
    new_url = list_of_urls[position-1]
    print 'Retrieving:', new_url
     
    #print type(new_url)
    string_url = "".join(new_url)
    #print string_url, type(string_url)
    url = string_url
