# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *


url = raw_input('Enter - ')
count = int(raw_input("Count: "))
position = int(raw_input("Position: "))

for i in range(count+1):

    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)

    # Retrieve all of the anchor tags
    tags = soup('a')

    list_of_urls = list()
    for tag in tags:
        urls = tag.get('href', None)
        names = tag.contents[0]
        strings = str(urls)
        list_of_urls.append(strings.split())

    new_url = list_of_urls[position-1]
    print 'Retrieving:', url
     
    string_url = "".join(new_url)
    url = string_url
