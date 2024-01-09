import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import csv

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://www.nba.com/stats/")