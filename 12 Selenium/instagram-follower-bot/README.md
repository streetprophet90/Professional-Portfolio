# Instagram Follower Bot

This Python script uses Selenium to automate the process of logging into Instagram, navigating to a specified account, and following its followers. It's designed to interact with Instagram's web interface.

## Prerequisites

Before running the script, make sure you have the following:

- [Python](https://www.python.org/downloads/)
- [Selenium](https://pypi.org/project/selenium/)
- [ChromeDriver](https://sites.google.com/chromium.org/driver/) (ensure it's in your system PATH)

## Configuration

1. Clone the repository to your local machine.

    ```bash
    git clone https://github.com/your-username/instagram-follower-bot.git
    cd instagram-follower-bot
    ```

2. Install the required packages.

    ```bash
    pip install selenium
    ```
3. Open the `instagram_follower_bot.py` file in a text editor.

4. Replace the placeholder values with your actual ChromeDriver path, Instagram username, and password.

    ```python
    CHROME_DRIVER_PATH = "YOUR CHROME DRIVER PATH"
    SIMILAR_ACCOUNT = "buzzfeedtasty"
    USERNAME = "YOUR INSTAGRAM USERNAME"
    PASSWORD = "YOUR INSTAGRAM PASSWORD"
    ```

5. Customize the `login`, `find_followers`, and `follow` methods based on your Instagram web interface. Update the login logic and actions to find and interact with the necessary elements.

    ```python
    def login(self):
        # Implement login logic here
        # Example: Find username and password fields, input credentials, and click login button

    def find_followers(self):
        # Navigate to the page where the followers are listed
        # Locate the desired elements based on the HTML structure

    def follow(self):
        # Iterate through the followers and click the follow button
        # Handle any exceptions that may occur during the process
    ```

6. Save the changes.

7. Run the script.

    ```bash
    python instagram_follower_bot.py
    ```



```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time
```

1. Import the necessary modules from the Selenium library, including the WebDriver, keys, exceptions, and time.

```python
CHROME_DRIVER_PATH = "YOUR CHROME DRIVER PATH"
SIMILAR_ACCOUNT = "buzzfeedtasty"
USERNAME = "YOUR INSTAGRAM USERNAME"
PASSWORD = "YOUR INSTAGRAM PASSWORD"
```

2. Set up constants for the ChromeDriver path, the Instagram account to interact with, and your Instagram username and password.

```python
class InstaFollower:
```

3. Define a class named `InstaFollower`.

```python
def __init__(self, path):
    self.driver = webdriver.Chrome(executable_path=path)
```

4. Define the constructor method for the `InstaFollower` class, initializing a WebDriver instance with the provided ChromeDriver path.

```python
def login(self):
    self.driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(5)
```

5. Define a method named `login` within the `InstaFollower` class. This method navigates to the Instagram login page and pauses execution for 5 seconds.

```python
    username = self.driver.find_element("name", "username")
    password = self.driver.find_element("name", "password")

    username.send_keys(USERNAME)
    password.send_keys(PASSWORD)

    time.sleep(2)
    password.send_keys(Keys.ENTER)
```

6. Find the username and password input fields, input the Instagram username and password, and simulate pressing the Enter key.

```python
def find_followers(self):
    time.sleep(5)
    self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")

    time.sleep(2)
    followers = self.driver.find_element("xpath", '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
    followers.click()

    time.sleep(2)
    modal = self.driver.find_element("xpath", '/html/body/div[4]/div/div/div[2]')
    for i in range(10):
        self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
        time.sleep(2)
```

7. Define a method named `find_followers`. This method navigates to the Instagram profile of a specified account, opens the followers modal, and scrolls down 10 times to load more followers.

```python
def follow(self):
    all_buttons = self.driver.find_elements("css selector", "li button")
    for button in all_buttons:
        try:
            button.click()
            time.sleep(1)
        except ElementClickInterceptedException:
            cancel_button = self.driver.find_element("xpath", '/html/body/div[5]/div/div/div/div[3]/button[2]')
            cancel_button.click()
```

8. Define a method named `follow`. This method finds all follow buttons on the followers modal and attempts to click them. If an `ElementClickInterceptedException` occurs, it finds and clicks the cancel button.

```python
bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()
```

9. Create an instance of the `InstaFollower` class, call the `login`, `find_followers`, and `follow` methods to automate Instagram interaction.

This code essentially automates the process of logging into Instagram, navigating to a specific account, and following its followers.


**Note:** Be responsible when automating interactions with websites. Make sure your actions comply with Instagram's policies and terms of service. Use the script at your own risk.

Feel free to contribute to and improve this script!