

# Job Scraper

This Python script scrapes job listings from the [Ghana Yellow Pages](https://ghanayellowpages.com/listings/) website. It retrieves information such as the company name, job category, date added, and a link for more information.

## Requirements

- Python 3.x
- `requests` library
- `BeautifulSoup` library

## Usage

1. Install the required libraries using the following command:
   ```bash
   pip install requests beautifulsoup4
   ```

2. Run the script:
   ```bash
   python yellow_pages_scrape.py
   ```

## Script Functionality

- The script sends an HTTP request to the Ghana Yellow Pages job listings page.
- It uses BeautifulSoup for HTML parsing and retrieves job information from the specified HTML elements.
- The script then prints details such as company name, job category, date added, and a link for more information.
- The `while True` loop continuously fetches and prints job information.

## Note

- The script is currently set to run indefinitely with a 10-minute interval between each run. You can adjust the `time_wait` variable to modify the waiting time.

---


```python
import time
import csv
import requests
from bs4 import BeautifulSoup
```

1. **Import necessary libraries:**
   - `time`: Provides various time-related functions.
   - `csv`: Used for working with CSV files.
   - `requests`: Allows sending HTTP requests to retrieve web pages.
   - `BeautifulSoup` from `bs4`: Used for web scraping and parsing HTML.

```python
def find_jobs():
    html_text = requests.get("https://ghanayellowpages.com/listings/").text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all("div", class_="hp-grid__item hp-col-sm-6 hp-col-xs-12")
```

2. **Define a function to find jobs:**
   - Sends an HTTP request to the specified URL and retrieves the HTML content.
   - Parses the HTML using BeautifulSoup.
   - Finds all job listings using the specified class.


```python
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
```

3. **Loop through job listings and print information:**
   - Iterates through each job listing.
   - Extracts specific information such as company name, job category, date added, and more info.
   - Prints the extracted information to the console.

```python
if __name__ == "__main__":
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} minutes... ')
        time.sleep(time_wait * 60)
```

