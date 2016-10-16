# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

global url
url = raw_input('Enter - ')
position = int(raw_input('Position: '))

def retrieve_url(url):
    #url = raw_input('Enter - ')
    #position = int(raw_input("Position: "))
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)

    # Retrieve all of the anchor tags
    tags = soup('a')

    list_of_urls = list()
    for tag in tags:
            urls = tag.get('href', None)
            #print urls
            strings = str(urls)

            list_of_urls.append(strings.split())

    #print 'url on position ',position,":", list_of_urls[position - 1]
    new_url = list_of_urls[position-1]
    print 'Retrieving:', new_url
    url = new_url
    return new_url

for i in range(3):
    retrieve_url(url)
