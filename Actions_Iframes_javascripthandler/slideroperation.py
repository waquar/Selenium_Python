from selenium import webdriver
import os, time
path= "D:\\Selenium_Addon_Files\\chromedriver.exe"
from selenium.webdriver.common.by import By
from  selenium.webdriver import  ActionChains                      #used for hovering

class slider():
    def test(self):
        os.environ['webdriver.chrome.driver'] = path
        driver = webdriver.Chrome(path)
        driver.set_window_position(1400, 0)
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get("https://jqueryui.com/slider/")
        driver.switch_to.frame(0)                                             #using iframe
        slide = driver.find_element(By.XPATH,".//div[@id='slider']//span")
        time.sleep(3)
        try:
            action = ActionChains(driver)
            action.drag_and_drop_by_offset(slide, 350, 0).perform()
            print("successful")
        except:
            print("try problem")
s = slider()
s.test()


