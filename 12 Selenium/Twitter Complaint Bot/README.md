
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


Please note that this script interacts with real websites and services. Be sure to use it responsibly and in accordance with the terms of service of the respective platforms.