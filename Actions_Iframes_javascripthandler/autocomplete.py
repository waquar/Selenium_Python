from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import os
path= "D:\\Selenium_Addon_Files\\chromedriver.exe"

os.environ['webdriver.chrome.driver'] = path
driver = webdriver.Chrome(path)
#driver.set_window_position(1400,0)
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://www.southwest.com/")

city = driver.find_element_by_id("LandingAirBookingSearchForm_originationAirportCode")
if city is not None:
    print(city)
time.sleep(10)
city.clear()
city.send_keys("NEW")
try:
    xpath = driver.find_element_by_xpath("//ul[@id='LandingAirBookingSearchForm_originationAirportCode--menu']/li[4]/button[@type='button']")
    xpath.click()
except ValueError:
    print("try unexecuted")
time.sleep(3)
driver.close()