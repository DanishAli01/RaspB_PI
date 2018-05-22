# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'AC070f341066262e44affecaca016a0072'
auth_token = '53396b5286a52ebfced5bebf0146db8c'
client = Client(account_sid, auth_token)

message = client.messages.create(


body='Hello there!',
     from_ = '+353861803452',
             to = '+353892434393'
                          )

print(message.sid)



call = client.calls.create(

                            to = '+353871406642',
                           from_='+353861803452',
                           url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient"

)
print(call.sid)

