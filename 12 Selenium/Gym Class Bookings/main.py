from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GymClassBooker:
    def __init__(self, gym_url, username, password):
        self.gym_url = gym_url
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get(self.gym_url)
        # Implement login logic here (depends on the website structure)
        # Example: Find username and password fields, input credentials, and click login button

    def book_class(self, class_name, date, time):
        # Navigate to the page where the classes are listed
        # locate the desired class based on its name, date and time
        # click the book button or perform necessary actions to bok the class

    def close_browser(self):
        self.driver.quit()

if __name__ == "__main__":
    #Replace these with your actual gym URL, username, and password
    gym_url = "Your GYM URL"
    username = "Your username"
    password = "Your password"

    gym_booker = GymClassBooker(gym_url, username, password)

    try:
        gym_booker.login()
        #call the book_class method with the specific class details you want to book
        #Example: gym_booker.book_class("Yoga Class", "2022-01-15", "16:00")
    finally:
        gym_booker.close_browser()
