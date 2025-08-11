import json
import random
import pytest
import requests
from src.assertions.common_assertions import *
from src.utils.loggers_helpers import log_request_response

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
    log_request_response(user_url, response, header, payload)


@pytest.mark.funcional
@pytest.mark.xfail(reason="Known Issue. BYT-80: Intentar crear un usuario con nombre duplicado devuelve 422 en ves de 409", run=False)
def test_BYT_T33_crear_usuario_username_existente_devuelve_409(user_url, header, create_employee, user):
    """
    Descripción: Verifica que la creación de un usuario con username duplicado/existente devuelva un código de estado HTTP 409 Conflict.
    """
    existing_user = user
    payload = json.dumps({
        "status": True,
        "password": "$435sdf35REWfs",
        "username": existing_user["userName"],
        "userRoleId": 1,
        "empNumber": create_employee["empNumber"]
    })
    response = requests.post(user_url, headers=header, data=payload)
    assert response.status_code == 409
    log_request_response(user_url, response, header, payload)

@pytest.mark.smoke
def test_BYT_T34_crear_usuario_sin_autenticacion_devuelve_401(user_url):
    """
    Descripción: Verifica que la creación de un usuario sin autenticación devuelva un código de estado HTTP 401 Unauthorized.
    """
    payload = json.dumps({
        "status": True,
        "password": "$435sdf35REWfs",
        "username": "user" + str(random.randint(1000, 9999)),
        "userRoleId": 1,
        "empNumber": "EMP001"
    })
    response = requests.post(user_url, data=payload)
    assert response.status_code == 401
    log_request_response(user_url, response, None, payload)

@pytest.mark.funcional
@pytest.mark.xfail(reason="Known Issue. BYT-81: Intentar crear un usuario con un rol Id inexistente devuelve 500 en ves de 422", run=False)
def test_BYT_T61_crear_usuario_con_userRoleId_inexistente_devuelve_422(user_url, header, create_employee):
    """
    Descripción: Verifica que la creación de un usuario con userRole ID inexistente devuelva un código de estado HTTP 422 Unprocessable Content.
    """
    payload = json.dumps({
        "status": True,
        "password": "$435sdf35REWfs",
        "username": "user" + str(random.randint(1000, 9999)),
        "userRoleId": 9999,
        "empNumber": create_employee["empNumber"]
    })
    response = requests.post(user_url, headers=header, data=payload)
    assert response.status_code == 422
    log_request_response(user_url, response, header, payload)

@pytest.mark.funcional
def test_BYT_T62_crear_usuario_con_empNumber_inexistente_devuelve_422(user_url, header):
    """
    Descripción: Verifica que la creación de un usuario con numero de empleado inexistente devuelva un código de estado HTTP 422 Unprocessable Content.
    """
    payload = json.dumps({
        "status": True,
        "password": "$435sdf35REWfs",
        "username": "user" + str(random.randint(1000, 9999)),
        "userRoleId": 1,
        "empNumber": "999999"
    })
    response = requests.post(user_url, headers=header, data=payload)
    assert response.status_code == 422
    log_request_response(user_url, response, header, payload)

@pytest.mark.smoke
def test_BYT_T63_crear_usuario_sin_username_devuelve_422(user_url, header, create_employee):
    """
    Descripción: Verifica que la creación de un usuario sin username devuelva un código de estado HTTP 422 Unprocessable Content.
    """
    payload = json.dumps({
        "status": True,
        "password": "$435sdf35REWfs",
        "userRoleId": 1,
        "empNumber": create_employee["empNumber"]
    })
    response = requests.post(user_url, headers=header, data=payload)
    assert response.status_code == 422
    log_request_response(user_url, response, header, payload)

@pytest.mark.funcional
def test_BYT_T64_crear_usuario_sin_password_devuelve_422(user_url, header, create_employee):
    """
    Descripción: Verifica que la creación de un usuario sin password devuelva un código de estado HTTP 422 Unprocessable Content.
    """
    payload = json.dumps({
        "status": True,
        "username": "user" + str(random.randint(1000, 9999)),
        "userRoleId": 1,
        "empNumber": create_employee["empNumber"]
    })
    response = requests.post(user_url, headers=header, data=payload)
    assert response.status_code == 422
    log_request_response(user_url, response, header, payload)

@pytest.mark.smoke
def test_BYT_T65_crear_usuario_sin_userRoleId_devuelve_422(user_url, header, create_employee):
    """
    Descripción: Verifica que la creación de un usuario sin userRole ID devuelva un código de estado HTTP 422 Unprocessable Content.
    """
    payload = json.dumps({
        "status": True,
        "username": "user" + str(random.randint(1000, 9999)),
        "password": "$435sdf35REWfs",
        "empNumber": create_employee["empNumber"]
    })
    response = requests.post(user_url, headers=header, data=payload)
    assert response.status_code == 422
    log_request_response(user_url, response, header, payload)

@pytest.mark.funcional
def test_BYT_T66_crear_usuario_sin_empNumber_devuelve_422(user_url, header):
    """
    Descripción: Verifica que la creación de un usuario sin numero de empleado devuelva un código de estado HTTP 422 Unprocessable Content.
    """
    payload = json.dumps({
        "status": True,
        "username": "user" + str(random.randint(1000, 9999)),
        "password": "$435sdf35REWfs",
        "userRoleId": 1
    })
    response = requests.post(user_url, headers=header, data=payload)
    assert response.status_code == 422
    log_request_response(user_url, response, header, payload)

@pytest.mark.funcional
def test_BYT_T67_crear_usuario_username_menor_5_caracteres_devuelve_422(user_url, header, create_employee):
    """
    Descripción: Verifica que la creación de un usuario con username menos a 5 caracteres devuelva un código de estado HTTP 422 Unprocessable Content.
    """
    payload = json.dumps({
        "status": True,
        "password": "$435sdf35REWfs",
        "username": "usr",
        "userRoleId": 1,
        "empNumber": create_employee["empNumber"]
    })
    response = requests.post(user_url, headers=header, data=payload)
    assert response.status_code == 422
    log_request_response(user_url, response, header, payload)

@pytest.mark.funcional
def test_BYT_T68_crear_usuario_username_mayor_40_caracteres_devuelve_422(user_url, header, create_employee):
    """
    Descripción: Verifica que la creación de un usuario con username mayor a 40 caracteres devuelva un código de estado HTTP 422 Unprocessable Content.
    """
    payload = json.dumps({
        "status": True,
        "password": "$435sdf35REWfs",
        "username": "u" * 41,
        "userRoleId": 1,
        "empNumber": create_employee["empNumber"]
    })
    response = requests.post(user_url, headers=header, data=payload)
    assert response.status_code == 422
    log_request_response(user_url, response, header, payload)

@pytest.mark.funcional
def test_BYT_T69_crear_usuario_con_campo_no_permitido_devuelve_422(user_url, header, create_employee):
    """
    Descripción: Verifica que la creación de un usuario con useraname invalido por ejemplo numeros o valores booleanos
    devuelva un código de estado HTTP 422 Unprocessable Content.
    """
    payload = json.dumps({
        "status": True,
        "password": "$435sdf35REWfs",
        "username": "user" + str(random.randint(1000, 9999)),
        "userRoleId": 1,
        "empNumber": create_employee["empNumber"],
        "extraField": "notAllowed"
    })
    response = requests.post(user_url, headers=header, data=payload)
    assert response.status_code == 422
    log_request_response(user_url, response, header, payload)

@pytest.mark.funcional
def test_BYT_T70_crear_usuario_status_no_booleano_devuelve_422(user_url, header, create_employee):
    """
    Descripción: Verifica que la creación de un usuario con status diffente a un valor booleano
    devuelva un código de estado HTTP 422 Unprocessable Content.
    """
    payload = json.dumps({
        "status": "yes",
        "password": "$435sdf35REWfs",
        "username": "user" + str(random.randint(1000, 9999)),
        "userRoleId": 1,
        "empNumber": create_employee["empNumber"]
    })
    response = requests.post(user_url, headers=header, data=payload)
    assert response.status_code == 422
    log_request_response(user_url, response, header, payload)

@pytest.mark.funcional
def test_BYT_T71_crear_usuario_username_con_espacios_devuelve_200(user_url, header, create_employee):
    """
    Descripción: Verifica que la creación de un usuario con username que contiene espacios devuelve 200 OK.
    """
    payload = json.dumps({
        "status": True,
        "password": "$435sdf35REWfs",
        "username": "user test " + str(random.randint(1000, 9999)),
        "userRoleId": 1,
        "empNumber": create_employee["empNumber"]
    })

    # POST
    response = requests.post(user_url, headers=header, data=payload)
    assert response.status_code == 200
    assert_resource_response_schema(response, "user_schema_response.json")

    response_data = response.json()["data"]
    expected_payload_dict = json.loads(payload)

    # Comparación campo a campo
    assert expected_payload_dict["status"] == response_data["status"]
    assert expected_payload_dict["username"] == response_data["userName"]
    assert expected_payload_dict["userRoleId"] == response_data["userRole"]["id"]
    assert expected_payload_dict["empNumber"] == response_data["employee"]["empNumber"]

    # GET para validar persistencia
    url = f"{user_url}/{response_data['id']}"
    response = requests.get(url, headers=header)
    assert response.status_code == 200
    response_data = response.json()["data"]
    assert expected_payload_dict["status"] == response_data["status"]
    assert expected_payload_dict["username"] == response_data["userName"]
    assert expected_payload_dict["userRoleId"] == response_data["userRole"]["id"]
    assert expected_payload_dict["empNumber"] == response_data["employee"]["empNumber"]

    log_request_response(user_url, response, header, payload)


@pytest.mark.funcional
def test_BYT_T73_crear_usuario_username_mayusculas_devuelve_200(user_url, header, create_employee):
    """
    Descripción: Verifica que la creación de un usuario con username en mayúsculas devuelve 200 OK.
    """
    payload = json.dumps({
        "status": True,
        "password": "$435sdf35REWfs",
        "username": "USER" + str(random.randint(1000, 9999)),
        "userRoleId": 1,
        "empNumber": create_employee["empNumber"]
    })

    # POST
    response = requests.post(user_url, headers=header, data=payload)
    assert response.status_code == 200
    assert_resource_response_schema(response, "user_schema_response.json")

    response_data = response.json()["data"]
    expected_payload_dict = json.loads(payload)

    # Comparación campo a campo
    assert expected_payload_dict["status"] == response_data["status"]
    assert expected_payload_dict["username"] == response_data["userName"]
    assert expected_payload_dict["userRoleId"] == response_data["userRole"]["id"]
    assert expected_payload_dict["empNumber"] == response_data["employee"]["empNumber"]

    # GET para validar persistencia
    url = f"{user_url}/{response_data['id']}"
    response = requests.get(url, headers=header)
    assert response.status_code == 200
    response_data = response.json()["data"]
    assert expected_payload_dict["status"] == response_data["status"]
    assert expected_payload_dict["username"] == response_data["userName"]
    assert expected_payload_dict["userRoleId"] == response_data["userRole"]["id"]
    assert expected_payload_dict["empNumber"] == response_data["employee"]["empNumber"]

    log_request_response(user_url, response, header, payload)

@pytest.mark.funcional
def test_BYT_T74_crear_usuario_sin_status_devuelve_422(user_url, header, create_employee):
    """
    Descripción: Verifica que la creación de un usuario sin status
    devuelva un código de estado HTTP 422 Unprocessable Content.
    """
    payload = json.dumps({
        "password": "$435sdf35REWfs",
        "username": "user" + str(random.randint(1000, 9999)),
        "userRoleId": 1,
        "empNumber": create_employee["empNumber"]
    })
    response = requests.post(user_url, headers=header, data=payload)
    assert response.status_code == 422
    log_request_response(user_url, response, header, payload)

@pytest.mark.funcional
def test_BYT_T75_crear_usuario_empNumber_vacio_devuelve_422(user_url, header):
    """
    Descripción: Verifica que la creación de un usuario con numero de empleado vacio ""
    devuelva un código de estado HTTP 422 Unprocessable Content.
    """
    payload = json.dumps({
        "status": True,
        "password": "$435sdf35REWfs",
        "username": "user" + str(random.randint(1000, 9999)),
        "userRoleId": 1,
        "empNumber": ""
    })
    response = requests.post(user_url, headers=header, data=payload)
    assert response.status_code == 422
    log_request_response(user_url, response, header, payload)

@pytest.mark.funcional
def test_BYT_T76_crear_usuario_userRoleId_vacio_devuelve_422(user_url, header, create_employee):
    """
    Descripción: Verifica que la creación de un usuario con userRole Id vacio ""
    devuelva un código de estado HTTP 422 Unprocessable Content.
    """
    payload = json.dumps({
        "status": True,
        "password": "$435sdf35REWfs",
        "username": "user" + str(random.randint(1000, 9999)),
        "userRoleId": "",
        "empNumber": create_employee["empNumber"]
    })
    response = requests.post(user_url, headers=header, data=payload)
    assert response.status_code == 422
    log_request_response(user_url, response, header, payload)

@pytest.mark.funcional
def test_BYT_T77_crear_usuario_password_invalido_devuelve_422(user_url, header, create_employee):
    """
    Descripción: Verifica que la creación de un usuario con password invalido 
    que no cumple con las caracteristicas minimas por ejemplo tamaño minimo 7 caracteres
    devuelva un código de estado HTTP 422 Unprocessable Content.
    """
    payload = json.dumps({
        "status": True,
        "password": "short",
        "username": "user" + str(random.randint(1000, 9999)),
        "userRoleId": 1,
        "empNumber": create_employee["empNumber"]
    })
    response = requests.post(user_url, headers=header, data=payload)
    assert response.status_code == 422
    log_request_response(user_url, response, header, payload)

@pytest.mark.funcional
def test_BYT_T78_crear_usuario_payload_vacio_devuelve_422(user_url, header):
    """
    Descripción: Verifica que la creación de un usuario con body vacio {}
    devuelva un código de estado HTTP 422 Unprocessable Content.
    """
    payload = json.dumps({})
    response = requests.post(user_url, headers=header, data=payload)
    assert response.status_code == 422
    log_request_response(user_url, response, header, payload)


