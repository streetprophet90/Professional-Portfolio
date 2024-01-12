


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


---