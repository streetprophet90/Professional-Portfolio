import time
import requests
import csv
from bs4 import BeautifulSoup

html_text = ("https://jiji.com.gh/new-builds")
response = requests.get(html_text)
print(response)

House = []
Prices = []
Desc = []
# Location = []

soup = BeautifulSoup(response.text, "lxml")
names = soup.find_all("div", "b-list-advert-base__data")

for name in names:
    house = name.find("div", class_="b-advert-title-inner qa-advert-title b-advert-title-inner--div").text.strip()
    House.append(house)

    prices = name.find("div", class_="qa-advert-price").text.strip()
    Prices.append(prices)

    # location = name.find(name='span', class_="b-list-advert__region__text")
    # Location.append(location)

    description = name.find("div", class_="b-list-advert-base__description-text").text.strip()
    Desc.append(description)

print(House)
print(Prices)
# print(Location)
print(Desc)




