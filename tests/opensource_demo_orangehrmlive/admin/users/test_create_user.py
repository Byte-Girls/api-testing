import json
import random
import pytest
import requests
from src.assertions.create_user_assertions import *

@pytest.mark.smoke
def test_crear_usuario_con_datos_validos(get_url, get_token):
    url = f"{get_url}/admin/users" 
    payload = json.dumps({
        "status": True,
        "password": "$435sdf35REWfs",
        "username": "carousernametest" + str(random.randint(1000, 9999)),
        "userRoleId": 1,
        "empNumber": "104"
    })
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {get_token}"
    }
    response = requests.post(url, headers=headers, data=payload)
    assert response.status_code == 200
    assert_create_user_response_schema(response)
