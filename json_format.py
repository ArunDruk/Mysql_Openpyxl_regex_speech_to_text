import json

req_params = '{"apikey":"ABC","secret":"abc123"}' #'usetype':'Stage','phone': "+91-9986233833"}'

req_json=json.loads(req_params)

print(req_params)
print(req_json)