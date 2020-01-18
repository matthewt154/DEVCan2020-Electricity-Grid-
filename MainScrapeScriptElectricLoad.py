import requests 
import bs4 
import os
#from apscheduler.schedulers 

#0- Ontario, 1-Alberta, 2-Nova Scotia, 3-New Brunswick
data_sources = ['http://ets.aeso.ca/ets_web/ip/Market/Reports/CSDReportServlet',
				'http://reports.ieso.ca/public/GenOutputbyFuelHourly/',
				'https://www.nspower.ca/oasis/monthly-reports/hourly-total-net-nova-scotia-load',
				'https://tso.nbpower.com/Public/en/system_information_archive.aspx']

def extractSource(data_sources, province):
	String link = data_sources[province]
	return 0

def scrapeAlberta(source):
	return 0

def scrapeOntario(source):
	return 0

def scrapeNB(source):
	return 0

def scrapeNS(source):
	return 0

def mainRun:
	
	return 0