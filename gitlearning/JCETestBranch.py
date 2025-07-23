import requests

url = "https://collectionapi.metmuseum.org/public/collection/v1/departments"

payload = {}
headers = {
  'Cookie': 'incap_ses_1725_1662004=mxOjB1F/2De9GUUct27wF08ogGgAAAAA/QxtRDHdxdVyS5z6RPWGhQ==; visid_incap_1662004=R99t4J7PSEyGuAQSL4/ThYsjgGgAAAAAQUIPAAAAAABs4JPntilbdiOwf5BU6p+o'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
