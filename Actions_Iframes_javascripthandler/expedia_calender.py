from selenium import  webdriver
from selenium.webdriver.common.by import  By
import os
import time

path= "D:\\Selenium_Addon_Files\\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = path
driver = webdriver.Chrome(path)
driver.set_window_position(1400, 0)                  # used to send current screen to secondary monitor
driver.maximize_window()
driver.get("https://www.expedia.com/")
driver.implicitly_wait(6)

driver.find_element(By.XPATH, "//input[@id='package-departing-hp-package']").click()
week = driver.find_element_by_xpath("//div[@class='datepicker-cal-month'][position()=2]")
print(week)
dates = week.find_elements(By.XPATH, ".//div[@class= 'datepicker-cal-dates']")
print(len(dates))
try:
    for date in dates:
        if date.text == '17':
            date.click()
            time.sleep(3)
            break
        else:
            print("cant find if statement")
except:
    print("cant run try block")
finally:
    driver.close()
