
# first thing is we have to open chrome manually from cmd by using this:
# chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chrome"

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
#Change chrome driver path accordingly
chrome_driver = "D:\\Selenium_Addon_Files\\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
#driver.get("https://sp.hexaware.com/sites/tne/sitepages/expensehome.aspx")
print(driver.title)











