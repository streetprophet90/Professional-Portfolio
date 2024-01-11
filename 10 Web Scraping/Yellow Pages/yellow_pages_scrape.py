import time
import csv
import requests
from bs4 import BeautifulSoup

html_text = requests.get("https://ghanayellowpages.com/listings/").text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all("div", class_="hp-grid__item hp-col-sm-6 hp-col-xs-12")

for job in jobs:
    company_name = job.find('h4', class_='hp-listing__title').text
    category = job.find('div', class_="hp-listing__categories hp-listing__category").text
    date_added = job.find('time', class_="hp-listing__created-date hp-listing__date hp-meta").text.replace(',','')

    print(f"Company Name: {company_name.strip()}")
    print(f"Job Category: {category.strip()}")
    print(f"Date: {date_added.strip()}")
    print('')


