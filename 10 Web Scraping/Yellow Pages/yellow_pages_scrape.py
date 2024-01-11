import time
import csv
import requests
from bs4 import BeautifulSoup

html_text = requests.get("https://ghanayellowpages.com/listings/").text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all("div", class_="hp-grid__item hp-col-sm-6 hp-col-xs-12")

print(jobs)
