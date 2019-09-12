from selenium import webdriver
import os, time
path= "D:\\Selenium_Addon_Files\\chromedriver.exe"
from selenium.webdriver.common.by import By
from  selenium.webdriver import  ActionChains                      #used for hovering

class hover():
    def test(self):
        os.environ['webdriver.chrome.driver'] = path
        driver = webdriver.Chrome(path)
        driver.set_window_position(1400, 0)
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get("https://learn.letskodeit.com/p/practice")
        hoverbutton = driver.find_element_by_id('mousehover')

        try:
            action = ActionChains(driver)
            action.move_to_element(hoverbutton).perform()
            print("hovered mouse")
            time.sleep(3)
            link1 = driver.find_element(By.XPATH, ".//div[@class = 'mousehover']//a[text()='Reload']")
            if link1.is_displayed():
                print("xpath is correct")
            else:
                print("xpath not found")
            action.move_to_element(link1).click().perform()
            print("clicked item")
        except:
            print("some error")

h = hover()
h.test()