import urllib2
from bs4 import BeautifulSoup

# scraping can be done using links that have the word "endpoint"

base_url = "https://developer.ciscospark.com"
url = "/endpoint-people-get.html"

link = base_url + url

page = urllib2.urlopen(link) # open the page
soup = BeautifulSoup(page,"html.parser") # parse it using BS

api_table = soup.find_all('table',class_="table api-table white queryparameters")
response_codes_table = soup.find_all('table',class_="table api-table white striped")
temp = api_table[0].find_all('td')

api_spec = [a.text for a in temp]
n = len(api_spec) / 4

frames = [] # list to store batches of 5 parameters
for i in xrange(0,len(api_spec),4):
    frame = api_spec[i:i+4]
    frames.append(frame)
names = ['Name','Type','Description','Required']
params = [dict(zip(names,frame)) for frame in frames] # create a list of dictionaries, where each dictionary contains the extracted parameters

'''for param in params:
    print param, "\n---------------------------"'''

temp = response_codes_table[0].find_all('td')

codes = [c.text for c in temp]
response_codes = dict(zip(codes[::2], codes[1::2])) # create a dictionary with odd values as keys and even values as vals.
# print response_codes, "\n------------------------------"

service_name = soup.find('h1').text
print service_name

service_description = soup.find('p').text
print service_description

resource_url = soup.find('span',class_="api-url-text").text
print resource_url