from selenium import webdriver
from selenium.webdriver.common.by import  By
import time
import os
path = 'D:\\Selenium_Addon_Files\\IEDriverServer.exe'
a = []
os.environ['webdriver.ie.driver'] = path
driver = webdriver.Ie(path)
driver.get('someurl')
time.sleep(4)
handlealert = driver.switch_to.alert
time.sleep(2)
handlealert.send_keys('zzzz')
handlealert.accept()

b= driver.find_elements(By.XPATH, "//div[@class='hdrcell'][3]")
b.__getitem__(a)
print(a)


