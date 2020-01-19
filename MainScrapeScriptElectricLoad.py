import requests 
import bs4 
import os
#from apscheduler.schedulers 

#0- Ontario, 1-Alberta, 2-Nova Scotia, 3-New Brunswick
data_sources = ['http://ets.aeso.ca/ets_web/ip/Market/Reports/CSDReportServlet',
				'http://reports.ieso.ca/public/GenOutputbyFuelHourly/',
				'https://www.nspower.ca/oasis/monthly-reports/hourly-total-net-nova-scotia-load',
				'https://tso.nbpower.com/Public/en/system_information_archive.aspx']

def scrapeAlberta(source):
	'''
	1-preliminary check to see if hour is correct (also record hour)
	2-Go to AIL value and isolate it
	3- Write it to correct spot in .csv file
	'''
	return 0

def scrapeOntario(source):
	'''
	1-Open correct XML file from source page (do we want past analysis too?)
	2- Isolate correct date and time column from XML
	3- Get value (TOTAL OUTPUT) from last column
	4- Write to .csv file in correct column
	'''
	int value
	 
	return 0

def scrapeNB(source):
	'''
	1- Change webpage to change date to last month then click Get Data 
	2- Navigates to .aspx file
	3. Go to first column to check date then second column for hour 
	4- 3rd column has load value we want. Write this to correct .csv file column 
	'''
	return 0

def scrapeNS(source):
	'''
	1- navigate to source page and open .htm file
	2- First column has date and hour. Split these so we can isolate date and time
	3- 2nd column has load value. Write this to correct .csv file 
	'''
	return 0

def mainRun:
	
	return 0