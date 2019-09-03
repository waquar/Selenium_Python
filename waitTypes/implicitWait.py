from selenium import  webdriver
from selenium.webdriver.common.by import  By
import os
path= "D:\\Selenium_Addon_Files\\chromedriver.exe"

os.environ["webdriver.chrome.driver"] = path
driver = webdriver.Chrome(path)
driver.get("https://learn.letskodeit.com/p/practice")
print(driver.title)
parenthandle = driver.current_window_handle
driver.implicitly_wait(3)
driver.find_element(By.ID,'opentab').click()

handles = driver.window_handles
for handle in handles:
    if handle not in parenthandle:
        driver.switch_to.window(handle)
        driver.get("https://www.youtube.com/watch?v=vq8goJQd9WE")
        print(driver.title)
        driver.close()