
# T-Rex Run Bot

Automate playing the T-Rex run game using a Python script that analyzes the screen and simulates keyboard presses.

## Requirements

- Python 3.x
- Pillow (PIL)
- PyAutoGUI

Install the required dependencies using:

```bash
pip install pillow pyautogui
```

## Usage

1. Open the T-Rex run game in your web browser: [T-Rex Run Game](https://elgoog.im/t-rex/)

2. Position the game window in a way that the T-Rex character is visible on your screen.

3. Run the T-Rex Run Bot script:

```bash
python trex_run_bot.py
```

4. The script will start in 3 seconds. The T-Rex character will jump automatically when an obstacle is detected.

5. To stop the script, press `Ctrl+C` in the terminal.

## Configuration

- You can adjust the delay in the script (`time.sleep(0.1)`) based on your system's performance.

## Disclaimer

This script is for educational purposes and should be used responsibly. Respect the terms of service of the website and avoid causing any disruptions.

## License

This T-Rex Run Bot script is provided under the [MIT License](LICENSE).


# Each line of code

```python
import time
from PIL import ImageGrab
import pyautogui
```

1. **Import necessary libraries:**
   - `time`: Provides functions to add delays in the script.
   - `ImageGrab` from `PIL`: Allows capturing a portion of the screen.
   - `pyautogui`: Used for controlling the keyboard and mouse.

```python
def is_obstacle(image):
    # Check if there is an obstacle on the screen based on pixel color
    obstacle_color = (83, 83, 83)  # Color of the obstacle in RGB
    return obstacle_color in image.getdata()
```
