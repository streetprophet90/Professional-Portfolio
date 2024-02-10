##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




from datetime import datetime
import pandas
import random
import smtplib

MY_EMAIL = ""
MY_PASSWORD = ""

today = datetime.now()
today_tuple = (today.month, today.day)

