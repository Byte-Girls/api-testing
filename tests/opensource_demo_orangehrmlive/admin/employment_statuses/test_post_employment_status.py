import json
import random
import pytest
import requests
from src.assertions.common_assertions import * 
    
@pytest.mark.funtional_positive
@pytest.mark.regression
def test_BYT_T37_crear_un_estado_de_empleado(statuses_url, header):
    """
    Descripción: El admin debe poder crear un nuevo estado de empleado
    """
    
    payload = json.dumps({
        "name" : "Maria" + str(random.randint(1000, 9999))
    })
    
    response = requests.post(statuses_url, headers=header, data=payload)
    assert response.status_code == 200
    assert_resource_response_schema(response, "create_employment_status_schema_response.json")
    response_data = response.json()["data"]
    #comparación directa con el campo
    expected_payload_dict = json.loads(payload)
    assert response_data["name"] == expected_payload_dict["name"]
    
    #validación del get
    url = f"{statuses_url}/{response_data['id']}"
    response = requests.get(url, headers=header)
    assert response.status_code == 200
    response_data = response.json()["data"]
    # comparacion dierecta campo a campo
    assert response_data["name"] == expected_payload_dict["name"]


@pytest.mark.valor_limite
@pytest.mark.regression
def test_BYT_T40_crear_estado_con_nombre_de_51_caracteres(statuses_url, header):
    """
    Descripción: El admin debe poder crear un nuevo estado de empleado
    """
    
    payload = json.dumps({
        "name" : "Lorem Ipsum is simply dummy text of the printing an" 
    })
    
    response = requests.post(statuses_url, headers=header, data=payload)
    assert response.status_code == 422
  