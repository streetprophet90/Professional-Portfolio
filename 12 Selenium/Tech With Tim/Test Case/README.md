

---

# Automated Testing with Selenium

This repository contains Python scripts for automated testing using Selenium WebDriver. The testing scenario involves searching for a keyword on the Python.org website and verifying the search results.

## Files:

1. **main.py:**
   - **PythonOrgSearch Class:** A unittest class for testing the search functionality on Python.org.
   - **SetUp:** Initializes a WebDriver instance and navigates to the Python.org website.
   - **test_search_in_python_org:** Tests the search feature by searching for the word "pycon" and verifying that some results show up.
   - **TearDown:** Closes the WebDriver.

2. **locator.py:**
   - **MainPageLocators Class:** Defines locators for elements on the main page.
     - `GO_BUTTON`: Locator for the "Submit" button.

3. **element.py:**
   - **BasePageElement Class:** Defines a base page element class with methods for setting and getting text.
   - **SearchTextElement Class:** A subclass of BasePageElement that specifies the locator for the search box.

4. **page.py:**
   - **BasePage Class:** Defines a base page class that is initialized for every page object class.
   - **MainPage Class:** Subclass of BasePage, contains action methods for the home page of Python.org.
     - `is_title_matches:` Checks if the word "Python" is in the page title.
     - `click_go_button:` Clicks the "Submit" button.
   - **SearchResultsPage Class:** Subclass of BasePage, contains a method for verifying search results.

## Execution:

To run the automated tests, execute the `main.py` script. The tests will navigate to the Python.org website, perform a search for "pycon," and verify the presence of search results.

---

