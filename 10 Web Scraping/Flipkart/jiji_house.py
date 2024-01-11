import time
import requests
import csv
from bs4 import BeautifulSoup

# html_text = ("https://www.flipkart.com/search?q=phones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
# response = requests.get(html_text)
# print(response)
#
# Names = []
# Prices = []
# Desc = []
# Reviews = []
#
# soup = BeautifulSoup(response.text, "lxml")
# names = soup.find_all("div", "_4rR01T")
#
# for name in names:
#     phone_name = name.text
#     Names.append(phone_name)
# print(Names)

html_text = ("https://jiji.com.gh/new-builds")
response = requests.get(html_text)
print(response)

House = []
Prices = []
Desc = []
Location = []

soup = BeautifulSoup(response.text, "lxml")
names = soup.find_all("div", "b-list-advert-base__data")

for name in names:
    house = name.find("div", class_="b-advert-title-inner qa-advert-title b-advert-title-inner--div").text
    House.append(house)

    prices = name.find("div", class_="qa-advert-price").text
    Prices.append(prices)

    location = name.find('span', class_="b-list-advert__region__text")
    Location.append(location)

    description = name.find("div", class_="b-list-advert-base__description-text").text
    Desc.append(description)

print(House)
print(Prices)
print(Location)
print(Desc)





