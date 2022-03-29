from twilio.rest import Client

account_sid=''
auth_token=''

def send_sms(msg_body):
    client=Client(account_sid,auth_token)
    message=client.messages.create(to="+91",from_="+",body=msg_body)


