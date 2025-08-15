import pytest
import requests
import random
import json
from faker import Faker
from src.assertions.common_assertions import * 

faker = Faker()

@pytest.fixture(scope="module")
def employment_status_create(statuses_url, header):
    
    payload = json.dumps({
        "name" : "Hourly Contract" + str(random.randint(1000, 9999))
    })

    response = requests.post(statuses_url, headers=header, data=payload)
    assert_status_code(response, expected_status=200)
    yield response.json()["data"]   
    
@pytest.fixture(scope="function")
def fresh_employment_status(statuses_url, header):
    
    payload = json.dumps({
        "name" : "On-Call Contract" + str(random.randint(1000, 9999))
    })

    response = requests.post(statuses_url, headers=header, data=payload)
    assert_status_code(response, expected_status=200)
    yield response.json()["data"] 
 

def delete_status(statuses_url, header, id_nombre):
    payload = json.dumps({
        "ids": [id_nombre]
    })
    response = requests.delete(statuses_url, headers=header, data=payload)
    assert_status_code(response, expected_status=200)

@pytest.fixture
def employment_status_create_multi(statuses_url, header):
    status = []
    for _ in range(6):
        payload = json.dumps({
            "name": "Reduced Hours Contract" + str(random.randint(1000, 9999))
        })
        response = requests.post(statuses_url, headers=header, data=payload)
        assert_status_code(response, expected_status=200)
        status.append(response.json()["data"])
    return status

@pytest.fixture
def new_employment_status():
    return json.dumps({
        "name": faker.name()
    })
