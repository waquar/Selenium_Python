from selenium import  webdriver
import os
import time
chrome_path = 'D:\\Selenium_Addon_Files\\chromedriver.exe'
firefox_path = 'D:\\Selenium_Addon_Files\\geckodriver.exe'
ie_path = 'D:\\Selenium_Addon_Files\\IEDriverServer.exe'

import pytest

#it will run each time before any method
@pytest.fixture()
def setUp():
    print("run once first ")
    yield
    print("run once after the caller method ")
    print("This is coming from confest.py")

def setUp_chrome():
    os.environ['webdriver.chrome.driver'] = chrome_path
    driver = webdriver.Chrome(chrome_path)
    driver.get('https://www.letskodeit.com')
    time.sleep(5)
    yield
    driver.close()

def setUp_firefox():
    driver = webdriver.Firefox(executable_path=firefox_path)
    driver.get('https://www.letskodeit.com')
    yield
    driver.close()

def setUp_IE():
    os.environ['webdriver.ie.driver'] = ie_path
    driver = webdriver.Ie(ie_path)
    driver.get('https://www.letskodeit.com')
    yield
    driver.close()