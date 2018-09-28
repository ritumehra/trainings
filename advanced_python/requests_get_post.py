import requests
import json

resp = requests.get("http://127.0.0.1:5000/empdb/employee")

print("============ Get Request ============= \n")

print("[1] :: Response Status Code : {} ".format(resp.status_code))  # Get the status code 200
print("[2] :: Check if the response is a success : {} ".format(resp.status_code == requests.codes.ok))  # check if response is success
print("[3] :: Get the Json response of the request sent : \n{}\n".format(resp.json()))  # Get the Content
# print("[4] :: Get the Text response of the request sent : \n{}\n".format(resp.text))  # Get the Content
print("[5] :: Get the URL that was accessed : {}".format(resp.url)) # Get the URL

print("============ Get Request Headers============= \n")
# Headers
print("[6] :: Get the header list received in response:{}".format(resp.headers))  # get all the headers
print("[7] :: Get specific header(Content-Type) value: {}".format(resp.headers['Content-Type']))  # get specific header values

# Get the headers of a given URL
resp = requests.head("http://127.0.0.1:5000/empdb/employee")
print("[8] :: Get the header of a given url:\n{}".format(resp.headers))

# Encoding

print(resp.encoding)
resp.encoding = 'utf-8'
print(resp.encoding)

print("============ Post Request with Json Input ============= \n")
payload = {"id": '110', "name": 'ABC',"title": 'Technical Analyst'}
resp = requests.post("http://127.0.0.1:5000/empdb/employee", json=payload)
print("[9] :: Get the Json response of the request sent : \n{}\n".format(resp.json()))  # Get the Content

print("============ Post Request with data Input ============= \n")
payload = json.dumps({"id": '110', "name": 'ABC',"title": 'Technical Analyst'})
resp = requests.post("http://127.0.0.1:5000/emp/post", data=payload)
print("[10] :: Get the Json response of the request sent : \n{}\n".format(resp.json()))  # Get the Content

print("============ Add custom headers ============= \n")

url = 'http://127.0.0.1:5000/emp/post'
payload = json.dumps({"id": '110', "name": 'ABC',"title": 'Technical Analyst'})
headers = {'Content-Type': 'application/json'}

r = requests.post(url, data=payload)
# r = requests.post(url, headers=headers)
# r = requests.post(url)

print(r.headers)
print(r.text)
