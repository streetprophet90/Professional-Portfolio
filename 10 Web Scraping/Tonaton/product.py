import csv
import time
import pandas as pd
import requests
from bs4 import BeautifulSoup

Names = []
Prices = []
Location = []
Condition =[]


url = ("https://tonaton.com/c_mobile-phones")
response = requests.get(url)
print(response)
soup = BeautifulSoup(response.text, "lxml")
# print(soup)

names = soup.find_all("p", class_="product__description")
# print(names)
for phone in names:
   phone_name = phone.text
   Names.append(phone_name.strip())
print(Names)

prices = soup.find_all("span", class_="product__title")
# print(prices)
for phone in prices:
   phone_prices = phone.text
   Prices.append(phone_prices.strip())
print(Prices)

location = soup.find_all("p", class_="product__location")

for phone in location:
   phone_location = phone.text
   Location.append(phone_location.strip())

print(Location)


