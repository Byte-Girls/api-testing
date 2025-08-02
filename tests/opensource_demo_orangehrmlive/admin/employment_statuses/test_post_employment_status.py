import random
import requests
import json
import jsonschema
import pytest
from src.assertions.create_employment_status_assertions import *  
    
@pytest.mark.funtional_positive
@pytest.mark.regression
def test_BYT_T37_crear_un_estado_de_empleado(get_url, get_token):
    """
    Descripción: El admin debe poder crear un nuevo estado de empleado
    """
    
    url = f"{get_url}/admin/employment-statuses"
    expected_name = "Maria" + str(random.randint(1000, 9999))
    
    payload = json.dumps({
        "name" : expected_name
    })
    headers = {
        "Content-Type": "application/json",
        "Authorization":  f'{get_token}'
    }

    response = requests.post(url, headers=headers, data=payload)
    assert response.status_code == 200
    assert_create_employment_status_schema_response(response)
    response=response.json()["data"]
    assert response["name"] == expected_name
    
    #validación del get
    url = f"{get_url}/admin/employment-statuses/{response['id']}"

    headers = {
        "Authorization": f'{get_token}'
        }
        
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    response = response.json()["data"]
    assert response["name"] == expected_name
    