import urllib2
from bs4 import BeautifulSoup
import csv

base_url = "https://dev.twitter.com/rest/reference"
url = "/get/trends/place"

link = base_url + url

page = urllib2.urlopen(link)
soup = BeautifulSoup(page,"html.parser")

print soup
