# /usr/bin/env python
# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import Client
from datetime import datetime
from threading import Timer
import time

def send_message():
    # Find these values at https://twilio.com/user/account
    account_sid = "your_id"
    auth_token = "your_token"
    client = Client(account_sid, auth_token)

    client.messages.create(to="your_mob", from_="+14158910679", body="Hello there!")
def hello_world():
    print "hello world"
i=0
while True:
    x=datetime.today()
    y=x.replace(day=x.day+i, hour=5, minute=7, second=0, microsecond=0)
    delta_t=y-x
    #print "here1"
    secs=delta_t.seconds+1

    t = Timer(secs, hello_world)
    #print "here2"
    t.start()
    #print "here3"
    i=i+1
    #print "here4"