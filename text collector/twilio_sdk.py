from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC75a49c1088af45446c09f384ade422c5"
# Your Auth Token from twilio.com/console
auth_token  = "f9d31809b71b84e1f85ece5c27b86766"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+13302688343", 
    from_="+12055375793",
    body="Hello from Python!")

print(message.sid)