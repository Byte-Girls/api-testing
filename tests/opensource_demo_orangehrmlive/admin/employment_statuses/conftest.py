import pytest
import requests
import json
from faker import Faker
from src.assertions.common_assertions import * 
from src.orange_api.api_request import OrangeRequest

faker = Faker()

@pytest.fixture(scope="function")
def employment_status_create(statuses_url, header):
    
    payload = json.dumps({
        "name" : "Hourly Contract" + " ".join(faker.words(nb=2))
    })

    response = OrangeRequest.post(statuses_url, headers=header, payload=payload)
    assert_status_code(response, expected_status=200)
    data = response.json()["data"]
    yield data
    delete_status(statuses_url, header, data["id"]) 
    
@pytest.fixture(scope="function")
def fresh_employment_status(statuses_url, header):
    
    payload = json.dumps({
        "name" : "On-Call Contract" + " ".join(faker.words(nb=2))
    })

    response = OrangeRequest.post(statuses_url, headers=header, payload=payload)
    assert_status_code(response, expected_status=200)
    data = response.json()["data"]
    yield data
    delete_status(statuses_url, header, data["id"]) 
 

def delete_status(statuses_url, header, id_nombre):
    payload = json.dumps({
        "ids": [id_nombre]
    })
    response = OrangeRequest.delete(statuses_url, headers=header, payload=payload)
    #assert_status_code(response, expected_status=200)

@pytest.fixture
def employment_status_create_multi(statuses_url, header):
    statuses = []
    for _ in range(6):
        payload = json.dumps({
            "name": "Reduced Hours Contract" + " ".join(faker.words(nb=2))
        })
        response = OrangeRequest.post(statuses_url, headers=header, payload=payload)
        assert_status_code(response, expected_status=200)
        statuses.append(response.json()["data"])
    yield statuses

    #Eliminar todos después de usar el fixture
    for status in statuses:
        delete_status(statuses_url, header, status["id"])

@pytest.fixture
def new_employment_status():
    return json.dumps({
        "name": "Hourly Contract" + " ".join(faker.words(nb=2))
    })
