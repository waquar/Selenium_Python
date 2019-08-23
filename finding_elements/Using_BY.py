
from selenium import  webdriver
import os
from selenium.webdriver.common.by import By
import time
path = 'D:\\Selenium_Addon_Files\\chromedriver.exe'

os.environ['webdriver.chrome.driver'] = path
driver = webdriver.Chrome(path)
driver.get('https://learn.letskodeit.com/p/practice')
target_link = driver.find_element(By.ID, 'header-sign-up-btn')
target_link.click()
time.sleep(4)
driver.close()