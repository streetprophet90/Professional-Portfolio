from twilio.rest import Client

TWILIO_SID ="YOUR SID"
TWILIO_AUTH_TOKEN = "YOUR AUTH TOKEN"
TWILIO_VIRTUAL_NUMBER = "YOUR VIRTUAL NUMBER"
TWILIO_VERIFIED_NUMBER = "YOUR NUMBER"

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)


