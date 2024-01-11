

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

Feel free to customize the README.md further based on additional details or specific instructions you'd like to include.