from twilio.rest import Client

class NotificationManager:

    TWILIO_SID = "ACd49222ff0c291f1996451b3dd003c6e3"
    TWILIO_AUTH_TOKEN = "cdcc3a16f5429de5823bb32f8ee90b8e"
    TWILIO_VIRTUAL_NUMBER = "+18456971489"
    TWILIO_VERIFIED_NUMBER = "***********"

    def __init__(self):
        self.client = Client(self.TWILIO_SID, self.TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages \
            .create(
            body=message,
            from_=self.TWILIO_VIRTUAL_NUMBER,
            to=self.TWILIO_VERIFIED_NUMBER
        )
