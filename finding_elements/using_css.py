# used for id   input#username
# .used for class      input.password
#  *used for anywhere
#  ^ used for starting
# $ used for ending


from selenium import webdriver
import time
path = 'D:\\Selenium_Addon_Files\\geckodriver.exe'

driver =  webdriver.Firefox(executable_path=path)
driver.get('https://www.imdb.com')
a=driver.find_element_by_css_selector("img[src*='imdbpro']")
a.click()
time.sleep(3)
driver.close()