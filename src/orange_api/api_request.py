import requests

class OrangeRequest:
    @staticmethod
    def get(url, headers):
        return requests.get(url, headers=headers)
    
    @staticmethod
    def post(url, headers, payload):
        return requests.post(url, headers=headers, data=payload)
    
    @staticmethod
    def put(url, headers, payload):
        return requests.post(url, headers=headers, data=payload)
    
    @staticmethod
    def delete(url, headers=None, data=None, json=None):
        return requests.delete(url, headers=headers, data=data, json=json)
