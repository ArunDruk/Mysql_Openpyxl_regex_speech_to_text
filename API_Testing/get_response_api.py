import requests
from requests.auth import HTTPBasicAuth
import json

# url= "https://manheim-api-test.epfinnp.coxautoinc.com/receipts2"
# url ="http://api.github.com"

# url="http://reqres.in/api/users?page=2"

url="http://reqres.in/api/users/2"
response=requests.get(url) #,auth = HTTPBasicAuth('cpcsauser', 'oracle123'))

# print(response.text)
D1=dict()

D1=response.json()
# D1=json.loads(response.text)

# print(D1)
# print(D1['data']['avatar'])
print(D1['ad']['url'])


# print(type(response.text))