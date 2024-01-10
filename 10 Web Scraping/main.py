import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import csv


# chrome_driver_path = "C:\Development\chromedriver.exe"
# driver = webdriver.Chrome(chrome_driver_path)
# driver.get(nba_url)
#
# soup = BeautifulSoup(nba_url, "html.parser")


nba_url = "https://www.nba.com/stats/"
response = requests.get(nba_url)
nba_page = response.text
soup = BeautifulSoup(nba_page, "xml")
print(soup.title)
nba_tag = soup.find(name="a", class_="Anchor_anchor__cSc3P LeaderBoardPlayerCard_lbpcTableLink__MDNgL")
print(nba_tag)

