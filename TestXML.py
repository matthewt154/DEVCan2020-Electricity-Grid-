import urllib.request, urllib.error, urllib.parse

url = 'http://reports.ieso.ca/public/GenOutputbyFuelHourly/PUB_GenOutputbyFuelHourly_2020_v17.xml'

response = urllib.request.urlopen(url)
webContent = str(response.read())

f = open('Generator Output by Fuel Type Hourly Report.xml', 'w')
f.write(webContent)
f.close

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Import BeautifulSoup
from bs4 import BeautifulSoup as bs


content = []
# Read the XML file
with open("Generator Output by Fuel Type Hourly Report.xml", "r") as file:
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

#add em all up 
