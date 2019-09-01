

from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
#Change chrome driver path accordingly
chrome_driver = "D:\\Selenium_Addon_Files\\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
#driver.get("https://sp.hexaware.com/sites/tne/sitepages/expensehome.aspx")
print(driver.title)

a = ['7850' , '5000']

for i in range(2, 32):
    xpath = "//table[@class='obj row20px']//tr[" + str(i) + "]//td[3]"
   # time.sleep(1)
    amountElem = driver.find_element_by_xpath(xpath)
    print(amountElem.text)
    a.append(amountElem.text)

total = list(map(int, a))
a = (sum(total))
b = a/12
print(f"total money taken in ECS is {a}")
print(f"monthly is {b}")
print(f"total taken in shiftallowance is {250*308}")
