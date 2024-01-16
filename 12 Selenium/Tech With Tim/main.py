from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time


driver = webdriver.Chrome()
driver .get("https://www.techwithtim.net/")
print(driver.title)

time.sleep(300)





