import requests

resp = requests.get("http://127.0.0.1:5000/empdb/employee")

print("[1] Response Status Code : {} ".format(resp.status_code))  # Get the status code 200
print("[2] Check if the response is a success : {} ".format(resp.status_code == requests.codes.ok))  # check if response is success
print("[3] Get the Json response of the request sent : \n{}\n".format(resp.json()))  # Get the Content
# print("[4] Get the Text response of the request sent : \n{}\n".format(resp.text))  # Get the Content
print("[5] Get the URL that was accessed : {}".format(resp.url)) # Get the URL

# Headers
print("[6] Get the header list received in response:{}".format(resp.headers))  # get all the headers
print("[7] Get specific header(Content-Type) value: {}".format(resp.headers['Content-Type']))  # get specific header values
#
# # Get the headers of a given URL
# resp = requests.head("http://www.google.com")
# print(resp.status_code)
# print("\n", resp.headers)
#
# # Encoding
#
# print(resp.encoding)
# resp.encoding = 'utf-8'
#
# print(resp.encoding)
#
# # add custom Headers
# import json
#
# url = 'https://jsonplaceholder.typicode.com/posts'
# # payload = {'some': 'data'}
# headers = {'Content-Type': 'text/html'}
#
# # r = requests.post(url, data=json.dumps(payload), headers=headers)
# r = requests.post(url, headers=headers)
# # r = requests.post(url)
#
# print(r.headers)
# print(r.text)
#
# r = requests.post('http://httpbin.org/post')
# print(r.text)
#
# import requests, json
#
# github_url = "https://api.github.com/user/repos"
# data = json.dumps({'name': 'test1', 'description': 'Python Training Repository'})
# r = requests.post(github_url, data, auth=('ritumehra', 'ritugaurav143.'))
#
# print(r.json)