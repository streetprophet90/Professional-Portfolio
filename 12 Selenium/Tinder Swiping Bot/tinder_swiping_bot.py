import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException


# url of main page.
URL = "https://tinder.com/app/recs"
EMAIL_ID = 'YOUR EMAIL'
PASSWORD = 'YOUR PASSWORD'

# driver path (driver location in folders)
driver_path = Service('DRIVER PATH/chromedriver')
# set driver object to drive browser
driver = webdriver.Chrome(service=driver_path)
driver.maximize_window()


