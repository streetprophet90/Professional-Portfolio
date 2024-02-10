


# Birthday Email Sender

This is an extra hard starting project that automates sending birthday emails to people whose birthdays are listed in a CSV file (`birthdays.csv`). The program checks if today matches a birthday in the CSV file, picks a random letter template, replaces placeholders with the birthday person's name, and sends the letter to their email address.

## Project Steps

1. **Update the birthdays.csv:**
   - The CSV file should contain the names, birthdays (month and day), and email addresses of the individuals.

2. **Check if today matches a birthday in the birthdays.csv:**
   - The program checks if today's date matches any birthday in the CSV file.

3. **Pick a random letter from letter templates:**
   - If a birthday matches today's date, the program selects a random letter template from a specified directory.

4. **Send the letter to the person's email address:**
   - The program replaces placeholders in the letter template with the person's actual name and sends the letter to their email address using SMTP (Simple Mail Transfer Protocol).

## Requirements

- Python 3.x
- Pandas library (for reading CSV files)
- smtplib module (for sending emails)
- Access to an SMTP server (e.g., Gmail) to send emails

## Usage

1. Ensure the birthdays.csv file is correctly formatted with names, birthdays, and email addresses.
2. Create letter templates (letter_1.txt, letter_2.txt, etc.) with placeholders for names.
3. Replace placeholders in the letter templates with `[NAME]` to be dynamically replaced with the birthday person's name.
4. Update the `MY_EMAIL` and `MY_PASSWORD` variables with your email credentials.
5. Run the program, and it will automatically check for birthdays and send emails if there's a match.

## Note

- This project uses Gmail's SMTP server for sending emails. Ensure that "Less secure app access" is turned on in your Gmail account settings or use App Passwords if you have 2-step verification enabled.
- Make sure to handle exceptions and errors, especially regarding file paths, SMTP connections, and email sending.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


This README provides an overview of the Birthday Email Sender project, including its purpose, steps, requirements, usage instructions, notes, and license information.

# Every line of Code

```python
from datetime import datetime
import pandas
import random
import smtplib
```

- `from datetime import datetime`: Imports the `datetime` class from the `datetime` module, which is used to work with dates and times.
- `import pandas`: Imports the `pandas` library, which is used for data manipulation and analysis, particularly for reading CSV files.
- `import random`: Imports the `random` module, which provides functions for generating random numbers.
- `import smtplib`: Imports the `smtplib` module, which is used for sending emails using the Simple Mail Transfer Protocol (SMTP).

```python
MY_EMAIL = ""
MY_PASSWORD = ""
```

- Defines two empty strings, `MY_EMAIL` and `MY_PASSWORD`, to store the sender's email address and password, respectively. These will be filled with actual email credentials later in the code.

```python
today = datetime.now()
today_tuple = (today.month, today.day)
```

- Retrieves the current date and time using the `datetime.now()` method and stores it in the `today` variable.
- Extracts the month and day from the current date and stores them as a tuple in the `today_tuple` variable.

```python
data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
```

- Reads the data from the CSV file named "birthdays.csv" using `pandas.read_csv()` and stores it in the `data` DataFrame.
- Iterates over each row in the DataFrame using `data.iterrows()`, extracts the month and day from each row, and creates a dictionary called `birthdays_dict`. This dictionary has tuples of month and day as keys and the corresponding rows from the DataFrame as values.

```python
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
```

- Checks if today's date (stored in `today_tuple`) matches any birthday in the `birthdays_dict`.
- If there's a match, selects the corresponding birthday person's data from `birthdays_dict` and stores it in `birthday_person`.
- Constructs a file path for a letter template by randomly choosing a number between 1 and 3 using `random.randint()` and appending it to the file path string.
- Opens the selected letter template file, reads its contents, and replaces the placeholder `[NAME]` with the birthday person's name.

```python
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL,
                        to_addrs=birthday_person["email"],
                        msg=f"Subject:Happy Birthday!\n\n{contents}"
                        )
```

- Establishes a connection to the Gmail SMTP server (`smtp.gmail.com`) using `smtplib.SMTP()`.
- Starts the TLS (Transport Layer Security) encryption protocol for secure communication with `connection.starttls()`.
- Logs in to the SMTP server using the sender's email address (`MY_EMAIL`) and password (`MY_PASSWORD`) with `connection.login()`.
- Sends an email using `connection.sendmail()` by specifying the sender's email address (`from_addr`), the recipient's email address obtained from `birthday_person["email"]` (`to_addrs`), and the message content (`msg`). The message contains a subject line ("Happy Birthday!") and the contents of the letter template with the birthday person's name.

Each line of code in this script serves a specific purpose, from reading birthday data, selecting a random letter template, to sending birthday emails to recipients.