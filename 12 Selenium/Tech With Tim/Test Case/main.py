import unittest
from selenium import webdriver
import page

class PythonOrgSearch(unittest.TestCase):

    def SetUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.python.org")

    def test_search_in_python_org(self):
        """Tests python.org search feature. Searches for the word "pycon" then
        verified that some results show up. Note that it does not look for
        any particular text in search results page. This test verifies that
        the results were not empty."""

        # Load the main page. In this case the home page of Python.org.

        mainPage = page.MainPage(self.driver)
        # Checks if the word "Python" is in title
        assert mainPage.is_title_matches() #Code written_1

        # Sets the text of search textbox to "pycon"
        mainPage.search_text_element = "pycon"
        mainPage.click_go_button()
        search_results_page = page.SearchResultsPage(self.driver)
        # Verifies that the results page is not empty
        assert search_results_page.is_results_found()

    def TearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()