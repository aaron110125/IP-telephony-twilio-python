from twilio.rest import Client


account_sid = 'AC10820b6be0861d83a553d865b1b3448e'
auth_token = '72f2f538ec22d32eba4da9fbc5993719'
client = Client(account_sid, auth_token)

call = client.calls.create(
                        url='https://handler.twilio.com/twiml/EH74665b08d179fd539620f198cf3a06af',
                        to='+18578693592',
                        from_='+12056568855'
                    )

print(call.sid)

