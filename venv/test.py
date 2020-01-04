# Selenium and Webdriver Test
# from selenium import webdriver
#
# driver = webdriver.Chrome()
#
# #Call the website
# url ="https://www.canada.ca/en/immigration-refugees-citizenship/services/immigrate-canada/express-entry/submit-profile/rounds-invitations.html"
# driver.get(url)
#
# #Find data table
# candidatesInPool = driver.find_element_by_class_name("table")
# titleOfData = candidatesInPool.find_element_by_tag_name("h3")
# print(titleOfData.text)


# Database Test
import cx_Oracle # package for oracle connection

dsn_tns = cx_Oracle.makedsn('localhost', '1521', 'oracledb')
con = cx_Oracle.connect(user='system', password='oracledb', dsn=dsn_tns)

# connection = OpenConnection()
cursor = con.cursor()

query = 'select * from all_candidates_info_vw'
data = cursor.execute(query)
for d in data:
    print(str(d))

print(data)
con.close()