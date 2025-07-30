import json
import random
import pytest
import requests
import jsonschema
from src.assertions.create_user_assertions import *

@pytest.mark.smoke
def test_crear_usuario_con_datos_validos(get_url, get_token):
    # TODO: Pendiente desarrollaar la funciones get_url, get_token
    token = ""
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/api/v2/admin/users"
    payload = json.dumps({
        "status": True,
        "password": "$435sdf35REWfs",
        "username": "carousernametest" + str(random.randint(1000, 9999)),
        "userRoleId": 1,
        "empNumber": "104"
    })
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    response = requests.post(url, headers=headers, data=payload)
    print(response.text)
    assert response.status_code == 200
    assert_create_user_response_schema(response)
