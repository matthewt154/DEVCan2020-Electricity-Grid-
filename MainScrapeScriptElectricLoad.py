import requests 
import bs4 
import os
#from apscheduler.schedulers 

def scrapeAlberta():
	with open("http://ets.aeso.ca/ets_web/ip/Market/Reports/CSDReportServlet") as fp:
		soup = BeautifulSoup(fp)
	id_soup.p.get_attribute_list('td')
	return 0

def scrapeOntario():
	return 0

def scrapeNB():
	return 0

def scrapeNS():
	return 0

def mainRun():
	return 0


with open("http://ets.aeso.ca/ets_web/ip/Market/Reports/CSDReportServlet") as fp:
		soup = BeautifulSoup(fp)
		Alberta_value = id_soup.p.get_attribute_list('td')
		print(Alberta_value)


