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


# make driver to go to preferred url
driver.get(URL)
time.sleep(5)
# save main window id, will tell you later on about its usage.
main_window = driver.current_window_handle

# click accept to terms on first page of tinder.
allow_cookies = driver.find_element(By.XPATH, '//*[@id="c-1420294622"]/div/div[2]/div/div/div[1]/button').click()
# click on log in button
click_log_in = driver.find_element(By.LINK_TEXT, 'Log in').click()
time.sleep(3)
try:
    # sometimes it shows facebook log in only after clicking on more options, that's why i used exception handling.
    click_more_options = driver.find_element(By.XPATH, '//*[@id="c1146291598"]/div/div/div[1]/div/div[3]/'
                                                       'span/button').click()
except NoSuchElementException:
    pass
time.sleep(5)
try:
    # normally click on log in with facebook
    log_in_facebook = driver.find_element(By.XPATH, '//*[@id="c1146291598"]/div/div/div[1]/div/div[3]/span/div'
                                                    '[2]/button/span[2]').click()

except NoSuchElementException:
    # sometimes before clicking on log in with facebook, it shows account recovery pop up. so we need to tackle that.
    recovery_cancel = driver.find_element(By.XPATH, '//*[@id="c1146291598"]/div/div/div[2]/button').click()
    time.sleep(2)
    # again click on log in
    click_log_in = driver.find_element(By.LINK_TEXT, 'Log in').click()
    time.sleep(2)
    log_in_facebook = driver.find_element(By.XPATH, '//*[@id="c1146291598"]/div/div/div[1]/div/div[3]/span/div'
                                                    '[2]/button/span[2]').click()

time.sleep(5)
# when we click on Facebook log in, our browser automatically opens new tab, but our driver is still on first tab
# so if we want to perform any operation in new window  it will give us error, so we need to change driver from
# main window to current window.
