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