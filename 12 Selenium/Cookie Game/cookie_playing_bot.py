from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_driver_path = "YOUR CHROME DRIVER PATH"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

