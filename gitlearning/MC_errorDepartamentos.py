import requests

url = "https://collectionapi.metmuseum.org/public/collection/v1/habitaciones"

payload = ""
headers = {
  'Cookie': 'incap_ses_1720_1662004=wcCyGGMsF2m1z4Y+QKveF4UQhGgAAAAAdYkCo4j0+7mYIvTmH2HyZQ==; visid_incap_1662004=Q/Qivtu9RgiQGNrtHytd6QckgGgAAAAAQUIPAAAAAAAATI5qPUOY0nqVVjYfylO8'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
