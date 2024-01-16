from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
# driver .get("https://www.techwithtim.net/")
# print(driver.title)
#
# element = driver.find_element(By.TAG_NAME , 'div')
# print(element)
# print(driver.page_source)

driver.get('http://www.yahoo.com')
assert 'Yahoo' in driver.title

elem = driver.find_element(By.NAME, 'p')  # Find the search box
elem.send_keys('seleniumhq' + Keys.RETURN)




time.sleep(300)





