

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

# Every Line of Code

### `main.py`

```python
import unittest
from selenium import webdriver
import page
```

1. Import necessary modules for unittest, Selenium, and the `page` module.

```python
class PythonOrgSearch(unittest.TestCase):
```

2. Define a test case class named `PythonOrgSearch` that inherits from `unittest.TestCase`.

```python
    def SetUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.python.org")
```

3. Define a setup method (`SetUp`) that initializes a Chrome WebDriver instance and navigates to the Python.org website.

```python
    def test_search_in_python_org(self):
        # ... (explained below)
```

4. Define a test method (`test_search_in_python_org`) to test the Python.org search feature.

```python
    def TearDown(self):
        self.driver.close()
```

5. Define a teardown method (`TearDown`) that closes the WebDriver after the test is complete.

```python
if __name__ == "__main__":
    unittest.main()
```

6. Check if the script is executed directly and run the unittest.

### `locator.py`

```python
from selenium.webdriver.common.by import By

class MainPageLocators(object):
    GO_BUTTON = (By.ID, "submit")
```

1. Import `By` from `selenium.webdriver.common.by`.
2. Define a class `MainPageLocators` that contains a tuple `GO_BUTTON` representing the locator for the "Submit" button.

### `element.py`

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class BasePageElement(object):
    # ... (explained below)
```

1. Import `WebDriverWait` and `By` from Selenium.

```python
    def __init__(self):
        self.locator = None
```

2. Initialize the `BasePageElement` class with a `locator` attribute.

```python
    def __set__(self, obj, value):
        # ... (explained below)
```

