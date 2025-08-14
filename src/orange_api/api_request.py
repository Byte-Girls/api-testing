import requests

class OrangeRequest:
    @staticmethod
    def get(url, headers, params=None):
        return requests.get(url, headers=headers, params=params)
    
    @staticmethod
    def post(url, headers, payload):
        return requests.post(url, headers=headers, data=payload)
    
    @staticmethod
    def put(url, headers, payload):
        return requests.post(url, headers=headers, data=payload)
    
    @staticmethod
    def delete(url, headers, payload):
        return requests.delete(url, headers=headers, data=payload)
    
    