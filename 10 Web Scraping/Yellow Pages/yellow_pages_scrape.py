import time
import csv
import requests
from bs4 import BeautifulSoup

html_text = requests.get("https://ghanayellowpages.com/listings/").text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all("div", "hp-listings hp-block hp-grid")

print(jobs)
