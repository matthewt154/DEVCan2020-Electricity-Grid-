import requests 
from bs4 import BeautifulSoup as bs
import bs4 
import os
import lxml.html as lh
#from apscheduler.schedulers 

#0- Ontario, 1-Alberta, 2-Nova Scotia, 3-New Brunswick
data_sources = ['http://ets.aeso.ca/ets_web/ip/Market/Reports/CSDReportServlet',
				'Generator Output by Fuel Type Hourly Report.xml',
				'https://www.nspower.ca/oasis/monthly-reports/hourly-total-net-nova-scotia-load',
				'https://tso.nbpower.com/Public/en/system_information_archive.aspx']

def scrapeAlberta(source):
	'''
	1-preliminary check to see if hour is correct (also record hour)
	2-Go to AIL value and isolate it
	3- Write it to correct spot in .csv file
	'''
	page = requests.get(source)
	tree = lh.fromstring(page.content)
	#get value of elements in td
	td_elements = tree.xpath('//td/text()')
	#storing the value in a list
	l_td = []
	for t in td_elements:
		l_td.append(t)
	#from our list, we get the value of the Alberta Internal Load
	for i in range(len(l_td) - 1):
		if l_td[i] == 'Alberta Internal Load (AIL)':
			alberta_value = l_td[i + 1]
	#Getting the time of last update for our value
	for i in range(len(l_td) - 1):
		if "Last Update" in l_td[i]:
			format_last_update = l_td[i]
	#Storing the data for the date of the last update of this information
	full_date_of_last_update = format_last_update.split()
	last_update_month = full_date_of_last_update[3]
	last_update_date = full_date_of_last_update[4]
	last_update_year = full_date_of_last_update[5]
	last_update_time = full_date_of_last_update[6]
	#Checking to see if there is a comma in the string for the date so that we remove
	if "," in last_update_date:
		last_update_date = last_update_date.replace(","," ")
	print(alberta_value)

	#TO_DO put to excel file 

	return 0

def scrapeOntario(source):
	'''
	1-Download correct XML file from source page (onto machine)
	2- Isolate correct date and time column from XML
	3- Get value (TOTAL OUTPUT) from last column
	4- Write to .csv file in correct column
	'''

	#TO_DO download 

	content = []
	# Read the XML file
	with open(source, "r") as file:
	    # Read each line in the file, readlines() returns a list of lines
	    content = file.readlines()
	    # Combine the lines in the list into a string
	    content = "".join(content)
	    #print(content)
	    bs_content = bs(content, "lxml")
	result =bs_content.find_all("energyvalue")
	#print (result)
	newres = []
	for all in result:
		newres.append(int(all.find("output").get_text()))
	#print(newres)
	finalOutput=[]
	while (newres):
		sum=0
		for i in range(6):
			sum+=newres.pop() #add all 6 columns of energy types for final load 
		finalOutput.append(sum)
	finalOutput.reverse()
	print(finalOutput)

	#TO_DO put to excel file 

	return 0

def scrapeNB(source):
	'''
	1- Change webpage to change date to last month then click Get Data 
	2- Navigates to .aspx file
	3. Go to first column to check date then second column for hour 
	4- 3rd column has load value we want. Write this to correct .csv file column 
	'''

	#TO_DO put to excel file 
	return 0

def scrapeNS(source):
	'''
	1- navigate to source page and open .htm file
	2- First column has date and hour. Split these so we can isolate date and time
	3- 2nd column has load value. Write this to correct .csv file 
	'''

	#TO_DO put to excel file 
	return 0

def mainRun():
	return 0

scrapeAlberta(data_sources[0])
scrapeOntario(data_sources[1])