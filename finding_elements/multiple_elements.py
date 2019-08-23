from selenium import  webdriver
import os
from selenium.webdriver.common.by import By
import time
path = 'D:\\Selenium_Addon_Files\\chromedriver.exe'
a =[]

os.environ['webdriver.chrome.driver'] = path
driver = webdriver.Chrome(path)
driver.get('https://learn.letskodeit.com/p/practice')
driver.maximize_window()
target_link = driver.find_elements(By.TAG_NAME, 'td')
for item in target_link:
    a.append(item.text)
time.sleep(4)
filewriting = open('elements.txt', 'ab')
for items in a:
    filewriting.write(items)
    filewriting.close()
driver.close()
