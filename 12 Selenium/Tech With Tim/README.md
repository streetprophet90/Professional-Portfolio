# Cookie Clicker Automation

This Python script automates the Cookie Clicker game using Selenium WebDriver.

## Requirements

- Python
- Selenium
- Chrome WebDriver

## Installation

1. Install Python: [Python Official Website](https://www.python.org/downloads/)
2. Install Selenium: `pip install selenium`
3. Download Chrome WebDriver: [ChromeDriver Downloads](https://sites.google.com/chromium.org/driver/)

## Usage

1. Clone the repository:


2. Run the script:

```bash
python cookie_game.py
```

## Description

- The script opens the [Cookie Clicker](https://orteil.dashnet.org/cookieclicker/) game in a Chrome browser.
- It selects the English language.
- It automates the clicking of the big cookie and purchases available upgrades.
- The script runs for a specific duration (300 seconds or 5 minutes).

## Configuration

- The script is currently configured for a 5-minute run. Adjust the duration as needed.
- Ensure you have the correct path to your Chrome WebDriver executable in the script.

## Notes

- This script serves as a simple automation example and may need adjustments based on the game's updates.




```python
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
```

