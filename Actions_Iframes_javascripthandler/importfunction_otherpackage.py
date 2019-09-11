from selenium import  webdriver
from selenium.webdriver.common.by import By
import time
import os
path= "D:\\Selenium_Addon_Files\\chromedriver.exe"
from Actions_Iframes_javascripthandler import  screenshot

class jsalert():
    def setup(self):
        os.environ["webdriver.chrome.driver"] = path
        driver = webdriver.Chrome(path)
        driver.set_window_position(1400, 0)
        driver.maximize_window()
        driver.implicitly_wait(4)
        self.test(driver)

    def test(self, driver):
        driver.get("https://learn.letskodeit.com/p/practice")
        screenshot.Screenshots.takescreenshots(self, driver)         #calling from another package
        print(driver.title)
        parenthandle = driver.current_window_handle
        driver.implicitly_wait(3)
        driver.find_element(By.ID, 'opentab').click()
        handles = driver.window_handles
        for handle in handles:
            if handle not in parenthandle:
                driver.switch_to.window(handle)  # going to new handle
                driver.get("https://www.youtube.com/watch?v=vq8goJQd9WE")
                screenshot.Screenshots.takescreenshots(self, driver)
                print(driver.title)
                if handle not in parenthandle:  # again going back to original handle
                    driver.switch_to.window(parenthandle)
                    print(driver.title)
                    screenshot.Screenshots.takescreenshots(self,driver)
                    time.sleep(4)
                driver.close()

js = jsalert()
js.setup()



