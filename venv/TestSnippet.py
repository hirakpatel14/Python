from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# browser = webdriver.Chrome()
# browser.get('https://myimmitracker.com/en/au/trackers/489-visa-tracker')
# elem = browser.find_element_by_class_name('ag-body-viewport-wrapper')
# time.sleep(10)
# name = browser.find_element_by_xpath("//div[@class='ag-cell-no-focus ag-cell ag-cell-not-inline-editing ag-cell-value ag-cell-range-selected ag-cell-range-selected-1']")
# print(name)
# elem.send_keys(Keys.END)
# time.sleep(5)
# elem.send_keys(Keys.HOME)

# elem=browser.execute_script("document.querySelector('ag-body-viewport-wrapper')")
# print(elem)
#
# def first_occurance(given_string):
#     count_of_alphabets = {} # dictionary or hash table
#     for char in given_string:
#         if char in count_of_alphabets:
#             count_of_alphabets[char]+=1
#         else:
#             count_of_alphabets[char] = 1
#
#     for elem in count_of_alphabets:
#         if count_of_alphabets[elem] ==1:
#             return elem
#
#     return None
#
#
# print(first_occurance('ABCA'))

candidate50Range = ['601-1200', '715', '451-600', '15917', '401-450', '40533', '441-450', '9135', '431-440', '9829', '421-430', '6556', '411-420', '7018', '401-410', '7995', '351-400', '47004', '391-400', '8239', '381-390', '10035', '371-380', '9710', '361-370', '9733', '351-360', '9287', '301-350', '26779', '0-300', '3687']

#data cleansing
listLen = len(candidate50Range)
cleanDataset =[]
for elem in range(0,listLen,2):
    temp =[]
    temp.extend(str(candidate50Range[elem]).split('-'))
    temp.append(candidate50Range[elem+1])
    #candidate50Range.remove(candidate50Range[elem+1])
    cleanDataset.append(temp)

candidate50Range.clear()
candidate10Range = []
#segregate range 50 and range 10
for elem in cleanDataset:
    if int(elem[1])-int(elem[0])==9:
        candidate10Range.append(elem)
    else:
        candidate50Range.append(elem)

print(candidate10Range)
print(candidate50Range)

