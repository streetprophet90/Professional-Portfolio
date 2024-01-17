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

1. **Import necessary libraries:**
   - `webdriver`: Provides a way to automate web browser interactions (Selenium).
   - `ActionChains`: Allows for performing complex input actions (e.g., mouse movements, clicks).
   - `By`: Defines the mechanisms used to locate elements within a document (Selenium).
   - `time`: Provides functions to add delays in the script.

```python
driver = webdriver.Chrome()
driver.get("https://orteil.dashnet.org/cookieclicker/")
driver.maximize_window()
print(driver)
```

2. **Initialize Chrome WebDriver and open Cookie Clicker:**
   - `webdriver.Chrome()`: Initializes a new instance of the Chrome WebDriver.
   - `driver.get("https://orteil.dashnet.org/cookieclicker/")`: Opens the Cookie Clicker game.
   - `driver.maximize_window()`: Maximizes the browser window for better visibility.
   - `print(driver)`: Outputs information about the WebDriver to the console.

```python
driver.implicitly_wait(5)
```

3. **Implicitly wait for elements to load:**
   - `driver.implicitly_wait(5)`: Sets an implicit wait time of 5 seconds, allowing elements to load before interacting with them.

```python
language = driver.find_element(By.ID, "langSelect-EN")
language.click()
cookie = driver.find_element(By.ID, "bigCookie")
cookie_count = driver.find_element(By.ID, "cookies")
items = [driver.find_element(By.ID, "productPrice" + str(i)) for i in range(1, -1, -1)]
```

4. **Locate elements on the page:**
   - `driver.find_element`: Finds individual elements using the specified method (`By.ID`) and value.
   - `items`: Retrieves a list of upgrade elements using a list comprehension.

```python
actions = ActionChains(driver)
actions.click(cookie)
```

5. **Create ActionChains for clicking the big cookie:**
   - `ActionChains(driver)`: Initializes a series of user actions.
   - `actions.click(cookie)`: Adds a click action on the big cookie element to the series.

```python
for i in range(5000):
    actions.click(cookie).perform()
    time.sleep(0.01)
    count = int(cookie_count.text.split(" ")[0])
```

6. **Automate cookie clicking and count cookies:**
   - Enters a loop that clicks the big cookie using the defined ActionChains.
   - Pauses for a short time (0.01 seconds) to simulate a human-like interaction.
   - Retrieves the current cookie count.

```python
for item in items:
    value = int(item.text)
    if value <= count:
        upgrade_actions = ActionChains(driver)
        upgrade_actions.move_to_element(item)
        upgrade_actions.click()
        upgrade_actions.perform()
```

