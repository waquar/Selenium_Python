from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import os
path= "D:\\Selenium_Addon_Files\\chromedriver.exe"
class Javascriptexecution():
    def test(self):
        os.environ['webdriver.chrome.driver'] = path
        driver = webdriver.Chrome(path)
        driver.set_window_position(1400,0)
        driver.maximize_window()
        driver.implicitly_wait(5)
        #driver.get("https://learn.letskodeit.com/p/practice")
        driver.execute_script("window.location = 'https://learn.letskodeit.com/p/practice';")       #used javascript
        element = driver.execute_script("return document.getElementById('name');")                 #used javascript
        element.send_keys('waquar')                                                                                               #used javascript
        time.sleep(3)
j = Javascriptexecution()
j.test()




