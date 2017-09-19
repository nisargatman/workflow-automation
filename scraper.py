import urllib2
from bs4 import BeautifulSoup
import csv

base_url = "https://dev.twitter.com/rest/reference"
url = "/get/lists/subscribers"

link = base_url + url

page = urllib2.urlopen(link)
soup = BeautifulSoup(page,"html.parser")

tables = soup.find_all('table')
resource_information = tables[0]
parameters = tables[1]

td_tags = resource_information.find_all('td')
resource_info_list = []
for tag in td_tags:
    resource_info_list.append(tag.text)
resource_info = dict(zip(resource_info_list[::2], resource_info_list[1::2]))
print resource_info, "\n------------------------------"

td_tags = parameters.find_all('td')
temp_info = []
for tag in td_tags:
    temp_info.append(tag.text)
n = len(temp_info) / 5
params = []
frames = []
for i in xrange(0,len(temp_info),5):
    frame = temp_info[i:i+5]
    frames.append(frame)
names = frames[0]
del frames[0]
for frame in frames:
    params.append(dict(zip(names,frame)))

for param in params:
    print param, "\n---------------------------"

urls = soup.find_all("cite")
for url in urls:
    if url.text.startswith('http'):
        resource_url = url.text

print resource_url
