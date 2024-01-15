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

