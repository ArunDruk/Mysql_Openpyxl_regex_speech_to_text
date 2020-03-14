#API Key = 53PVJUZUE7NB3FG9RDYEXVZ895DKEI76
# Secret Key = FV9JSBO93CIRXS5S

import requests
import json

URL = 'https://www.sms4india.com/api/v1/sendCampaign'

# get request
def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
  req_params = {
  'apikey':apiKey,
  'secret':secretKey,
  'usetype':useType,
  'phone': phoneNo,
  'message':textMessage,
  'senderid':senderId
  }
  return requests.post(reqUrl, req_params)

# get response
# response = sendPostRequest(URL, 'provided-api-key', 'provided-secret', 'prod/stage', 'valid-to-mobile', 'active-sender-id', 'message-text' )
message="Hello Man, Come to US and Enjoy the life here; :) "
response = sendPostRequest(URL, '53PVJUZUE7NB3FG9RDYEXVZ895DKEI76', 'FV9JSBO93CIRXS5S', 'stage', '9986233833', 'arundruk@gmail.com', message )
"""
  Note:-
    you must provide apikey, secretkey, usetype, mobile, senderid and message values
    and then requst to api
"""
# print response if you want
print (response.text)