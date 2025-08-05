import requests
import pytest
import time
import logging
from src.assertions.common_assertions import *

logger = logging.getLogger(__name__)

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.funcional
@pytest.mark.positivo
def test_BYT_T26_obtener_detalles_del_usuario_con_ID_válido_devuelve_código_200_OK(user_url, header, user):
    """
    Descripción: Verifica que al solicitar un usuario existente por su ID, 
    el sistema responde con código 200 y devuelve los datos esperados.
    """
    user_id = user["id"]
    url = f"{user_url}/{user_id}"
    response = requests.get(url, headers=header)
    assert response.status_code == 200
    assert_resource_response_schema(response, "user_schema_response.json")
    # Logging information
    logger.info("domain: %s", user_url)
    logger.debug("request+headers: GET %s %s", user_url, header)
    logger.info("status code: %s", response.status_code)
    logger.debug("response text: %s", response.text)

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
    # Logging information
    logger.info("domain: %s", user_url)
    logger.debug("request+headers: GET %s %s", user_url, header)
    logger.info("status code: %s", response.status_code)
    logger.debug("response: %s", response.json())

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
    assert_resource_response_schema(response, "error_message_schema_response.json")
    # Logging information
    logger.info("domain: %s", user_url)
    logger.debug("request+headers: GET %s %s", user_url, header)
    logger.info("status code: %s", response.status_code)
    logger.debug("response: %s", response.json())

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
    # Logging information
    logger.info("domain: %s", user_url)
    logger.debug("request+headers: GET %s %s", user_url, header)
    logger.info("status code: %s", response.status_code)
    logger.debug("response: %s", response.json())

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
    # Logging information
    logger.info("domain: %s", user_url)
    logger.debug("request+headers: GET %s %s", user_url, header)
    logger.info("status code: %s", response.status_code)
    logger.debug("response: %s", response.json())

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
    # Logging information
    logger.info("domain: %s", user_url)
    logger.debug("request+headers: GET %s %s", user_url, header)
    logger.info("status code: %s", response.status_code)
    logger.debug("response: %s", response.json())

@pytest.mark.regression
@pytest.mark.funcional
@pytest.mark.negativo
@pytest.mark.xfail(reason="Known Issue. BYT-37: GET /users/ sin parámetro {id} devuelve 404 en lugar de 422", run=False)
def test_BYT_T53_obtener_usuario_con_ID_vacío_sin_parámetro_id_devuelve_422_unprocessable_content(user_url, header):
    """
    Descripción: Verifica que al omitir el parámetro ID, el sistema devuelve 422 Unprocessable Content.
    """
    url = f"{user_url}/"
    response = requests.get(url, headers=header)
    assert response.status_code == 422
    assert_resource_response_schema(response, "error_422_schema_response.json")
    # Logging information
    logger.info("domain: %s", user_url)
    logger.debug("request+headers: GET %s %s", user_url, header)
    logger.info("status code: %s", response.status_code)
    logger.debug("response: %s", response.json())

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
    assert_resource_response_schema(response, "error_message_schema_response.json")
    # Logging information
    logger.info("domain: %s", user_url)
    logger.debug("request+headers: GET %s %s", user_url, header)
    logger.info("status code: %s", response.status_code)
    logger.debug("response: %s", response.json())

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
    # Logging information
    logger.info("domain: %s", user_url)
    logger.debug("request+headers: GET %s %s", user_url, header)
    logger.info("status code: %s", response.status_code)
    logger.debug("response text: %s", response.text)

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
    # Logging information
    logger.info("domain: %s", user_url)
    logger.debug("request+headers: GET %s %s", user_url, header)
    logger.info("status code: %s", response.status_code)
    logger.debug("response text: %s", response.text)

@pytest.mark.regression
@pytest.mark.funcional
@pytest.mark.negativo
@pytest.mark.smoke
@pytest.mark.seguridad
def test_BYT_T28_solicitud_sin_autenticacion_devuelve_401_unauthorized(user_url, user):
    """
    Descripción: Verifica que una solicitud sin encabezado de autenticación devuelva un código 401 Unauthorized.
    """
    user_id = user["id"]
    url = f"{user_url}/{user_id}"
    response = requests.get(url)  # Sin headers
    assert response.status_code == 401
    assert_resource_response_schema(response, "error_message_schema_response.json")
    # Logging information
    logger.info("domain: %s", user_url)
    logger.debug("request: GET %s", user_url)
    logger.info("status code: %s", response.status_code)
    logger.debug("response: %s", response.json())

@pytest.mark.regression
@pytest.mark.funcional
@pytest.mark.negativo
@pytest.mark.seguridad
@pytest.mark.xfail(reason="Known Issue. BYT-49: API get user se queda estancada con token inválido — no responde ni devuelve error", run=False)
def test_BYT_T59_solicitud_con_token_invalido_devuelve_401_unauthorized(user_url, user):
    """
    Descripción: Verifica que una solicitud con un token inválido en el encabezado devuelva un código 401 Unauthorized.
    """
    invalid_header = {
        "Authorization": "Bearer token_invalido"
    }
    user_id = user["id"]
    url = f"{user_url}/{user_id}"
    response = requests.get(url, headers=invalid_header)
    assert response.status_code == 401
    assert_resource_response_schema(response, "error_message_schema_response.json")
    # Logging information
    logger.info("domain: %s", user_url)
    logger.debug("request: GET %s", user_url)
    logger.info("status code: %s", response.status_code)
    logger.debug("response: %s", response.json())

@pytest.mark.regression
@pytest.mark.funcional
@pytest.mark.smoke
@pytest.mark.positivo
def test_BYT_T29_verificar_que_el_campo_contrasena_no_se_incluya_en_respuesta(user_url, header, user):
    """
    Descripción: Verifica que el campo 'contraseña' (password) no esté presente en la respuesta al obtener los datos de un usuario.
    """
    user_id = user["id"]
    url = f"{user_url}/{user_id}"
    response = requests.get(url, headers=header)
    
    assert response.status_code == 200
    response_data = response.json()["data"]
    assert 'password' not in response_data, "El campo 'password' no debe estar presente en la respuesta del usuario"
    assert_resource_response_schema(response, "user_schema_response.json")
    # Logging information
    logger.info("domain: %s", user_url)
    logger.debug("request+headers: GET %s %s", user_url, header)
    logger.info("status code: %s", response.status_code)
    logger.debug("response: %s", response.json())

@pytest.mark.regression
@pytest.mark.funcional
def test_BYT_T57_validar_respuesta_cuando_usuario_esta_deshabilitado(user_url, header, disabled_user):
    """
    Descripción: Valida que al consultar un usuario deshabilitado, la API igualmente devuelve el usuario.
    """
    disabled_user_id = disabled_user["id"]
    url = f"{user_url}/{disabled_user_id}"
    response = requests.get(url, headers=header)
    
    assert response.status_code == 200
    response_data = response.json()["data"]
    assert response_data["status"] == False, "El campo 'enabled' debería ser False para un usuario deshabilitado"
    assert_resource_response_schema(response, "user_schema_response.json")
    # Logging information
    logger.info("domain: %s", user_url)
    logger.debug("request+headers: GET %s %s", user_url, header)
    logger.info("status code: %s", response.status_code)
    logger.debug("response: %s", response.json())

@pytest.mark.regression
@pytest.mark.rendimiento
def test_BYT_T58_tiempo_respuesta_menor_a_2_segundos(user_url, header, user):
    """
    Descripción: Verifica que la respuesta de la API al consultar un usuario sea menor a 2 segundos.
    """
    user_id = user["id"]
    url = f"{user_url}/{user_id}"
    start_time = time.time()
    response = requests.get(url, headers=header)
    end_time = time.time()
    
    response_time = end_time - start_time
    assert response.status_code == 200
    assert response_time < 2.0, f"La respuesta tardó {response_time:.2f} segundos, debe ser menor a 2 segundos"
    assert_resource_response_schema(response, "user_schema_response.json")
    # Logging information
    logger.info("domain: %s", user_url)
    logger.debug("request+headers: GET %s %s", user_url, header)
    logger.info("status code: %s", response.status_code)
    logger.debug("response: %s", response.json())

