import requests
import csv
from bs4 import BeautifulSoup

html_text = requests.get('https://www.nba.com/stats').text
soup = BeautifulSoup(html_text, 'lxml')
players = soup.find_all('div', class_='LeaderBoardCard_lbcWrapper__e4bCZ LeaderBoardWithButtons_lbwbCardGrid__'
                                      'Iqg6m LeaderBoardCard_leaderBoardCategory__vWRuZ')

for player in players:
    category = player.find('h2', "LeaderBoardCard_lbcTitle___WI9J").text
    player_name = player.find('a', 'Anchor_anchor__cSc3P LeaderBoardPlayerCard_lbpcTableLink__MDNgL').text
    player_points = player.find('td', 'LeaderBoardWithButtons_lbwbCardValue__5LctQ').text
    player_team = player.find('span', 'LeaderBoardPlayerCard_lbpcTeamAbbr__fGlx3').text


    print(f'Category: {category} '
          f'Player: {player_name} '
          f'Points: {player_points} '
          f'Team: {player_team}')


