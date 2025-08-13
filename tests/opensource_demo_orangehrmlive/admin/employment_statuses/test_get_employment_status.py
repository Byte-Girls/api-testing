import requests
import pytest
import string
import random
import json
from src.assertions.common_assertions import *
from src.utils.loggers_helpers import log_request_response

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
    response = requests.get(url, headers=header)
    assert response.status_code == 200
    log_request_response(statuses_url, response, header, None)
    
@pytest.mark.funcional
@pytest.mark.negativo
@pytest.mark.regression
def test_BYT_T42_obtener_informacion_de_un_estado_con_ID_de_letras(statuses_url, header):
    """
    Descripción: El Admin no debe poder obtener información de un estado de empleado si el id es de solo letras
    """
    id_invalido = ''.join(random.choices(string.ascii_letters, k=2))
    url = f"{statuses_url}/{id_invalido}"
    response = requests.get(url, headers=header)
    assert response.status_code == 422
    log_request_response(statuses_url, response, header, None)
    
@pytest.mark.funcional
@pytest.mark.seguridad
@pytest.mark.negativo
@pytest.mark.regression
def test_BYT_T43_obtener_informacion_de_un_estado_con_token_invalido(statuses_url):
    """
    Descripción: El Admin no debe poder obtener información de un estado de empleado si el el token es invalido
    """
    id_estado_empleado = random.randint(1, 999)
    url = f"{statuses_url}/{id_estado_empleado}"
    
    headers_invalidos = {
        "Authorization": "TOKEN_NO_VALIDO_123",
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers_invalidos)
    assert response.status_code == 401
    log_request_response(statuses_url, response, None, None)
    
@pytest.mark.funcional
@pytest.mark.negativo
@pytest.mark.regression
def test_BYT_T44_obtener_informacion_de_un_estado_con_caracteres_especiales(statuses_url, header):
    """
    Descripción: El admin intenta obtener un estado usando un ID que contiene solo caracteres especiales.
    El sistema debe rechazar la solicitud con un error 422.
    """
    url = f"{statuses_url}/@$"
    
    response = requests.get(url, headers=header)
    assert response.status_code == 422
    log_request_response(statuses_url, response, header, None)

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
    response = requests.get(url, headers=headers_sin_token)
    assert response.status_code == 401
    log_request_response(statuses_url, response, None, None)

@pytest.mark.funcional
@pytest.mark.negativo
@pytest.mark.regression
def test_BYT_T80_obtener_informacion_del_estado_con_id_0(statuses_url, header):
    """
    Descripción: El admin intenta obtener el estado, del id 0
    """
    url = f"{statuses_url}/0"
    
    response = requests.get(url, headers=header)
    assert response.status_code == 422
    log_request_response(statuses_url, response, header, None)

@pytest.mark.funcional
@pytest.mark.negativo
@pytest.mark.regression
def test_BYT_T81_obtener_informacion_del_estado_con_nombre_del_id(statuses_url, header):
    """
    Descripción: El admin crea un estado, y quiere obtener información del estado con el nombre del estado creado
    """
    
    payload = json.dumps({
        "name" : "Flash" + str(random.randint(1000, 9999))
    })
    nombre=payload
    
    response = requests.post(statuses_url, headers=header, data=payload)
    assert response.status_code == 200
    assert_resource_response_schema(response, "create_employment_status_schema_response.json")
    
    url = f"{statuses_url}/{nombre}"
    response = requests.get(url, headers=header)
    assert response.status_code == 422
    log_request_response(statuses_url, response, header, None)
    
@pytest.mark.funcional
@pytest.mark.negativo
@pytest.mark.regression
def test_BYT_T84_obtener_informacion_del_estado_con_ID_inexistente(statuses_url, header):
    """
    Descripción: El admin intenta obtener el estado, del id que no existe
    """
    id_inexistente = random.randint(10000, 99999)
    url = f"{statuses_url}/{id_inexistente}"
    
    response = requests.get(url, headers=header)
    assert response.status_code == 404
    assert_resource_response_schema(response, "error_message_schema_response.json")
    log_request_response(statuses_url, response, header, None)

@pytest.mark.funcional
@pytest.mark.negativo
@pytest.mark.regression
def test_BYT_T82_obtener_informacion_del_estado_sin_mandar_el_ID(statuses_url, header):
    """
    Descripción: El admin intenta obtener información del estado, sin mandar el id
    """
    url = f"{statuses_url}/"
    
    response = requests.get(url, headers=header)
    assert response.status_code == 404
    #assert_resource_response_schema(response, "error_404_schema_response.json")
    #log_request_response(statuses_url, response, header, None)
    
@pytest.mark.funcional
@pytest.mark.negativo
@pytest.mark.regression
def test_BYT_T91_obtener_informacion_del_estado_con_ID_negativos(statuses_url, header):
    """
    Descripción: El admin intenta obtener información del estado, mandando id negativo
    """
    url = f"{statuses_url}/-1"
    
    response = requests.get(url, headers=header)
    assert response.status_code == 422 
    log_request_response(statuses_url, response, header, None)
    