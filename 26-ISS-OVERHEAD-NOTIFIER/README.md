
# ISS Tracker and Nighttime Notifier

This script tracks the International Space Station (ISS) and notifies the user via email if the ISS is overhead during nighttime based on the user's location.

## Functionality

1. **ISS Tracking:**
   - Uses the Open Notify API to get the current position of the ISS.
   - Compares the ISS position with the user's specified latitude and longitude to check if the ISS is overhead within a certain range.

2. **Nighttime Detection:**
   - Utilizes the Sunrise-Sunset API to get the sunrise and sunset times for the user's location.
   - Determines if it's currently nighttime based on the user's local time compared to the sunset and sunrise times.

3. **Email Notification:**
   - If the ISS is overhead during nighttime, sends an email notification to the user's specified email address using SMTP (Simple Mail Transfer Protocol).

## Requirements

- Python 3.x
- `requests` library (for making HTTP requests)
- `smtplib` module (for sending emails)
- `datetime` module (for working with dates and times)
- `time` module (for adding delays)
- Access to an SMTP server (e.g., Gmail) to send emails

## Usage

1. **Setup:**
   - Replace the placeholders for `MY_EMAIL`, `MY_PASSWORD`, `MY_LAT`, and `MY_LONG` with your email credentials and your latitude and longitude, respectively.

2. **Run the Script:**
   - Execute the script, and it will continuously monitor the ISS and nighttime conditions in the background.

3. **Receive Notifications:**
   - If the ISS is overhead during nighttime, you will receive an email notification informing you to look up at the sky.

