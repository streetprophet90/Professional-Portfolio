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
nba_tag = soup.find(name="a", class_="Anchor_anchor__cSc3P LeaderBoardPlayerCard_lbpcTableLink__MDNgL")
stats_heading = soup.find(name="h2", class_="LeaderBoardCard_lbcTitle___WI9J")
nba_player = nba_tag.getText()
stats_text = stats_heading.getText()
player_link = nba_tag.get("href")
player_team = soup.find(name="span", class_="LeaderBoardPlayerCard_lbpcTeamAbbr__fGlx3").getText()
print(nba_player)
print(stats_text)
print(player_link)
print(player_team)






