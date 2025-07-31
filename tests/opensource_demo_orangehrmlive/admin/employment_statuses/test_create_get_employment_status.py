import random
import requests
import json
import jsonschema
import pytest
from src.assertions.create_employment_status_assertions import *

@pytest.mark.smoke
@pytest.mark.regression
def test_BYT_T79_obtener_informacion_de_un_estado_de_empleado(get_url, get_token):
    "El Admin debe poder obtener información de un estado de empleado específico"
    url = f"{get_url}/admin/employment-statuses/3"

    headers = {
    "Authorization": f'{get_token}'
    }
    
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
 
 
    
@pytest.mark.funtional_positive
@pytest.mark.regression
def test_BYT_T37_crear_un_estado_de_empleado(get_url, get_token):
    "El admin debe poder crear un nuevo estado de empleado"
    url = f"{get_url}/admin/employment-statuses"

    payload = json.dumps({
        "name" : "Bolt" + str(random.randint(1000, 9999))
    })
    headers = {
        "Content-Type": "application/json",
        "Authorization":  f'{get_token}'
    }

    response = requests.post(url, headers=headers, data=payload)
    print(response.text)
    assert response.status_code == 200
    assert_create_employment_status_schema_response(response)
    