from .api_request import OrangeRequest
from ..utils.loggers_helpers import log_response
import json


class BaseAPI:
    def __init__(self, base_url, header):
        self.base_url = base_url
        self.header = header

    @log_response
    def get_all(self, params=None, specific_header=None):
        final_header = specific_header if specific_header is not None else self.header
        return OrangeRequest.get(
            self.base_url,
            headers=final_header,
            params=params
        )

    @log_response
    def get_by_id(self, item_id):
        return OrangeRequest.get(
            f"{self.base_url}/{item_id}",
            headers=self.header
        )

    @log_response
    def create(self, payload):
        return OrangeRequest.post(
            self.base_url,
            headers=self.header,
            payload=json.dumps(payload)
        )

    @log_response
    def delete(self, payload):
        return OrangeRequest.delete(
            self.base_url,
            headers=self.header,
            payload=json.dumps(payload)
        )

