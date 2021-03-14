# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.twiml.voice_response import Conference, Dial, VoiceResponse
from twilio.rest import Client
import time

app = Flask(__name__)

client_sid = 'AC10820b6be0861d83a553d865b1b3448e'
auth_token = '72f2f538ec22d32eba4da9fbc5993719'
client = Client(client_sid, auth_token)

@app.route("/", methods=['GET', 'POST'])
def sms_ahoy_reply():
    """Response to message sent by the user"""
    from_msg = request.values.get("From")
    tomsg = request.values.get("To")
    print("Message from:"+ str(from_msg))
    msgrcv = request.values.get("Body")
    print("Message from:"+ str(msgrcv))
    to_call,from_call = from_msg, tomsg
#connect call from which message was sent
    client.calls.create(to = to_call, from_=from_call, url='https://handler.twilio.com/twiml/EHba30cc79415c66f44c8a4e3fb446a26a', method = "GET")

    #time.sleep(2)
# connect call in conference
    client.calls.create(to = msgrcv, from_=from_call, url='https://handler.twilio.com/twiml/EHa2ba8ce428542c66042c3982b20e8087', method = "GET")
    z = "Executed"
    return(z)

if __name__ == "__main__":
    app.run(debug=True)

