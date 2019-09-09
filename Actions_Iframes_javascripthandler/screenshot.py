from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import os
path= "D:\\Selenium_Addon_Files\\chromedriver.exe"

os.environ['webdriver.chrome.driver'] = path
driver = webdriver.Chrome(path)
driver.set_window_position(1400,0)
driver.maximize_window()
driver.implicitly_wait(4)

driver.get("https://learn.letskodeit.com/")
driver.find_element_by_link_text('Login').click()
username= driver.find_element_by_id("user_email")
password = driver.find_element_by_id("user_password")
login = driver.find_element_by_name('commit')
username.send_keys('waq@gmail.com')
password.send_keys('123ear')
login.click()
filelocation = "D:\\Export_path\\1.png"

try:
    if not os.path.isfile(filelocation):                      #checking if already same name file is there
        driver.save_screenshot(filelocation)
        print(f"file saved at this location:-- {filelocation}")
        os.startfile(filelocation)                                         #used this to open the screenshot
    else:
        print("same name file is already present")
except NotADirectoryError:
    print("not location issue")
finally:
    driver.close()
