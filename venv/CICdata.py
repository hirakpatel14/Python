from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys #need to send keystrokes
import pyodbc
import re

driver = webdriver.Chrome()
driver.set_page_load_timeout(60)
#Call the website
url ="https://www.canada.ca/en/immigration-refugees-citizenship/services/immigrate-canada/express-entry/submit-profile/rounds-invitations.html"
driver.get(url)
time.sleep(5)

#Find data table
candidatesInPool = driver.find_element_by_class_name("table")
titleOfData = candidatesInPool.find_element_by_tag_name("h3")
print(titleOfData.text)

header = str(titleOfData.text).split(" ")
asOfDate =  re.sub('[^A-Za-z0-9]+', '', header[len(header)-2]) +'-' + header[len(header)-3] +'-' + header[len(header)-1]
print(asOfDate)

# Header of the table
crsScoreRange = candidatesInPool.find_element_by_id("tbl1")
numberOfCandidates = candidatesInPool.find_element_by_id("tbl2")

#Prepare all candidates data -- all values from the table on website is stored in candidate50Range list
bodyElements = candidatesInPool.find_elements_by_tag_name("tbody")
candidate50Range = []
for elem in bodyElements:
    candidate50Range.append(str(elem.text).split())
        # if no seperator is provided then split uses white spaces as a separator
#End

candidate10Range = []

#Prepare data of candidates in range of 10 elements, If any element has more than two values means it has range of 10
# such elements should be deleted from the main list and inserted into separate list
for elem in candidate50Range:
    elemLen = len(str(elem).split("', '"))

    if(elemLen>2):
        for i in range(0,int(elemLen),2):
            temp = []
            temp.append(elem[i])
            temp.append(elem[i+1])
            print(temp)
            candidate10Range.append(temp)

        candidate50Range.remove(elem)
#End

# Insert Data into Database
# def OpenConnection():
#     try:
#         con = pyodbc.connect('Driver={SQL Server};'
#                       'Server=II31-2KQX0X2;'
#                       'Database=LocalDBTest;'
#                       'Trusted_Connection=yes;')
#     except Exception as exp:
#         print(exp)
#     return con
#
# def CloseConnection(con):
#     try:
#         con.close()
#     except Exception as exp:
#         print(exp)
#
# #
# connection = OpenConnection()
# cursor = connection.cursor()
# try:
#     for row in candidate50Range:
#         query = 'insert into all_candidates_tb (points_range,no_of_candidates,as_of_date) values (?,?,?)'
#         cursor.execute(query,[row[0],re.sub('[^A-Za-z0-9]+', '',row[1]),asOfDate])
#
#     for row in candidate10Range:
#         query = 'insert into candidate_segregation_tb (points_range,no_of_candidates,as_of_date) values (?,?,?)'
#         cursor.execute(query, [row[0], re.sub('[^A-Za-z0-9]+', '', row[1]), asOfDate])
#
#         connection.commit()
#
# except Exception as exp:
#     print(exp)
#
# finally:
#     CloseConnection(connection)
# #End