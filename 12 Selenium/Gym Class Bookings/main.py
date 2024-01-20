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

