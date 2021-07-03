import requests
import json

url="https://reqres.in/api/users"


body= {"name": "Dragon", "job": "Tech_lead"}
# If the body is in str format or .json format, you can use json.loads
# Suppose if the body is already in dictionary
body_json=json.dumps(body)
response=requests.post(url,body_json)

r_json=response.json()

print(response.status_code)
print(response.content)
print(response.text)


# response= requests.get(url)
#
# print(response.text)
