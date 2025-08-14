from src.assertions.common_assertions import assert_status_code
from src.utils.loggers_helpers import log_request_response
from src.orange_api.api_request import OrangeRequest
from faker import Faker
import pytest
import json

faker = Faker()

@pytest.fixture
def new_user_data(create_employee):
    employee_number = create_employee["empNumber"]
    return json.dumps({
        "status": True,
        "password": faker.password(),
        "username": faker.user_name(),
        "userRoleId": 1,
        "empNumber": employee_number
    })

@pytest.mark.e2e
def test_user_e2e(user_url, validation_username_url, header, new_user_data):
    username = json.loads(new_user_data)["username"]

    # 1. Validar unicidad del nombre de usuario
    validation_url_with_username = f"{validation_username_url}?userName={username}"
    username_validation_response = OrangeRequest.get(validation_url_with_username, header)
    log_request_response(user_url, username_validation_response, header)
    assert_status_code(username_validation_response, expected_status=200)

    # 2. Crear usuario
    create_response = OrangeRequest.post(user_url, headers=header, payload=new_user_data)
    log_request_response(user_url, create_response, header, payload=new_user_data)
    assert_status_code(create_response, expected_status=200)

    # 3. Obtener usuario
    user_id = create_response.json()["data"]["id"]
    user_url_with_id = f"{user_url}/{user_id}"
    get_response = OrangeRequest.get(user_url_with_id, headers=header)
    log_request_response(user_url, get_response, header)
    assert_status_code(get_response, expected_status=200)

    # 4. Eliminar usuario
    user_id_to_delete = json.dumps({"ids": [user_id]})
    delete_response = OrangeRequest.delete(user_url, headers=header, payload=user_id_to_delete)
    log_request_response(user_url, delete_response, header, payload=user_id_to_delete)
    assert_status_code(delete_response, expected_status=200)

    # 5. Verificar que ya no existe
    user_url_with_id = f"{user_url}/{user_id}"
    get_response = OrangeRequest.get(user_url_with_id, headers=header)
    log_request_response(user_url, get_response, header)
    assert_status_code(get_response, expected_status=404)

