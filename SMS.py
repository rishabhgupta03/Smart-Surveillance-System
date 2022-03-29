from twilio.rest import Client

account_sid='AC002dbe648a2859f40156c33214ae2877'
auth_token='a092cf2ff178f632e185d10c61f0de69'

def send_sms(msg_body):
    client=Client(account_sid,auth_token)
    message=client.messages.create(to="+919990055131",from_="+16362514487",body=msg_body)


