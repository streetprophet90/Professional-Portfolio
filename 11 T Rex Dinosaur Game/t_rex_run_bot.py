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
