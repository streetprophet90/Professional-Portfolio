
# Cookie Clicker Bot

Automate the Cookie Clicker game using Selenium and Python to click on the cookie and purchase upgrades.

## Requirements

- Python 3.x
- Selenium
- Chrome WebDriver

Install the required dependencies using:

```bash
pip install selenium
```

Make sure to download the Chrome WebDriver from [here](https://sites.google.com/chromium.org/driver/) and provide the path in the script.

## Usage

1. Set up the Chrome WebDriver path:
    ```python
    chrome_driver_path = "YOUR CHROME DRIVER PATH"
    ```

2. Run the script:
    ```bash
    python cookie_playing_bot.py
    ```

3. The script will automate clicking on the cookie and purchasing upgrades.

4. The bot runs for 5 minutes, then stops and prints the cookies per second count.

## Script Explanation

- The script uses Selenium to control the Chrome browser and interact with the [Cookie Clicker game](http://orteil.dashnet.org/experiments/cookie/).

- It continuously clicks the cookie and purchases the most expensive affordable upgrade every 5 seconds.

- The bot stops after 5 minutes and prints the cookies per second count.

## Configuration

- Adjust the Chrome WebDriver path: Change the value of `chrome_driver_path` to the path of your Chrome WebDriver.

- Modify time intervals: You can adjust the time intervals for clicking and checking upgrades.

## Disclaimer

This script is for educational purposes and should be used responsibly. Respect the terms of service of the website and avoid causing any disruptions.

## License

``` bash
This Cookie Clicker Bot script is provided under the [MIT License](LICENSE).
```

# Lines of code
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
```

1. **Import necessary libraries:**
   - `webdriver`: Provides a way to automate web browser interactions (Selenium).
   - `By`: Defines the mechanisms used to locate elements within a document (Selenium).
   - `time`: Provides functions to add delays in the script.

```python
chrome_driver_path = "YOUR CHROME DRIVER PATH"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")
```

2. **Set up Chrome WebDriver and open the Cookie Clicker game:**
   - `chrome_driver_path`: Replace with the path to your Chrome WebDriver executable.
   - `webdriver.Chrome`: Initializes a new instance of the Chrome WebDriver.
   - `driver.get`: Opens the specified URL (Cookie Clicker game).

```python
cookie = driver.find_element(By.ID, "cookie")
```

3. **Get the cookie element:**
   - `driver.find_element`: Finds the HTML element using the specified method (`By.ID`) and value ("cookie").

```python
items = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_ids = [item.get_attribute("id") for item in items]
```

4. **Get upgrade item IDs:**
   - `driver.find_elements`: Finds multiple HTML elements using the specified method (`By.CSS_SELECTOR`) and value ("#store div").
   - Retrieves the IDs of the upgrade items.

```python
timeout = time.time() + 5
five_min = time.time() + 60*5  # 5 minutes
```

5. **Set up timeouts:**
   - `timeout`: Time until the next cookie click (initially set to 5 seconds).
   - `five_min`: Time until the script stops (initially set to 5 minutes).

```python
while True:
    cookie.click()
```

6. **Continuous clicking on the cookie:**
   - Enters a loop that continuously clicks on the cookie.

```python
    if time.time() > timeout:
```

7. **Check for upgrades every 5 seconds:**
   - Executes the code inside the block every 5 seconds.

```python
        all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
        item_prices = []
```

8. **Get upgrade prices:**
   - `driver.find_elements`: Finds multiple HTML elements using the specified method (`By.CSS_SELECTOR`) and value ("#store b").
   - Retrieves the prices of the upgrades.

```python
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)
```

9. **Convert upgrade prices to integers:**
   - Parses and converts the prices from text to integers.

```python
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]
```

10. **Create a dictionary of store items and prices:**
    - Maps each upgrade price to its corresponding item ID.

```python
        money_element = driver.find_element(By.ID, "money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)
```

11. **Get current cookie count:**
    - `driver.find_element`: Finds the element with ID "money" and retrieves the text.
    - Removes commas from the text and converts it to an integer.

```python
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id
```

12. **Find affordable upgrades:**
    - Creates a dictionary of affordable upgrades based on the current cookie count.

```python
        highest_price_affordable_upgrade = max(affordable_upgrades, key=int)
        print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]
```

13. **Purchase the most expensive affordable upgrade:**
    - Finds the highest priced upgrade among the affordable ones.
    - Prints the price of the purchased upgrade.
    - Retrieves the ID of the upgrade to purchase.

```python
        driver.find_element(By.ID, to_purchase_id).click()
```

14. **Click on the purchased upgrade:**
    - `driver.find_element`: Finds the upgrade element by ID and clicks on it.

```python
        timeout = time.time() + 5
```

15. **Reset the timeout for the next check:**
    - Adds another 5 seconds until the next check.

```python
    if time.time() > five_min:
        cookie_per_s = driver.find_element(By.ID, "cps").text
        print(cookie_per_s)
        break
```

16. **Stop the script after 5 minutes and print CPS:**
    - Checks if 5 minutes have passed.
    - Retrieves and prints the "cookies per second" (CPS) count.
    - Breaks out of the loop to stop the script.

This script automates the process of clicking on the cookie and purchasing upgrades in the Cookie Clicker game using Selenium.
