from selenium import  webdriver
import  os
import  time
path = 'D:\\Selenium_Addon_Files\\chromedriver.exe'

class Running_Chrome():
    def openingbrowser(self):
        os.environ['webdriver.chrome.driver']= path
        driver = webdriver.Chrome(path)
        driver.get('https://www.letskodeit.com')
        time.sleep(5)
        driver.close()

run = Running_Chrome()
run.openingbrowser()


