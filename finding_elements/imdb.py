from selenium import webdriver
import os
import  time
from selenium.webdriver.common.by import  By
path = 'D:\\Selenium_Addon_Files\\chromedriver.exe'

os.environ['webdriver.chrome.driver'] = path
driver = webdriver.Chrome(path)
driver.get('https://www.imdb.com')
a = driver.find_element(By.XPATH, "//img[contains(@src, 'imdbpro')]")
a.click()
time.sleep(3)
driver.close()



