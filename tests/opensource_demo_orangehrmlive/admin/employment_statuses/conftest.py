import pytest
import requests
import random
import string
import json
import logging
from src.assertions.common_assertions import * 
logger = logging.getLogger(__name__)

@pytest.fixture(scope="module")
def employment_tastus_create(statuses_url, header, get_url):
    
    payload = json.dumps({
        "name" : "Calani" + str(random.randint(1000, 9999))
    })

    response = requests.post(statuses_url, headers=header, data=payload)
    logger.debug("response: %s", response.json())
    assert response.status_code == 200
    yield response.json()["data"]
    delete_status(statuses_url, header, response.json()["data"]["id"])
    
    
@pytest.fixture(scope= "session")
def create_status_1_caracter(statuses_url, header):
    
    letra_un_caracter = random.choice(string.ascii_letters)
    
    payload = json.dumps({
        "name" : letra_un_caracter 
    })
    
    response = requests.post(statuses_url, headers=header, data=payload)
    assert response.status_code == 200
    assert_resource_response_schema(response, "create_employment_status_schema_response.json")
    id_nombre= response.json()["data"]["id"]
    yield response.json()
    delete_status(statuses_url, header, id_nombre)

def delete_status(statuses_url, header, id_nombre):
    payload = json.dumps({
        "ids": [id_nombre]
    })
    response = requests.delete(statuses_url, headers=header, data=payload)
    assert response.status_code == 200
    