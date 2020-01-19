from bs4 import BeautifulSoup #html parsing package
import re #regular expressions
#import pandas as pd #pandas, useful for reading/writing tables and 

f=open('CSDReportServlet.html') #best practice to locally save html page while you're messing around,
                               #rather than repeatedly re-download the same webpage
                               
soup=BeautifulSoup(f, features='lxml')


#we should record when the table was last updated, which is on the page with
# the text "Last Update:"

updated=soupf.ind(string=re.compile("Last Update")) #re.compile lets us search using just part of the string
print(updated)
#keep only the date and time
updated=updated.split(':')[1].strip()
print(updated)

#We want to copy the data tables. All of the tables are in tbody tags

def get_table(table):
    table_content=[]
    #rows are tagged tr, columns td
    ROWS=table.find_all("tr")
    for row in ROWS:
        row_content=[]
        COLUMNS=row.find_all("td")
        for column in COLUMNS:
            row_content.append(column.get_text())
        table_content.append(row_content)
    return table_content


#The whole structure of the webpage is tables- all tables are within 'tbody' tags, but the whole page itself is
# also in those tags - the tables are nested together!

#Therefore, instead of naively grabbing ALL tbody tags, we're going to to to the table we want, then find its 
#particular tbody tag to extract only that table.


summary=soup.find("b",string=re.compile("SUMMARY")).find_parent("tbody")
print(summary)


summary_table=get_table(summary)

print(summary_table)

#The first thing we get is an empty row - we can drop it
del summary_table[0]
print(summary_table)
'''
#Convert the list of lists to a dataframe and write to csv:

df=pd.DataFrame(columns=['Summary','Energy'])
for sublist in summary_table:
    print(sublist)
    df=df.append({'Summary':sublist[0],'Energy':sublist[1]}, ignore_index=True)
    
df.to_csv('AESO_Summary_'+updated+'.csv',index=False,encoding='cp1252')
'''