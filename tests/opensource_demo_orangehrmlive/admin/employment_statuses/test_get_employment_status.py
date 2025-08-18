import pytest
import json
from faker import Faker
from src.assertions.common_assertions import *
from src.utils.loggers_helpers import log_request_response
from src.orange_api.api_request import OrangeRequest

faker = Faker()

@pytest.mark.funcional
@pytest.mark.smoke
@pytest.mark.positivo
@pytest.mark.regression
def test_BYT_T79_obtener_informacion_de_un_estado_de_empleado(statuses_url, header,employment_status_create):
    """
    Descripción: El Admin debe poder obtener información de un estado de empleado en específico
    """
    id_status=employment_status_create["id"]
    url = f"{statuses_url}/{id_status}"
    response = OrangeRequest.get(url, headers=header)
    assert_status_code(response, expected_status=200)
    log_request_response(statuses_url, response, header)
    
@pytest.mark.funcional
@pytest.mark.negativo
@pytest.mark.regression
def test_BYT_T42_obtener_informacion_de_un_estado_con_ID_de_letras(statuses_url, header):
    """
    Descripción: El Admin no debe poder obtener información de un estado de empleado si el id es de solo letras
    """
    id_invalido = faker.lexify(text="??") 
    url = f"{statuses_url}/{id_invalido}"
    response = OrangeRequest.get(url, headers=header)
    assert_status_code(response, expected_status=422)
    log_request_response(statuses_url, response, header)
    
@pytest.mark.funcional
@pytest.mark.seguridad
@pytest.mark.negativo
@pytest.mark.regression
def test_BYT_T43_obtener_informacion_de_un_estado_con_token_invalido(statuses_url):
    """
    Descripción: El Admin no debe poder obtener información de un estado de empleado si el el token es invalido
    """
    id_estado_empleado = faker.random_int(min=1, max=999)
    url = f"{statuses_url}/{id_estado_empleado}"
    
    headers_invalidos = {
        "Authorization": "TOKEN_NO_VALIDO_123",
        "Content-Type": "application/json"
    }
    response = OrangeRequest.get(url, headers=headers_invalidos)
    assert_status_code(response, expected_status=401)
    log_request_response(statuses_url, response)
    
@pytest.mark.funcional
@pytest.mark.negativo
@pytest.mark.regression
def test_BYT_T44_obtener_informacion_de_un_estado_con_caracteres_especiales(statuses_url, header):
    """
    Descripción: El admin intenta obtener un estado usando un ID que contiene solo caracteres especiales.
    El sistema debe rechazar la solicitud con un error 422.
    """
    url = f"{statuses_url}/@$"
    
    response = OrangeRequest.get(url, headers=header)
    assert_status_code(response, expected_status=422)
    log_request_response(statuses_url, response, header)

@pytest.mark.funcional
@pytest.mark.seguridad
@pytest.mark.negativo
@pytest.mark.regression
def test_BYT_T46_obtener_informacion_del_estado_sin_token_de_autorizacion(statuses_url):
    """
    Descripción: El admin intenta obtener el estado, sin token de autorización
    """
    url = f"{statuses_url}/3"
    headers_sin_token = {
        "Content-Type": "application/json"
        # Sin 'Authorization'
    }
    response = OrangeRequest.get(url, headers=headers_sin_token)
    assert_status_code(response, expected_status=401)
    log_request_response(statuses_url, response)

@pytest.mark.funcional
@pytest.mark.negativo
@pytest.mark.regression
def test_BYT_T80_obtener_informacion_del_estado_con_id_0(statuses_url, header):
    """
    Descripción: El admin intenta obtener el estado, del id 0
    """
    url = f"{statuses_url}/0"
    
    response = OrangeRequest.get(url, headers=header)
    assert_status_code(response, expected_status=422)
    log_request_response(statuses_url, response, header)

@pytest.mark.funcional
@pytest.mark.negativo
@pytest.mark.regression
def test_BYT_T81_obtener_informacion_del_estado_con_nombre_del_id(statuses_url, header, employment_status_create):
    """
    Descripción: El admin crea un estado, y quiere obtener información del estado con el nombre del estado creado
    """
    nombre= employment_status_create["name"]
    
    url = f"{statuses_url}/{nombre}"
    response = OrangeRequest.get(url, headers=header)
    assert_status_code(response, expected_status=422)
    log_request_response(statuses_url, response, header)
    
@pytest.mark.funcional
@pytest.mark.negativo
@pytest.mark.regression
def test_BYT_T84_obtener_informacion_del_estado_con_ID_inexistente(statuses_url, header):
    """
    Descripción: El admin intenta obtener el estado, del id que no existe
    """
    id_inexistente = faker.random_int(min=10000, max=99999)
    url = f"{statuses_url}/{id_inexistente}"
    
    response = OrangeRequest.get(url, headers=header)
    assert_status_code(response, expected_status=404)
    assert_resource_response_schema(response, "error_message_schema_response.json")
    log_request_response(statuses_url, response, header)

@pytest.mark.funcional
@pytest.mark.negativo
@pytest.mark.regression
def test_BYT_T82_obtener_informacion_del_estado_sin_mandar_el_ID(statuses_url, header):
    """
    Descripción: El admin intenta obtener información del estado, sin mandar el id
    """
    url = f"{statuses_url}/"
    
    response = OrangeRequest.get(url, headers=header)
    assert_status_code(response, expected_status=404)
    #No se puede hacer el assert porque en el postman no muestra ningun html, json
    #assert_resource_response_schema(response, "error_message_schema_response.json")
    #log_request_response(statuses_url, response, header)
    
@pytest.mark.funcional
@pytest.mark.negativo
@pytest.mark.regression
def test_BYT_T91_obtener_informacion_del_estado_con_ID_negativos(statuses_url, header):
    """
    Descripción: El admin intenta obtener información del estado, mandando id negativo
    """
    url = f"{statuses_url}/-1"
    
    response = OrangeRequest.get(url, headers=header)
    assert_status_code(response, expected_status=422)
    log_request_response(statuses_url, response, header)
