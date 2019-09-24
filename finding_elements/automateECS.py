from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = "D:\\Selenium_Addon_Files\\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
print(driver.title)

a = ['7850' , '5000']
totalvouchers =0

for i in range(2, 34):
    xpath = "//table[@class='obj row20px']//tr[" + str(i) + "]//td[3]"
    amountElem = driver.find_element_by_xpath(xpath)
    print(amountElem.text)
    a.append(amountElem.text)
    totalvouchers+=1

total = list(map(int, a))
a = (sum(total))

print(f"total money taken from ECS is :- {a}")
print(f"total vouchers claimed are: - {totalvouchers}")





