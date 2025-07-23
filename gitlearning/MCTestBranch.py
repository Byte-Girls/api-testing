import requests

url = "https://collectionapi.metmuseum.org/public/collection/v1/objects"

payload = {}
headers = {
  'Cookie': 'incap_ses_1720_1662004=z+b+aJI2RH1wMxE7QKveF/dLgGgAAAAAe9GPiVXraKPuGfS1sYathA==; visid_incap_1662004=Q/Qivtu9RgiQGNrtHytd6QckgGgAAAAAQUIPAAAAAAAATI5qPUOY0nqVVjYfylO8'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
