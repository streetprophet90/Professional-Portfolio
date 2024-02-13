
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

## Note

- Ensure that your email provider allows access via SMTP. For Gmail, you may need to enable "Less secure app access" in your account settings.
- Keep in mind that the script will run indefinitely, checking the ISS position and nighttime conditions every 60 seconds.

## License
```
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

This README provides an overview of the ISS Tracker and Nighttime Notifier script, including its functionality, requirements, usage instructions, notes, and license information.

# Every line of Code

```python
import requests
from datetime import datetime
import smtplib
import time
```

- `import requests`: Imports the `requests` library, which is used to make HTTP requests to APIs.
- `from datetime import datetime`: Imports the `datetime` class from the `datetime` module, which is used to work with dates and times.
- `import smtplib`: Imports the `smtplib` module, which is used for sending emails using the Simple Mail Transfer Protocol (SMTP).
- `import time`: Imports the `time` module, which is used to add time-related functionality such as delays.

```python
MY_EMAIL = ""
MY_PASSWORD = ""
MY_LAT = 6.695070  # Your latitude
MY_LONG = -1.615800  # Your longitude
```

- Defines variables `MY_EMAIL`, `MY_PASSWORD`, `MY_LAT`, and `MY_LONG` to store the user's email credentials, latitude, and longitude.
- Note: The email credentials should be filled with the user's actual email address and password. Latitude and longitude should be set to the user's actual coordinates.

```python
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True
```

- Defines a function `is_iss_overhead()` to check if the ISS (International Space Station) is overhead the user's location.
- Makes a GET request to the Open Notify API endpoint (`http://api.open-notify.org/iss-now.json`) to get the current position of the ISS.
- Parses the JSON response and extracts the ISS latitude and longitude.
- Checks if the difference between the user's latitude and longitude and the ISS latitude and longitude is within ±5 degrees. If so, returns `True`.

```python
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True
```

- Defines a function `is_night()` to check if it's currently nighttime at the user's location.
- Constructs a dictionary `parameters` containing latitude, longitude, and a parameter to return unformatted times.
- Makes a GET request to the Sunrise-Sunset API endpoint (`https://api.sunrise-sunset.org/json`) with the specified parameters.
- Parses the JSON response to extract the sunrise and sunset times and convert them to integers.
- Retrieves the current hour using `datetime.now().hour`.
- Checks if the current hour is greater than or equal to the sunset hour or less than or equal to the sunrise hour. If so, returns `True`.

