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
nba = soup.find_all(name="a", class_="Anchor_anchor__cSc3P LeaderBoardPlayerCard_lbpcTableLink__MDNgL")
stats_heading = soup.find_all(name="h2", class_="LeaderBoardCard_lbcTitle___WI9J")


player_name = []
player_links = []
player_team = []

for nba_tag in nba:
    nba_player = nba_tag.getText()
    player_name.append(nba_player)

    link = nba_tag.get("href")
    player_links.append(link)

team = [player_team.getText() for player_team in soup.find_all(name="span", class_="LeaderBoardPlayerCard_lbpcTeamAbbr__fGlx3")]


print(player_name)
print(player_links)
print(team)







