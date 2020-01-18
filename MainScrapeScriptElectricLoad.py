from bs4 import BeautifulSoup
import requests
import os
#from apscheduler.schedulers 
import lxml.html as lh

page = requests.get("http://reports.ieso.ca/public/GenOutputbyFuelHourly/")
tree = lh.fromstring(page.content)

td_elements = tree.xpath('//td/text()')
l_td = []
for t in td_elements: 
        l_td.append(t)



for i in range(len(l_td) - 1):
        if l_td[i] == 'Alberta Internal Load (AIL)':
                alberta_value = l_td[i + 1]
       
print(alberta_value)

#print("Checking for where last update is:")
#print(l_td)

print("See if this gives last update value")
for i in range(len(l_td) - 1):
        if "Last Update" in l_td[i]:
                format_last_update = l_td[i]
                
full_date_of_last_update = format_last_update.split()
last_update_month = full_date_of_last_update[3]
last_update_date = full_date_of_last_update[4]
last_update_year = full_date_of_last_update[5]
last_update_time = full_date_of_last_update[6]

if "," in last_update_date:
        last_update_date = last_update_date.replace(","," ")

#print(full_date_of_last_update)

print(last_update_month,last_update_date,last_update_year,last_update_time)
