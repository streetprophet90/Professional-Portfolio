
# Tinder Automation Script

Automate Tinder interactions using Selenium and Python to log in, swipe right, and like profiles.

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

- Set up your Tinder credentials:
  ```python
  EMAIL_ID = 'YOUR EMAIL'
  PASSWORD = 'YOUR PASSWORD'
  ```

- Set the path to your Chrome WebDriver:
  ```python
  driver_path = Service('DRIVER PATH/chromedriver')
  ```

## Usage

1. Run the script:
    ```bash
    python tinder_swiping_bot.py
    ```

2. The script will automate the login process and start swiping right on Tinder.

## Script Explanation

- The script uses Selenium to control the Chrome browser and interact with the Tinder website.

- It logs in to Tinder with specified credentials, handles various pop-ups, and starts swiping right.

- The loop iterates 20 times, attempting to like profiles. It handles exceptions for pop-ups and profile loading delays.

- The script stops after swiping right 20 times.

## Disclaimer

This script is for educational purposes and should be used responsibly. Respect the terms of service of the website and avoid causing any disruptions.

## License

This Tinder Automation Script is provided under the [MIT License](LICENSE).
```
