'''
import webbrowser 
webbrowser.open('http://reports.ieso.ca/public/GenOutputbyFuelHourly/PUB_GenOutputbyFuelHourly.xml')
'''
from bs4 import BeautifulSoup
import requests 
import re
source ='http://reports.ieso.ca/public/GenOutputbyFuelHourly/PUB_GenOutputbyFuelHourly.xml'

URL = 'https://en.wikipedia.org/wiki/List_of_game_engines'
content = requests.get(source)
xml_soup = BeautifulSoup(content.text, 'xml')
row = xml_soup.find('td') # Extract and return first occurrence of tr
print(row)            # Print row with HTML formatting
print("=========Text Result==========")
print(row.get_text()) # Print row as text
'''
source ='http://reports.ieso.ca/public/GenOutputbyFuelHourly/PUB_GenOutputbyFuelHourly.xml'

f=open ('Generator Output by Fuel Type Hourly Report.xml')
soup = BeautifulSoup(f, features='lxml')
update =soup.find_all("hours")
print(update)
'''

#res=requests.get(source).text
#print(res.content)
#soup = BeautifulSoup(source, 'html.parser')
#print (soup.prettify())
'''
for x in range(24):
	print (soup.hour)

for link in soup.find_all("a"):
    print("Inner Text: {}".format(link.text))
    print("Title: {}".format(link.get("title")))
    print("href: {}".format(link.get("href")))
'''

#print (soup.select('body > div.report > table > tbody > tr:nth-child(2) > td:nth-child(1)'))