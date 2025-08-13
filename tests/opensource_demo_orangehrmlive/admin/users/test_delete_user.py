import json
import time
import pytest
import requests
from src.assertions.common_assertions import *
from src.assertions.user_assertions import *
from src.utils.loggers_helpers import log_request_response

@pytest.mark.smoke
@pytest.mark.funcional
@pytest.mark.positivo
@pytest.mark.regression
def test_BYT_T125_eliminar_usuario_con_id_valido(user_url, header, new_user):
    payload = json.dumps({"ids": [new_user["id"]]})
    response = requests.delete(user_url, headers=header, data=payload)
    assert response.status_code == 200
    log_request_response(user_url, response, header, payload)
    assert_resource_response_schema(response, "delete_user_schema_response.json")
    assert_user_not_exists(user_url, new_user['id'], header )
    

@pytest.mark.smoke
@pytest.mark.funcional
@pytest.mark.positivo
@pytest.mark.regression
def test_BYT_T126_eliminar_multiples_usuarios_con_ids_validos(user_url, header, create_multiple_users):
    user_ids = [new_user["id"] for new_user in create_multiple_users]
    payload = json.dumps({"ids": user_ids})
    response = requests.delete(user_url, headers=header, data=payload)
    assert response.status_code == 200
    log_request_response(user_url, response, header, payload)
    assert_resource_response_schema(response, "delete_user_schema_response.json")
    for user_id in user_ids:
        assert_user_not_exists(user_url, user_id, header )


@pytest.mark.funcional
@pytest.mark.positivo
@pytest.mark.regression
def test_BYT_T127_eliminar_ids_parcialmente_existentes(user_url, header, new_user):
    payload = json.dumps({"ids": [new_user["id"], 999999]})
    response = requests.delete(user_url, headers=header, data=payload)
    assert response.status_code == 200
    log_request_response(user_url, response, header, payload)
    assert_resource_response_schema(response, "delete_user_schema_response.json")
    assert_deleted_ids(response, expected_ids=[new_user["id"]], unexpected_ids=[999999])
    assert_user_not_exists(user_url, new_user["id"], header)

@pytest.mark.funcional
@pytest.mark.negativo
@pytest.mark.regression
@pytest.mark.seguridad
def test_BYT_T133_eliminar_sin_autenticacion_valida(user_url, header, new_user):
    payload = json.dumps({"ids": [new_user["id"]]})
    header_con_token_invalido = {'Content-Type': 'application/json', "Authorization": "Bearer invalid"}
    response = requests.delete(user_url, headers=header_con_token_invalido, data=payload)
    assert response.status_code == 401
    log_request_response(user_url, response, header, payload)
    assert_resource_response_schema(response, "error_message_schema_response.json")

@pytest.mark.funcional
@pytest.mark.positivo
@pytest.mark.regression
def test_BYT_T134_eliminar_usuario_y_confirmar_listado(user_url, header, new_user):
    payload = json.dumps({"ids": [new_user["id"]]})
    response = requests.delete(user_url, headers=header, data=payload)
    assert response.status_code == 200
    log_request_response(user_url, response, header, payload)
    assert_resource_response_schema(response, "delete_user_schema_response.json")
    assert_user_not_in_list(user_url, new_user["id"], header)

@pytest.mark.funcional
@pytest.mark.positivo
@pytest.mark.regression
def test_BYT_T135_eliminar_multiples_y_confirmar_listado(user_url, header, create_multiple_users):
    ids = [u["id"] for u in create_multiple_users]
    payload = json.dumps({"ids": ids})
    response = requests.delete(user_url, headers=header, data=payload)
    assert response.status_code == 200
    log_request_response(user_url, response, header, payload)
    assert_resource_response_schema(response, "delete_user_schema_response.json")
    for uid in ids:
        assert_user_not_in_list(user_url, uid, header)


@pytest.mark.regression
@pytest.mark.rendimiento
def test_BYT_T138_eliminar_usuario_tiempo(user_url, header, new_user):
    payload = json.dumps({"ids": [new_user["id"]]})
    start_time = time.time()
    response = requests.delete(user_url, headers=header, data=payload)
    elapsed = time.time() - start_time
    assert response.status_code == 200
    log_request_response(user_url, response, header, payload)
    assert_resource_response_schema(response, "delete_user_schema_response.json")
    assert_response_time(elapsed, 2)


@pytest.mark.regression
@pytest.mark.rendimiento
def test_BYT_T139_eliminar_5_usuarios_tiempo(user_url, header, create_multiple_users):
    ids = [u["id"] for u in create_multiple_users]
    payload = json.dumps({"ids": ids})
    start_time = time.time()
    response = requests.delete(user_url, headers=header, data=payload)
    elapsed = time.time() - start_time
    assert response.status_code == 200
    log_request_response(user_url, response, header, payload)
    assert_resource_response_schema(response, "delete_user_schema_response.json")
    assert_response_time(elapsed, 5)


@pytest.mark.funcional
@pytest.mark.negativo
@pytest.mark.regression
def test_BYT_T128_eliminar_sin_propiedad_ids(user_url, header):
    payload = json.dumps({"otherKey": [1, 2]})
    response = requests.delete(user_url, headers=header, data=payload)
    assert response.status_code == 422
    log_request_response(user_url, response, header, payload)
    assert_resource_response_schema(response, "error_message_schema_response.json")


@pytest.mark.funcional
@pytest.mark.negativo
@pytest.mark.regression
def test_BYT_T129_eliminar_body_vacio(user_url, header):
    payload = json.dumps({})
    response = requests.delete(user_url, headers=header, data=payload)
    assert response.status_code == 422
    log_request_response(user_url, response, header, payload)
    assert_resource_response_schema(response, "error_message_schema_response.json")


@pytest.mark.funcional
@pytest.mark.negativo
@pytest.mark.regression
@pytest.mark.xfail(reason="Known Issue. BYT-86: Intentar eliminar usuarios con el arrays de Ids vacio devuelve 404 en ves de 422", run=False)
def test_BYT_T130_eliminar_ids_array_vacio(user_url, header):
    payload = json.dumps({"ids": []})
    response = requests.delete(user_url, headers=header, data=payload)
    assert response.status_code == 422
    log_request_response(user_url, response, header, payload)
    assert_resource_response_schema(response, "error_message_schema_response.json")


@pytest.mark.funcional
@pytest.mark.negativo
@pytest.mark.regression
def test_BYT_T131_eliminar_id_formato_string(user_url, header):
    payload = json.dumps({"ids": ["invalid_id"]})
    response = requests.delete(user_url, headers=header, data=payload)
    assert response.status_code == 422
    log_request_response(user_url, response, header, payload)
    assert_resource_response_schema(response, "error_message_schema_response.json")


@pytest.mark.funcional
@pytest.mark.negativo
@pytest.mark.regression
def test_BYT_T132_eliminar_id_duplicado(user_url, header, new_user):
    payload = json.dumps({"ids": [new_user["id"], new_user["id"]]})
    response = requests.delete(user_url, headers=header, data=payload)
    assert response.status_code == 200
    log_request_response(user_url, response, header, payload)
    assert_resource_response_schema(response, "delete_user_schema_response.json")
    assert_id_deleted_once(response, new_user["id"])


@pytest.mark.funcional
@pytest.mark.negativo
@pytest.mark.regression
def test_BYT_T136_eliminar_mezcla_ids_validos_invalidos(user_url, header, new_user):
    payload = json.dumps({"ids": [new_user["id"], "invalid"]})
    response = requests.delete(user_url, headers=header, data=payload)
    assert response.status_code == 422
    log_request_response(user_url, response, header, payload)
    assert_resource_response_schema(response, "error_message_schema_response.json")


@pytest.mark.funcional
@pytest.mark.negativo
@pytest.mark.regression
def test_BYT_T137_eliminar_ids_null_o_undefined(user_url, header):
    payload = json.dumps({"ids": [None, "undefined"]})
    response = requests.delete(user_url, headers=header, data=payload)
    assert response.status_code == 422
    log_request_response(user_url, response, header, payload)
    assert_resource_response_schema(response, "error_message_schema_response.json")

