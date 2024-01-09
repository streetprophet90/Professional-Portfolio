
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

2. **Define a function to check for obstacles:**
   - `is_obstacle` is a function that takes an image and checks if the specified obstacle color is present in the image's pixel data.

```python
def main():
    print("Starting T-Rex Run Bot in 3 seconds...")
    time.sleep(3)
```

3. **Define the main function:**
   - `main` is the main function of the script.
   - It prints a starting message and then waits for 3 seconds before entering the game loop.

```python
    while True:
        # Capture a portion of the screen where the T-Rex game is located
        screen = ImageGrab.grab(bbox=(300, 340, 600, 400))
```

4. **Capture a portion of the screen:**
   - `ImageGrab.grab` captures a portion of the screen specified by the bounding box (300, 340, 600, 400).
   - Adjust the bounding box based on the location of the T-Rex game on your screen.

```python
        # Convert the image to grayscale to simplify analysis
        screen_gray = screen.convert('L')
```

5. **Convert the image to grayscale:**
   - `convert('L')` converts the color image to grayscale to simplify the analysis.
   - Grayscale images have a single channel, making it easier to work with pixel values.

```python
        if is_obstacle(screen):
            # Jump when an obstacle is detected
            pyautogui.press('space')
            print("Jump!")
```

6. **Check for obstacles and simulate jump:**
   - Calls the `is_obstacle` function to check if an obstacle is present in the captured screen.
   - If an obstacle is detected, simulates a jump by pressing the space bar using `pyautogui.press`.

```python
        # Adjust the delay based on your system's performance
        time.sleep(0.1)
```

