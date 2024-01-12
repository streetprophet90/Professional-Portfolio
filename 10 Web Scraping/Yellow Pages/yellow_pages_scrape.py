import time
import csv
import requests
from bs4 import BeautifulSoup

def find_jobs():
    html_text = requests.get("https://ghanayellowpages.com/listings/").text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all("div", class_="hp-grid__item hp-col-sm-6 hp-col-xs-12")

    # while True:
    #     next_page = soup.find("a", class_="next page-numbers").get("href")
    #     print(next_page)
    #     new_url = next_page
    #     response = requests.get(new_url)
    #     soup = BeautifulSoup(response.text, "lxml")



    for job in jobs:
        date_added = job.find('time', class_="hp-listing__created-date hp-listing__date hp-meta").text.replace(',', '')
        company_name = job.find('h4', class_='hp-listing__title').text
        category = job.find('div', class_="hp-listing__categories hp-listing__category").text
        more_info = job.header.a['href']




        print(f"Company Name: {company_name.strip()}")
        print(f"Job Category: {category.strip()}")
        print(f"Date: {date_added.strip()[9:]}")
        print(f'More info: {more_info}')
        print('')

if __name__ == "__main__":
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} minutes... ')
        time.sleep(time_wait * 60)



