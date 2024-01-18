import unittest
from selenium import webdriver
import page

class PythonOrgSearch(unittest.TestCase):

    def SetUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.python.org")

    def test_title(self):
        mainPage = page.MainPage()
        assert mainPage.is_title_matches() #Code written_1


    def TearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()