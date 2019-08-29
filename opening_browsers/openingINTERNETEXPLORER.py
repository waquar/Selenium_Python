from selenium import  webdriver
import  os
import  time
path = 'D:\\Selenium_Addon_Files\\IEDriverServer.exe'

class Running_IE():
    def openingbrowser(self):
        os.environ['webdriver.ie.driver']= path
        driver = webdriver.Ie(path)
        driver.get('https://www.letskodeit.com')

run = Running_IE()
run.openingbrowser()