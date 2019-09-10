from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import os
path= "D:\\Selenium_Addon_Files\\chromedriver.exe"

class Scrollelement():
    def test(self):
        os.environ['webdriver.chrome.driver'] = path
        driver = webdriver.Chrome(path)
        driver.set_window_position(1400, 0)
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.execute_script("window.location = 'https://learn.letskodeit.com/p/practice';")

        driver.execute_script("window.scrollBy(0, 1000);")
        time.sleep(3)
        driver.execute_script("window.scrollBy(0,-850);")
        time.sleep(3)

        element = driver.find_element_by_id('mousehover')
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(3)
        driver.execute_script("window.scrollBy(0,-150);")
        time.sleep(3)


        driver.close()

s = Scrollelement()
s.test()