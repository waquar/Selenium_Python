from selenium import webdriver
import os
import time

path = 'D:\\Selenium_Addon_Files\\chromedriver.exe'

class runTest():
    def automate_urls(self, url):
        os.environ['webdriver.chrome.driver'] = path
        driver = webdriver.Chrome(path)
        driver.get(url)
        driver.maximize_window()

        byID = driver.find_element_by_id('header-sign-up-btn')
        time.sleep(8)
        if byID is not  None:
            print('data is there')
        byID.click()
        time.sleep(7)

        byName = driver.find_element_by_class_name('recaptcha-checkbox-border')
        if byName is not  None:
            print('Name data also there')
        byName.click()             #Not clicking here
        time.sleep(3)
        driver.close()

run = runTest()
run.automate_urls('https://learn.letskodeit.com/p/practice')

