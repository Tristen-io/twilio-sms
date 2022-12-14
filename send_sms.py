import os
from twilio.rest import Client
from dotenv import load_dotenv

def configure():
    load_dotenv()
configure()
# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ[os.getenv('TWILIO_ACCOUNT_SID')]
auth_token = os.environ[os.getenv('TWILIO_AUTH_TOKEN')]
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='This is the ship that made the Kessel Run in fourteen parsecs?',
         from_='+15017122661',
         to='+15558675310'
     )

print(message.sid)