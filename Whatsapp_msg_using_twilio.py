######### pip install twilio ###########

import os
from twilio.rest import Client

client=Client()

from_whatsapp_num='whatsapp:+919738476056'
to_whatsapp_num='whatsapp:+919986233833'

msg ="Hello, This is Arun, Can you call me.."
client.messages.create(body=msg,
                       from_=from_whatsapp_num,
                       to=to_whatsapp_num)