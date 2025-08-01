import random
import requests
import json
import jsonschema
import pytest
from src.assertions.get_employment_status_assertions import *

@pytest.mark.smoke
@pytest.mark.regression
def test_BYT_T79_obtener_informacion_de_un_estado_de_empleado(get_url, get_token):
    """
    Descripción: El Admin debe poder obtener información de un estado de empleado en específico
    """
    url = f"{get_url}/admin/employment-statuses/3"
    
    response =requests.get(url)
    headers = {
    "Authorization": f'{get_token}'
    }
    
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    assert_get_employment_status_schema_response(response)
    