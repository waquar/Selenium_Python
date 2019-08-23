from selenium import  webdriver

path = 'D:\\Selenium_Addon_Files\\geckodriver.exe'
driver = webdriver.Firefox(executable_path=path)
driver.get('https://www.letskodeit.com')
driver.close()