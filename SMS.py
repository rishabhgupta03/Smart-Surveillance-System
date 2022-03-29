from twilio.rest import Client

account_sid='AC002dbe648a2859f40156c33214ae2877'
auth_token='93ab466d6f682095a12727dc09c5aefb'

def send_sms(msg_body):
    client=Client(account_sid,auth_token)
    message=client.messages.create(to="+919990055131",from_="+16362514487",body=msg_body)


