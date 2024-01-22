# Library Book Renewal Automation

This Python script utilizes Selenium to automate the process of renewing library books. It is designed to interact with the specific structure and elements of your library's website. Please note that the implementation might vary based on the library's website structure.

## Prerequisites

Before running the script, ensure you have the following installed:

- [Python](https://www.python.org/downloads/)
- [Selenium](https://pypi.org/project/selenium/)
- [ChromeDriver](https://sites.google.com/chromium.org/driver/) (ensure it's in your system PATH)


## Usage

1. Clone the repository to your local machine.


2. Install the required packages.

```bash
pip install selenium
```

3. Open the `main.py` file in a text editor.

4. Replace the placeholder values in the script with your actual library URL, username, and password.

```python
library_url = "Your Library URL"
username = "Your username"
password = "Your password"
```

5. Customize the `login` and `renew_books` methods based on your library's website structure. Update the login logic and actions to find and interact with the necessary elements.

```python
def login(self):
    # Implement login logic here (depends on the website structure)
    # Example: Find username and password fields, input credentials, and click login button

