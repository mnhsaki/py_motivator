from twilio.rest import Client
from config import auth_token,account_sid,phone_number


client = Client(account_sid,auth_token,phone_number),
message = client.messages.create(
    from_='',
    body='',
    to=''
)

print(message.sid)