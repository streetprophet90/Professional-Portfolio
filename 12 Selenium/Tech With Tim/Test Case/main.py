import unittest
from selenium import webdriver
import page

class PythonOrgSearch(unittest.TestCase):

    def SetUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.python.org")


