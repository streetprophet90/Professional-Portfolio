import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import csv

nba_url= "https://www.nba.com/stats/"
chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.get(nba_url)

soup = BeautifulSoup(nba_url, "html.parser")