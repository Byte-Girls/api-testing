import json
import random
import pytest
import requests
import logging
from src.assertions.common_assertions import *

logger = logging.getLogger(__name__)

@pytest.mark.smoke
def test_BYT_T30_crear_usuario_con_datos_validos(user_url, header, create_employee):
    """
    Descripción: Verifica que la creación de un usuario con datos válidos devuelva un código de estado HTTP 200 OK.
    """
    payload = json.dumps({
        "status": True,
        "password": "$435sdf35REWfs",
        "username": "carousernametest" + str(random.randint(1000, 9999)),
        "userRoleId": 1,
        "empNumber": create_employee["empNumber"]
    })

    response = requests.post(user_url, headers=header, data=payload)
    assert response.status_code == 200
    assert_resource_response_schema(response, "user_schema_response.json")
    response_data = response.json()["data"]
    # Comparación directa campo a campo
    expected_payload_dict = json.loads(payload)
    assert expected_payload_dict["status"] == response_data["status"]
    assert expected_payload_dict["username"] == response_data["userName"]
    assert expected_payload_dict["userRoleId"] == response_data["userRole"]["id"]
    assert expected_payload_dict["empNumber"] == response_data["employee"]["empNumber"]

    # Validación con el get
    url = f"{user_url}/{response_data['id']}" 
    response = requests.get(url, headers=header)
    assert response.status_code == 200
    response_data = response.json()["data"]
    # Comparación directa campo a campo
    assert expected_payload_dict["status"] == response_data["status"]
    assert expected_payload_dict["username"] == response_data["userName"]
    assert expected_payload_dict["userRoleId"] == response_data["userRole"]["id"]
    assert expected_payload_dict["empNumber"] == response_data["employee"]["empNumber"]
    # Logging information
    logger.info("domain: %s", user_url)
    logger.debug("request+headers: GET %s %s", user_url, header)
    logger.debug("Payload enviado: %s", payload)
    logger.info("status code: %s", response.status_code)
    logger.debug("response text: %s", response.text)



