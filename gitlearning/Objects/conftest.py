import json

import pytest
import requests

import config as conf
from src.utils.load_resources import load_payload_resource

@pytest.fixture(scope='session')
def get_url():
    return conf.BASE_URI



@pytest.fixture(scope='session')
def add_object(get_url):
    payload = json.dumps(load_payload_resource("add_object.json"))
    url = get_url + "objects"
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.post(url, headers=headers, data=payload)
    assert response.status_code == 200
    return response.json()


