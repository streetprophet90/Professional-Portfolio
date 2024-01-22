from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class LibraryBookRenewal:
    def __init__(self, library_url, username, password):
        self.library_url = library_url
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()

