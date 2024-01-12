


# Tonaton Mobile Phones Scraper

This Python script scrapes information about mobile phones listed on [Tonaton](https://tonaton.com) and stores the data in a CSV file.

## Prerequisites

Make sure you have the following Python libraries installed:

- `csv`
- `time`
- `pandas`
- `requests`
- `BeautifulSoup`

You can install them using:

```bash
pip install pandas requests beautifulsoup4
```

## How to Run

1. Clone the repository or download the Python script.
2. Open a terminal and navigate to the script's directory.
3. Run the script:

    ```bash
    python product.py
    ```


4. The script will scrape information about mobile phones from the specified pages on Tonaton and save the data in a CSV file named `mobiles.csv`.

## Script Overview

- The script uses the `requests` library to make HTTP requests to Tonaton's mobile phones listing pages.
- It utilizes `BeautifulSoup` for HTML parsing to extract information such as phone names, prices, locations, conditions, and links.
- Data is stored in lists and then converted into a Pandas DataFrame.
- The resulting DataFrame is saved to a CSV file named `mobiles.csv`.
- The script automatically iterates through 20 pages (you can adjust this range based on your requirements).




```python
import csv
import time
import pandas as pd
import requests
from bs4 import BeautifulSoup
```

1. **Import necessary libraries:**
   - `csv`: Used for working with CSV files.
   - `time`: Provides various time-related functions.
   - `pandas` (as `pd`): A powerful library for data manipulation and analysis.
   - `requests`: Allows sending HTTP requests to retrieve web pages.
   - `BeautifulSoup` from `bs4`: Used for web scraping and parsing HTML.

```python
Names = []
Prices = []
Location = []
Condition = []
Links = []
```

2. **Initialize lists to store data:**
   - `Names`: To store phone names.
   - `Prices`: To store phone prices.
   - `Location`: To store phone locations.
   - `Condition`: To store phone conditions.
   - `Links`: To store links for more information.

```python
for page in range(1, 21):
```

3. **Loop through pages (1 to 20):**
   - Initiates a loop to iterate through pages 1 to 20 of the Tonaton website.

```python
   home_url = ("https://tonaton.com")
   url = "https://tonaton.com/c_mobile-phones?page="+str(page)
   response = requests.get(url)
   print(response)
```

4. **Fetch data from Tonaton:**
   - Defines the Tonaton base URL and constructs the URL for mobile phones on the specified page.
   - Sends an HTTP request to the Tonaton website and prints the response.

```python
   soup = BeautifulSoup(response.text, "lxml")
   box = soup.find("div", class_="product grid wrap")
```

5. **Parse HTML using BeautifulSoup:**
   - Parses the HTML content of the Tonaton page using BeautifulSoup.
   - Finds the main container (`box`) containing product information.

```python
   names = box.find_all("p", class_="product__description")
   for phone in names:
      phone_name = phone.text
      Names.append(phone_name.strip())
   print(Names)
```

6. **Extract phone names:**
   - Finds all elements with the specified class containing phone names.
   - Iterates through each name, extracts the text, and appends it to the `Names` list.

```python
   prices = box.find_all("span", class_="product__title")
   for phone in prices:
      phone_prices = phone.text
      Prices.append(phone_prices.strip())
   print(Prices)
```

7. **Extract phone prices:**
   - Finds all elements with the specified class containing phone prices.
   - Iterates through each price, extracts the text, and appends it to the `Prices` list.

```python
   location = box.find_all("p", class_="product__location")
   for phone in location:
      phone_location = phone.text
      Location.append(phone_location.strip())
   print(Location)
```

8. **Extract phone locations:**
   - Finds all elements with the specified class containing phone locations.
   - Iterates through each location, extracts the text, and appends it to the `Location` list.

```python
   conditions = box.find_all("div", class_="product__tags flex wrap")
   for phone in conditions:
      phone_conditions = phone.text
      Condition.append(phone_conditions.strip())
   print(Condition)
```

9. **Extract phone conditions:**
   - Finds all elements with the specified class containing phone conditions.
   - Iterates through each condition, extracts the text, and appends it to the `Condition` list.

```python
   links = box.find_all("a", class_="product__item flex")
   for phone in links:
      phone_links = phone.get("href")
      Links.append(home_url + phone_links)
   print(Links)
```

10. **Extract phone links:**
    - Finds all elements with the specified class containing phone links.
    - Iterates through each link, extracts the `href` attribute, appends it to the `Links` list, and adds the base URL.

```python
   print(len(Links))
   print(len(Condition))
   print(len(Location))
   print(len(Prices))
   print(len(Names))
```

11. **Print lengths of data lists:**
    - Prints the lengths of the `Links`, `Condition`, `Location`, `Prices`, and `Names` lists.

```python
df = pd.DataFrame({"Phone Name": Names, "Prices": Prices, "Location": Location, "Phone Condition": Condition, "More Info": Links})
print(df)
df.to_csv("mobiles.csv")
```

12. **Create DataFrame and export to CSV:**
    - Creates a pandas DataFrame from the collected data.
    - Prints the DataFrame.
    - Exports the DataFrame to a CSV file named "mobiles.csv".