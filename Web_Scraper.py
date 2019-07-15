"""
Author      :       Souradeep Bhowmik
Date        :       April 2019
Environment :       Windows 10
Version     :       Python 3.6.2
"""


from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import os

options = Options()
options.add_argument("--headless")              # Runs Chrome in headless mode
options.add_argument('--no-sandbox')            # Bypass OS security model
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument("--disable-extensions")
curDir = os.path.dirname(os.path.realpath(__file__)) + "\\" + "chromedriver.exe"
driver = webdriver.Chrome(chrome_options=options, executable_path=curDir)


driver.get('https://www.mother.ly/news/the-most-popular-baby-names-of-2018')    # Connect to first names website
driver.implicitly_wait(10)                      # 10 seconds wait for all elements to be available

##########         First name extractor code snippet         ##########
tableLocator = driver.find_element_by_xpath("/html/body/div[4]/div/div[7]/div[2]/div[2]/div/div[5]/table")             # XPath of the names elemnt on website
firstNames = []          # To append all first names
for rows in tableLocator.find_elements_by_tag_name("tr"):
    columns = rows.find_elements_by_tag_name("td")
    for iterator in range(1,len(columns)):
        firstNames.append(columns[iterator].text)
##########       First name extractor code snippet end       ##########



driver.get('https://www.rong-chang.com/namesdict/100_last_names.htm')    # Connect to last names website
driver.implicitly_wait(10)      # 10 seconds wait for all elements to be available

##########         Last name extractor code snippet         ##########
tableLocator = driver.find_element_by_xpath("/html/body/div[1]/font/center[3]/table/tbody")
lastNames = []          # To append all last names
rows = tableLocator.find_element_by_tag_name("tr")

for columns in rows.find_elements_by_tag_name("td"):
    for names in columns.find_elements_by_tag_name("b"):
        lastNames.append(names.find_element_by_tag_name("a").text)
##########       Last name extractor code snippet end       ##########

driver.close()

##########       File writer code snippet       ##########
files = open("first_names.txt","w+")
for iterator in range(len(firstNames)):
    files.write("%s\n" %firstNames[iterator])
files.close()

files = open("last_names.txt","w+")
for iterator in range(len(lastNames)):
    files.write("%s\n" %lastNames[iterator])
files.close()
##########       File writer code snippet end   ##########
