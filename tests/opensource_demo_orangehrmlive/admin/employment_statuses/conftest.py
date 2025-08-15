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
        "name" : "Calani" + str(random.randint(1000, 9999))
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
            "name": "estado" + str(random.randint(1000, 9999))
        })
        response = requests.post(statuses_url, headers=header, data=payload)
        assert_status_code(response, expected_status=200)
        status.append(response.json()["data"])
    return status
@pytest.fixture
def create_two_employment_status(statuses_url, header):
    status = []
    for _ in range(2):
        payload = json.dumps({
            "name": "estado" + str(random.randint(1000, 9999))
        })
        response = requests.post(statuses_url, headers=header, data=payload)
        assert_status_code(response, expected_status=200)
        status.append(response.json()["data"])
    return status

@pytest.fixture
def obtener_lista_estados(statuses_url, header):
    """Devuelve la lista completa de estados de empleado"""
    response = requests.get(statuses_url, headers=header)
    response.raise_for_status()  
    return response.json().get("data", [])
