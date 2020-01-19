#new brunswick test 
from selenium import webdriver
#downloading to a .txt file 
url='https://tso.nbpower.com/Public/en/system_information_archive.aspx'
driver=webdriver.Chrome(executable_path='C:/Users/tran/Desktop/DEVCan2020/DEVCan2020-Electricity-Grid-/chromedriver.exe')
driver.get(url) #open up webpage using selenium webdriver
year = driver.find_element_by_xpath('//select[@id="ctl00_cphMainContent_ddlYear"]')
all_years = year.find_element_by_xpath('//option[@value="2019"]')
all_years.click() #click the 2019 option 

get_data=driver.find_element_by_xpath('//a [@id="ctl00_cphMainContent_lbGetData"]')
get_data.click()

unfiltered_data=driver.find_element_by_xpath('//pre').text
driver.close()

#print(unfiltered_data)
filename='NBData.txt' #writing to the text file 
f = open(filename, 'w')
f.write(unfiltered_data)

f.close

f=open(filename, 'r')
lines =f.readlines() #list of all lines of data in txt 
print(lines[2])
s = lines[2]
date = s[:10]
hour = s[11:16]
load = s[17:21]
print (date)
print(hour)
print(load)
f.close



'''
import webbrowser 
webbrowser.open('http://reports.ieso.ca/public/GenOutputbyFuelHourly/PUB_GenOutputbyFuelHourly.xml')

from bs4 import BeautifulSoup
import requests 
import re
source ='http://reports.ieso.ca/public/GenOutputbyFuelHourly/PUB_GenOutputbyFuelHourly.xml'

URL = 'https://en.wikipedia.org/wiki/List_of_game_engines'
content = requests.get(source)
soup = bs4.BeautifulSoup(content.text, 'xml')
row = xml_soup.find('td') # Extract and return first occurrence of tr
print(row)            # Print row with HTML formatting
print("=========Text Result==========")
print(row.get_text()) # Print row as text

source ='http://reports.ieso.ca/public/GenOutputbyFuelHourly/PUB_GenOutputbyFuelHourly.xml'

f=open ('Generator Output by Fuel Type Hourly Report.xml')
soup = BeautifulSoup(f, features='lxml')
update =soup.find_all("hours")
print(update)


#res=requests.get(source).text
#print(res.content)
#soup = BeautifulSoup(source, 'html.parser')
#print (soup.prettify())

for x in range(24):
	print (soup.hour)

for link in soup.find_all("a"):
    print("Inner Text: {}".format(link.text))
    print("Title: {}".format(link.get("title")))
    print("href: {}".format(link.get("href")))


#print (soup.select('body > div.report > table > tbody > tr:nth-child(2) > td:nth-child(1)'))
'''