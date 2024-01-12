import csv
import time
import pandas as pd
import requests
from bs4 import BeautifulSoup

Names = []
Prices = []
Location = []
Condition = []
Links = []

for page in range(1, 21):
   home_url = ("https://tonaton.com")
   # url = ("https://tonaton.com/c_mobile-phones")
   url = "https://tonaton.com/c_mobile-phones?page="+str(page)
   response = requests.get(url)
   print(response)

   soup = BeautifulSoup(response.text, "lxml")
   # print(soup)
   box = soup.find("div", class_="product grid wrap")


   names = box.find_all("p", class_="product__description")
   # print(names)
   for phone in names:
      phone_name = phone.text
      Names.append(phone_name.strip())
   print(Names)

   prices = box.find_all("span", class_="product__title")
   # print(prices)
   for phone in prices:
      phone_prices = phone.text
      Prices.append(phone_prices.strip())
   print(Prices)

   location = box.find_all("p", class_="product__location")

   for phone in location:
      phone_location = phone.text
      Location.append(phone_location.strip())

   print(Location)

   conditions = box.find_all("div", class_="product__tags flex wrap")

   for phone in conditions:
      phone_conditions = phone.text
      Condition.append(phone_conditions.strip())

   print(Condition)


   links = box.find_all("a", class_="product__item flex")
   for phone in links:
      phone_links = phone.get("href")
      Links.append(home_url + phone_links)

   print(Links)

   print(len(Links))
   print(len(Condition))
   print(len(Location))
   print(len(Prices))
   print(len(Names))

df = pd.DataFrame({"Phone Name": Names, "Prices": Prices, "Location": Location, "Phone Condition": Condition, "More Info": Links})
print(df)
df.to_csv("mobiles.csv")
