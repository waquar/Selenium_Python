from selenium import  webdriver
from selenium.webdriver.common.by import By
import time
import os
path= "D:\\Selenium_Addon_Files\\chromedriver.exe"

class javascriptsalert():
    def test(self):
        os.environ["webdriver.chrome.driver"] = path
        driver = webdriver.Chrome(path)
        driver.set_window_position(1400, 0)
        driver.maximize_window()
        driver.implicitly_wait(4)
        driver.get("https://learn.letskodeit.com/p/practice")
        driver.find_element_by_id('name').send_keys('waquar')
        driver.find_element_by_id('alertbtn').click()
        alert1 = driver.switch_to.alert
        alert1.accept()
        time.sleep(2)
        driver.find_element_by_id('confirmbtn').click()
        alert2 = driver.switch_to.alert
        alert2.dismiss()
        time.sleep(3)
        driver.close()

j = javascriptsalert()
j.test()




