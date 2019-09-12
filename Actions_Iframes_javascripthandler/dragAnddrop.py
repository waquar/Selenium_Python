from selenium import webdriver
import os, time
path= "D:\\Selenium_Addon_Files\\chromedriver.exe"
from selenium.webdriver.common.by import By
from  selenium.webdriver import  ActionChains                      #used for hovering

class dragDrop():
    def test(self):
        os.environ['webdriver.chrome.driver'] = path
        driver = webdriver.Chrome(path)
        driver.set_window_position(1400, 0)
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get("https://jqueryui.com/droppable/")
        driver.switch_to.frame(0)                                             #using iframe
        drag = driver.find_element_by_id('draggable')
        drop = driver.find_element_by_id('droppable')
        time.sleep(2)
        try:
            action = ActionChains(driver)
            #             # action.drag_and_drop(drag, drop).perform()
            #second method
            action.click_and_hold(drag).move_to_element(drop).release().perform()
            print("successful")
        except:
            print("something wromng in try")

d = dragDrop()
d.test()

