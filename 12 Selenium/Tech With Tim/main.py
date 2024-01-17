from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()
driver .get("https://www.techwithtim.net/")
driver.maximize_window()
print(driver.title)

# element = driver.find_element(By.TAG_NAME , 'div')
# print(element)
# print(driver.page_source)


link = driver.find_element(By.LINK_TEXT, "Tutorials")
link.click()

# time.sleep(5)


# try:
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.LINK_TEXT, "Programming Tutorials"))
#     )
#     element.click()
# except:
#     driver.quit()
driver.back()
# driver = webdriver.Chrome()
# driver.get('http://www.yahoo.com')
# assert 'Yahoo' in driver.title
#
# elem = driver.find_element(By.NAME, 'p')  # Find the search box
# elem.send_keys('seleniumhq' + Keys.RETURN)
# print(f"Successful: {elem}")
#
# try:
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.LINK_TEXT, "Getting Started · Selenium IDE"))
#     )
# finally:
#     time.sleep(5)
time.sleep(300)






