import requests
from requests.auth import HTTPBasicAuth

# url= "https://manheim-api-test.epfinnp.coxautoinc.com/receipts2"
url ="http://api.github.com"
response=requests.get(url) #,auth = HTTPBasicAuth('cpcsauser', 'oracle123'))

# print(response.text)
print(response.url)