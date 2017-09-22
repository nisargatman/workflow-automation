import urllib2
from bs4 import BeautifulSoup
import csv

base_url = "https://dev.twitter.com/rest/reference"
url = "/get/lists/subscribers"

link = base_url + url

page = urllib2.urlopen(link) # open the page
soup = BeautifulSoup(page,"html.parser") # parse it using BS

tables = soup.find_all('table') # extract the two tables from the page
resource_information = tables[0]
parameters = tables[1] # allocate individual tables to separate variables

td_tags = resource_information.find_all('td') # extract all td tags from the table - all entries in the table
resource_info_list = [tag.text for tag in td_tags] # empty list to store each value
resource_info = dict(zip(resource_info_list[::2], resource_info_list[1::2])) # create a dictionary with odd values as keys and even values as vals.
print resource_info, "\n------------------------------"

td_tags = parameters.find_all('td') # n by 5 table - extract all parameters
temp_info = [tag.text for tag in td_tags]
n = len(temp_info) / 5

frames = [] # list to store batches of 5 parameters
for i in xrange(0,len(temp_info),5):
    frame = temp_info[i:i+5]
    frames.append(frame)
names = frames[0]
del frames[0]
params = [dict(zip(names,frame)) for frame in frames] # create a list of dictionaries, where each dictionary contains the extracted parameters

for param in params:
    print param, "\n---------------------------"

urls = soup.find_all("cite") # extract the resource url
for url in urls:
    if url.text.startswith('http'):
        resource_url = url.text

print resource_url
