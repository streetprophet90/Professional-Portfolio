


# Web Scraping with Python

This repository contains Python scripts for web scraping using BeautifulSoup and Selenium. Web scraping is the process of extracting data from websites, and it's essential to be aware of ethical considerations and legal implications. Ensure that you have permission to scrape the website and comply with the website's terms of service.

## Dependencies

Make sure to install the required Python libraries before running the scripts:

```bash
pip install requests beautifulsoup4 selenium
```

- `requests`: For making HTTP requests.
- `beautifulsoup4`: For HTML parsing with BeautifulSoup.
- `selenium`: For automating web browsers.

## ChromeDriver Setup

If you're using Selenium with Chrome, download ChromeDriver:

- [ChromeDriver Downloads](https://sites.google.com/chromium.org/driver/)

Ensure that you download the version compatible with your Chrome browser.

## Usage

### Basic Web Scraping with BeautifulSoup:

1. Edit the `url` variable in the script to the target website.
2. Run the script:

   ```bash
   python beautifulsoup_scraper.py
   ```

### Web Scraping with Selenium:

1. Set up ChromeDriver and specify its path in the script.
2. Edit the `url` variable in the script to the target website.
3. Run the script:

   ```bash
   python selenium_scraper.py
   ```

Adjust the code in the scripts according to the structure of the website you're scraping. Be respectful of the website's resources and policies.

## Legal and Ethical Consider

# Each Line of code

```python
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import csv
```

1. **Import necessary libraries:**
   - `requests`: Used to make HTTP requests.
   - `BeautifulSoup` from `bs4`: Used for web scraping and parsing HTML.
   - `webdriver` from `selenium`: Provides a way to automate web browser interaction.
   - `time`: Provides various time-related functions.
   - `csv`: Used for working with CSV files.


```python
nba_url = "https://www.nba.com/stats/"
```

2. **Define the NBA website URL:**
   - Sets the URL of the NBA stats website.

```python
response = requests.get(nba_url)
nba_page = response.text
soup = BeautifulSoup(nba_page, "xml")
```

3. **Make an HTTP request and create a BeautifulSoup object:**
   - Uses `requests.get` to fetch the content of the NBA website.
   - Converts the response content to text.
   - Creates a BeautifulSoup object (`soup`) to parse the HTML content.

```python
nba = soup.find_all(name="a", class_="Anchor_anchor__cSc3P LeaderBoardPlayerCard_lbpcTableLink__MDNgL")
stats_heading = soup.find_all(name="h2", class_="LeaderBoardCard_lbcTitle___WI9J")
```

4. **Scrape player names and links:**
   - Uses `soup.find_all` to find all `<a>` tags with specified classes representing player links.
   - Also finds all `<h2>` tags with a specific class representing statistics headings.

```python
player_name = []
player_links = []
player_team = []

for nba_tag in nba:
    nba_player = nba_tag.getText()
    player_name.append(nba_player)

    link = nba_tag.get("href")
    player_links.append(link)

player_team = [player_team.getText() for player_team in soup.find_all(name="span", class_="LeaderBoardPlayerCard_lbpcTeamAbbr__fGlx3")]
```

5. **Loop through player tags and extract information:**
   - Iterates through each player tag obtained.
   - Gets the player's name using `getText()` and appends it to the `player_name` list.
   - Retrieves the player's link using `get("href")` and appends it to the `player_links` list.

```python
print(player_name)
print(player_links)
print(player_team)
```

6. **Print the extracted data:**
   - Prints the lists containing player names, links, and team information.

```python
csv_headers = ['Player', 'Url', 'Team', 'Category']
with open('results.csv', 'w', newline='', encoding='utf-8') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(csv_headers)
```
7. **creates the csv file to store scraped data:**