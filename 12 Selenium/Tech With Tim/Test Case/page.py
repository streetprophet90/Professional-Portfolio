from locator import *
from element import BasePageElement


class SearchTextElement(BasePageElement):
    """This class gets the search text from the specified locator"""
    #The locator for search box where search string is entered
    locator = 'q'


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):

    def is_title_matches(self):
        return "Python" in self.driver.title #after this go to main.py to write some code_1

    def click_go_button(self):
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()  #after this go to locator.py to write some code_1

class SearchResultsPage(BasePage):

    def is_results_found(self):
        return "No results found." not in self.driver.page_source