
# Internet Speed Twitter Bot

A Python script using Selenium to check your internet speed using Speedtest and tweet the results to your Internet Service Provider on Twitter.

## Requirements

- Python 3.x
- Selenium
- Chrome WebDriver

Install the required dependencies using:

```bash
pip install selenium
```

Make sure to download the Chrome WebDriver from [here](https://sites.google.com/chromium.org/driver/) and provide the path in the script.

## Configuration

- Set up your Twitter credentials:
  ```python
  TWITTER_EMAIL = 'YOUR TWITTER EMAIL'
  TWITTER_PASSWORD = 'YOUR TWITTER PASSWORD'
  ```

- Set the promised internet speed values and the path to your Chrome WebDriver:
  ```python
  PROMISED_DOWN = 150
  PROMISED_UP = 10
  CHROME_DRIVER_PATH = 'YOUR CHROME DRIVER PATH'
  ```

## Usage

1. Run the script:
    ```bash
    python complaint_bot.py
    ```

2. The script will perform a Speedtest, tweet the results to your Internet Service Provider on Twitter, and then exit.

## Script Explanation

- The script uses Selenium to automate the Speedtest website, fetch internet speed values, and tweet them to your Internet Service Provider on Twitter.

- It opens Speedtest, starts the test, waits for the results, and tweets the speed values to the configured Twitter account.

- The Twitter credentials, promised internet speed values, and the Chrome WebDriver path need to be configured.

## Disclaimer

This script is for educational purposes and should be used responsibly. Respect the terms of service of the websites and avoid causing any disruptions.

## License

This Internet Speed Twitter Bot script is provided under the [MIT License](LICENSE).




```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = 'YOUR CHROME DRIVER PATH'
TWITTER_EMAIL = 'YOUR TWITTER EMAIL'
TWITTER_PASSWORD = 'YOUR TWITTER PASSWORD'
```

- Import the necessary modules: `webdriver` from `selenium`, `Keys`, and `time`.
- Define constants for the promised download and upload speeds, Chrome driver path, Twitter email, and Twitter password.

```python
class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.up = 0
        self.down = 0
```

- Define a class `InternetSpeedTwitterBot` with an initialization method that sets up the Chrome WebDriver and initializes `up` and `down` variables.

```python
    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        go_button = self.driver.find_element_by_css_selector(".start-button a")
        go_button.click()
        time.sleep(60)
        self.up = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.down = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text
```

- Define a method `get_internet_speed` within the class to navigate to the Speedtest website, click the "Go" button, wait for the speed test to complete, and fetch the upload and download speeds.

```python
    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")
        time.sleep(2)
        email = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input')
        password = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')
        email.send_keys(TWITTER_EMAIL)
        password.send_keys(TWITTER_PASSWORD)
        time.sleep(2)

        password.send_keys(Keys.ENTER)
        time.sleep(5)
        tweet_compose = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_compose.send_keys(tweet)
        time.sleep(3)
        tweet_button = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        tweet_button.click()
        time.sleep(2)
        self.driver.quit()

 


Please note that this script interacts with real websites and services. Be sure to use it responsibly and in accordance with the terms of service of the respective platforms.