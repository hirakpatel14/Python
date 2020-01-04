from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys #need to send keystrokes

driver = webdriver.Chrome()
driver.set_page_load_timeout(60)
#"https://www.sephora.com/product/obsessions-eyeshadow-palette-P425909?icid2=palettes%20and%20value%20sets:p425909:product"
url ="https://myimmitracker.com/en/au/trackers/489-visa-tracker"
driver.get(url)
time.sleep(5)

tableHeader = driver.find_element_by_class_name("ag-header-viewport")
tableEnd = driver.find_element_by_class_name("ag-floating-bottom")
dataTable = driver.find_element_by_id("tracker-table")
# print("First Set:\n",dataTable.text)
# dataTable.send_keys(Keys.PAGE_DOWN)
#can be used for scrolling down
# driver.execute_script('arguments[0].scrollIntoView(true);', tableEnd)
time.sleep(5)
print(dataTable.text)

# row =driver.find_element_by_xpath("//div[@class='ag-cell-no-focus']")

