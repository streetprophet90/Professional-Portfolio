# Gym Class Booker

This Python script uses Selenium to automate the process of booking gym classes on a website. It is particularly useful when you want to schedule your workouts efficiently without manual intervention.

## Requirements

Make sure you have the following installed:

- [Python](https://www.python.org/downloads/)
- [ChromeDriver](https://sites.google.com/chromium.org/driver/) (Ensure it matches your Chrome browser version)
- Selenium library (Install using `pip install selenium`)

## Usage

1. **Clone Repository:**
   ```bash
   git clone 

   ```

2. **Install Dependencies:**
   ```bash
   pip install selenium
   ```

3. **Configure Script:**
   Open the script in a text editor and replace the placeholder values with your actual gym URL, username, and password.

4. **Run the Script:**
   ```bash
   python main.py
   ```
   Adjust the `book_class` method call with the specific details of the class you want to book.

## Script Explanation

The script follows a simple structure:

- `GymClassBooker` class is initialized with the gym URL, username, and password. It uses the Chrome WebDriver for automation.

- `login` method navigates to the gym's login page and performs the login action. You need to customize this part based on the website structure.

- `book_class` method is responsible for finding and booking a gym class. Adjust the logic based on the website structure and how classes are displayed.

- `close_browser` method quits the WebDriver.

- The `__main__` section initializes the `GymClassBooker` class, logs in, books a class (modify the details), and closes the browser afterward.

Note: Make sure to use this script responsibly and in compliance with the terms of service of the gym's website. Automating interactions may violate website policies.



## Usage

4. Replace the placeholder values in the script with your actual gym URL, username, and password.

```python
gym_url = "Your GYM URL"
username = "Your username"
password = "Your password"
```

5. Customize the `login` and `book_class` methods based on your gym's website structure. Update the login logic and actions to find and interact with the necessary elements.

```python
def login(self):
    # Implement login logic here (depends on the website structure)
    # Example: Find username and password fields, input credentials, and click login button

def book_class(self, class_name, date, time):
    # Navigate to the page where the classes are listed
    # Locate the desired class based on its name, date, and time
    # Click the book button or perform necessary actions to book the class
```

6. Save the changes.

7. Run the script.

```bash
python main.py
```

Note: Be responsible when automating interactions with websites. Make sure your actions comply with the gym's policies and terms of service. Use the script at your own risk.