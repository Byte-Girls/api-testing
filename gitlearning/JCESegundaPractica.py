import requests

url = "https://jsonplaceholder.typicode.com/posts/999999"

payload = ""
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
