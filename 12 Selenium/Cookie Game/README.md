
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

This Cookie Clicker Bot script is provided under the [MIT License](LICENSE).
```
