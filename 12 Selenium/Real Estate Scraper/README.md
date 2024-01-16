# Real Estate Scraper

This Python script scrapes real estate data from Zillow and populates a Google Form with the gathered information.

## Overview

The script does the following:

1. Sends a GET request to Zillow's search page for homes in San Francisco, CA.
2. Extracts relevant information such as property links, addresses, and prices using BeautifulSoup.
3. Opens a Google Form using Selenium.
4. Enters the scraped data into the corresponding fields in the form.

## Prerequisites

Ensure you have the necessary libraries installed:

```bash
pip install beautifulsoup4 requests selenium
```

Additionally, download the Chrome WebDriver and specify the path in the script:

```python
# Substitute your own path here 👇
chrome_driver_path = 'YOUR_PATH_HERE'
driver = webdriver.Chrome(executable_path=chrome_driver_path)
```

## Usage

1. Run the script:

   ```bash
   python real_estate_scraper.py
   ```

2. Check the Google Form for the populated data.

## Important Notes

- The script assumes the existence of a Google Form with specific input fields. Adjust the XPath values accordingly:

  ```python
  address = driver.find_element_by_xpath('...your_xpath_here...')
  price = driver.find_element_by_xpath('...your_xpath_here...')
  link = driver.find_element_by_xpath('...your_xpath_here...')
  submit_button = driver.find_element_by_xpath('...your_xpath_here...')
  ```

- Replace `'URL_TO_YOUR_GOOGLE_FORM'` with the URL of your Google Form.

- The header information (`User-Agent` and `Accept-Language`) in the script mimics a standard browser request. Adjust if necessary.

This script is designed for educational purposes and personal use. Be respectful of the website's terms of service.



### Section 1: Import Libraries

```python
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
```
These lines import necessary libraries:
- `BeautifulSoup`: For parsing HTML content.
- `requests`: For sending HTTP requests.
- `webdriver` from `selenium`: For browser automation.
- `time`: For adding delays.

### Section 2: Set Up Headers
```python
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
```
This dictionary defines headers for the HTTP request, including the user agent and language.

### Section 3: Send HTTP Request to Zillow
```python
response = requests.get("https://www.zillow.com/homes/San-Francisco,-CA_rb/?searchQueryState=...", headers=header)
data = response.text
soup = BeautifulSoup(data, "html.parser")
```
These lines send an HTTP GET request to Zillow's page, retrieve the HTML content, and parse it using BeautifulSoup.

### Section 4: Extract Property Links
```python
all_link_elements = soup.select(".list-card-top a")
all_links = []
for link in all_link_elements:
    href = link["href"]
    print(href)
    if "http" not in href:
        all_links.append(f"https://www.zillow.com{href}")
    else:
        all_links.append(href)
```
These lines extract property links from the parsed HTML, format them, and store them in the `all_links` list.

### Section 5: Extract Property Addresses
```python
all_address_elements = soup.select(".list-card-info address")
all_addresses = [address.get_text().split(" | ")[-1] for address in all_address_elements]
```
These lines extract property addresses from the parsed HTML and store them in the `all_addresses` list.

### Section 6: Extract Property Prices
```python
all_price_elements = soup.select(".list-card-heading")
all_prices = []
for element in all_price_elements:
    try:
        price = element.select(".list-card-price")[0].contents[0]
    except IndexError:
        print('Multiple listings for the card')
        price = element.select(".list-card-details li")[0].contents[0]
    finally:
        all_prices.append(price)
```
These lines extract property prices from the parsed HTML. It handles cases where there are multiple listings for a card.

### Section 7: Set Up Selenium WebDriver
```python
chrome_driver_path = YOUR_PATH_HERE
driver = webdriver.Chrome(executable_path=chrome_driver_path)
```
These lines set up the Chrome WebDriver for Selenium. Replace `YOUR_PATH_HERE` with the path to your Chrome WebDriver executable.

### Section 8: Populate Google Form
```python
for n in range(len(all_links)):
    driver.get(URL_TO_YOUR_GOOGLE_FORM)
    time.sleep(2)
    address = driver.find_element_by_xpath('...')
    price = driver.find_element_by_xpath('...')
    link = driver.find_element_by_xpath('...')
    submit_button = driver.find_element_by_xpath('...')

    address.send_keys(all_addresses[n])
    price.send_keys(all_prices[n])
    link.send_keys(all_links[n])
    submit_button.click()
```
These lines loop through the extracted data and use Selenium to populate a Google Form. Replace `URL_TO_YOUR_GOOGLE_FORM` with the URL of your Google Form.

Make sure to replace placeholder values and customize the script according to your needs.