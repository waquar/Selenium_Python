from selenium import  webdriver
from selenium.webdriver.common.by import  By
import os
import time
path= "D:\\Selenium_Addon_Files\\chromedriver.exe"

os.environ["webdriver.chrome.driver"] = path
driver = webdriver.Chrome(path)
driver.get("https://www.expedia.com/")
print(driver.title)
driver.implicitly_wait(9)

# a = driver.find_element(By.ID,"package-departing-hp-package")
# a.send_keys("10/10/2019")

a = driver.find_element(By.CLASS_NAME, 'datepicker-cal-dates')

for i in range(3,4):
    xpath = "//div[@class='datepicker-cal-dates']//tr[i]"
    driver.find_element(By.XPATH, xpath).click()
    time.sleep(3)
    driver.close()

