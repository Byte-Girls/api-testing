import requests

url = "https://collectionapi.metmuseum.org/public/collection/v1/objects/5"

payload = {}
headers = {
  'Cookie': 'incap_ses_1723_1662004=4+gsLrQlihszhi4ovFPpF7ZjgGgAAAAAq4u0AqmKj514bDYqXljNRw==; visid_incap_1662004=pEVjDs6+R8WKGYjh+zNXt7ZjgGgAAAAAQUIPAAAAAADu6qTYiIdXUWsIXvf2lcDd'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
#prueba revisión
