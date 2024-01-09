import time
import PIL import ImageGrab
import pyautogui

def is_obstacle(image):
        # Check if there is an obstacle on the screen based on pixel color
    obstacle_color = (83, 83, 83)  # Color of the obstacle in RGB
    return obstacle_color in image.getdata()

def main():
    print("Starting T-Rex Run Bot in 3 seconds...")
    time.sleep(3)

    while True:
            # Capture a portion of the screen where the T-Rex game is located
            screen = ImageGrab.grab(bbox=(300, 340, 600, 400))
            # Convert the image to grayscale to simplify analysis
            screen_gray = screen.convert('L')

            if is_obstacle(screen):
                # Jump when an obstacle is detected
                pyautogui.press('space')
                print("Jump!")

            # Adjust the delay based on your system's performance
            time.sleep(0.1)

if __name__ == "__main__":
    main()
