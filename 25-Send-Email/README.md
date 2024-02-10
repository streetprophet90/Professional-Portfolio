


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