import json
import random
import requests
import pytest
import logging

logger = logging.getLogger(__name__)

@pytest.fixture(scope="module")
def user(user_url, header, get_url, create_employee):
    employee_number = create_employee["empNumber"]
    payload = json.dumps({
        "status": True,
        "password": "$435sdf35REWfs",
        "username": "testnewuser" + str(random.randint(1000, 9999)),
        "userRoleId": 1,
        "empNumber": employee_number
    })

    response = requests.post(user_url, headers=header, data=payload)
    logger.debug("response: %s", response.json())
    assert response.status_code == 200
    yield response.json()["data"]
    delete_user(user_url, header, response.json()["data"]["id"])

@pytest.fixture(scope="function")
def disabled_user(user_url, header, get_url, create_employee):
    employee_number = create_employee["empNumber"]
    payload = json.dumps({
        "status": False,
        "password": "$435sdf35REWfs",
        "username": "userdisabled" + str(random.randint(1000, 9999)),
        "userRoleId": 1,
        "empNumber": employee_number
    })

    response = requests.post(user_url, headers=header, data=payload)
    assert response.status_code == 200
    yield response.json()["data"]
    delete_user(user_url, header, response.json()["data"]["id"])

def delete_user(user_url, header, user_id):
    payload = json.dumps({
        "ids": [user_id]
    })

    response = requests.delete(user_url, headers=header, data=payload)
    assert response.status_code == 200

@pytest.fixture(scope="module")
def create_employee(get_url, header):
    url = f"{get_url}/pim/employees"
    payload = json.dumps({
        "lastName": "test create new employee",
        "firstName": "test"
    })

    response = requests.post(url, headers=header, data=payload)
    assert response.status_code == 200
    yield response.json()["data"]
    delete_employee(get_url, header, response.json()["data"]["empNumber"])

def delete_employee(get_url, header, employee_id):
    url = f"{get_url}/pim/employees"
    payload = json.dumps({
        "ids": [employee_id]
    })

    response = requests.delete(url, headers=header, data=payload)
    assert response.status_code == 200

