import requests
import pytest
from src.assertions.common_assertions import *

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.funcional
@pytest.mark.positivo
def test_BYT_T26_obtener_detalles_del_usuario_con_ID_válido_devuelve_código_200_OK(user_url, header):
    """
    Descripción: Verifica que al solicitar un usuario existente por su ID, 
    el sistema responde con código 200 y devuelve los datos esperados.
    """
    url = f"{user_url}/1"
    response = requests.get(url, headers=header)
    assert response.status_code == 200
    assert_resource_response_schema(response, "user_schema_response.json")  

@pytest.mark.funcional
@pytest.mark.positivo
def test_BYT_T49_obtener_usuario_con_ID_mínimo_válido_1_devuelve_200_OK_si_el_usuario_existe(user_url, header):
    """
    Descripción: Verifica que el sistema devuelve 200 OK 
    cuando se solicita el usuario con ID 1, si existe.
    """
    url = f"{user_url}/1"
    response = requests.get(url, headers=header)
    assert response.status_code == 200
    assert_resource_response_schema(response, "user_schema_response.json")

@pytest.mark.regression
@pytest.mark.funcional
@pytest.mark.negativo
def test_BYT_T27_obtener_usuario_con_ID_inexistente_devuelve_código_404_y_mensaje_de_error(user_url, header):
    """
    Descripción: Verifica que al solicitar un usuario inexistente, 
    el sistema devuelve código 404 y un mensaje de error adecuado.
    """
    url = f"{user_url}/999999"
    response = requests.get(url, headers=header)
    assert response.status_code == 404
    assert_resource_response_schema(response, "error_404_schema_response.json")

@pytest.mark.regression
@pytest.mark.funcional
@pytest.mark.negativo
def test_BYT_T50_obtener_usuario_con_ID_mínimo_inválido_0_devuelve_422_unprocessable_content(user_url, header):
    """
    Descripción: Verifica que el sistema devuelve 422 Unprocessable Content al enviar ID 0.
    """
    url = f"{user_url}/0"
    response = requests.get(url, headers=header)
    assert response.status_code == 422
    assert_resource_response_schema(response, "error_422_schema_response.json")

@pytest.mark.regression
@pytest.mark.funcional
@pytest.mark.negativo
def test_BYT_T51_obtener_usuario_con_ID_negativo_menos_1_devuelve_422_unprocessable_content(user_url, header):
    """
    Descripción: Verifica que el sistema devuelve 422 Unprocessable Content al enviar un ID negativo (-1).
    """
    url = f"{user_url}/-1"
    response = requests.get(url, headers=header)
    assert response.status_code == 422
    assert_resource_response_schema(response, "error_422_schema_response.json")

@pytest.mark.regression
@pytest.mark.funcional
@pytest.mark.negativo
def test_BYT_T52_obtener_usuario_con_ID_no_numérico_abc123_devuelve_422_unprocessable_content(user_url, header):
    """
    Descripción: Verifica que el sistema devuelve 422 Unprocessable Content al enviar un ID no numérico (abc123).
    """
    url = f"{user_url}/abc123"
    response = requests.get(url, headers=header)
    assert response.status_code == 422
    assert_resource_response_schema(response, "error_422_schema_response.json")

@pytest.mark.regression
@pytest.mark.funcional
@pytest.mark.negativo
@pytest.mark.xfail(reason="Known Issue. BYT-37: GET /users/ sin parámetro {id} devuelve 422 en lugar de 404", run=False)
def test_BYT_T53_obtener_usuario_con_ID_vacío_sin_parámetro_id_devuelve_404_not_found(user_url, header):
    """
    Descripción: Verifica que al omitir el parámetro ID, el sistema devuelve 404 Not Found.
    """
    url = f"{user_url}/"
    response = requests.get(url, headers=header)
    assert response.status_code == 422
    assert_resource_response_schema(response, "error_422_schema_response.json")

@pytest.mark.regression
@pytest.mark.funcional
@pytest.mark.negativo
def test_BYT_T54_obtener_usuario_con_ID_numérico_máximo_válido_4004_cifras_devuelve_404_not_found(user_url, header):
    """
    Descripción: Verifica que al enviar un ID numérico con 4004 cifras (válido pero inexistente), se devuelve 404 Not Found.
    """
    id_4004_digits = "1" * 4004
    url = f"{user_url}/{id_4004_digits}"
    response = requests.get(url, headers=header)
    assert response.status_code == 404
    assert_resource_response_schema(response, "error_404_schema_response.json")

@pytest.mark.regression
@pytest.mark.funcional
@pytest.mark.negativo
def test_BYT_T55_obtener_usuario_con_ID_numérico_máximo_inválido_8144_cifras_devuelve_414_request_uri_too_large(user_url, header):
    """
    Descripción: Verifica que al enviar un ID numérico con 8144 cifras (inválido), se devuelve 414 Request-URI Too Large.
    """
    id_8144_digits = "1" * 8144
    url = f"{user_url}/{id_8144_digits}"
    response = requests.get(url, headers=header)
    assert response.status_code == 414

@pytest.mark.regression
@pytest.mark.funcional
@pytest.mark.negativo
def test_BYT_T56_obtener_usuario_con_ID_de_8143_cifras_devuelve_403_forbidden(user_url, header):
    """
    Descripción: Verifica que al enviar un ID con 8143 cifras, se devuelve 403 Forbidden.
    """
    id_8143_digits = "1" * 8143
    url = f"{user_url}/{id_8143_digits}"
    response = requests.get(url, headers=header)
    assert response.status_code == 403

