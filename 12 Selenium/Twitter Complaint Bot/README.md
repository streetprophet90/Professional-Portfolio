
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

