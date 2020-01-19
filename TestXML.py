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
		sum+=newres.pop()
	finalOutput.append(sum)
finalOutput.reverse()
print(finalOutput)

#add em all up 

'''
from xml.etree import ElementTree
root = ElementTree.parse("Generator Output by Fuel Type Hourly Report.xml").getroot()

for item in root.findall("item"):
    ElementTree.dump(item)
'''