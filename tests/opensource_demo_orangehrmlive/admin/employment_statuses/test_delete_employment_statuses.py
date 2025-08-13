import json
import random
import pytest
import requests
import string
from src.assertions.common_assertions import * 
from src.utils.loggers_helpers import log_request_response

@pytest.mark.smoke
@pytest.mark.funcional
@pytest.mark.positivo
@pytest.mark.regression
def test_BYT_T111_Eliminar_estado_existente_con_exito(statuses_url, header,employment_status_create):
    """ 
    Descripción: El Administrador quiere eliminar un estado de empleado que existe en la lista, el sistema debe permitir
    """""
    payload = json.dumps({"ids": [employment_status_create["id"]]})


    response = requests.delete(statuses_url, headers=header, data=payload)
    assert response.status_code == 200
    assert_resource_response_schema(response, "delete_employment_status_schema_response.json")
    log_request_response(statuses_url, response, header, payload)

@pytest.mark.smoke
@pytest.mark.funcional
@pytest.mark.negativo
@pytest.mark.regression
def test_BYT_T112_Eliminar_un_estado_inexistente(statuses_url, header):
    """ 
    Descripción: El Administrador quiere eliminar un estado de empleado que no existe en la lista
    """""
    payload = json.dumps({"ids": [999999999999999]})


    response = requests.delete(statuses_url, headers=header, data=payload)
    assert response.status_code == 404
    assert_resource_response_schema(response, "delete_404_status_schema_response.json")
    #log_request_response(statuses_url, response, header, payload)  

@pytest.mark.funcional
@pytest.mark.positivo
@pytest.mark.regression
def test_BYT_T166_Eliminar_varios_estados_simultaneamente(statuses_url, header, employment_status_create_multi):
    """ 
    Descripción: El Administrador quiere eliminar varios estados de empleado simultaneamente
    """""
    status_ids = [employment_status_create["id"] for employment_status_create in employment_status_create_multi]
    payload = json.dumps({"ids": status_ids})

    response = requests.delete(statuses_url, headers=header, data=payload)
    assert response.status_code == 200
    assert_resource_response_schema(response, "delete_employment_status_schema_response.json")
    log_request_response(statuses_url, response, header, payload)  

@pytest.mark.funcional
@pytest.mark.negativo
@pytest.mark.regression
def test_BYT_T168_Eliminar_estado_sin_mandar_id(statuses_url, header):
    """ 
    Descripción: El Administrador quiere eliminar un estado de empleado, pero no manda el id. el sistema no debe permitir
    """""
    payload = json.dumps({"ids": [""]})


    response = requests.delete(statuses_url, headers=header, data=payload)
    assert response.status_code == 404
    assert_resource_response_schema(response, "delete_404_status_schema_response.json")
    log_request_response(statuses_url, response, header, payload)

@pytest.mark.funcional
@pytest.mark.negativo
@pytest.mark.seguridad
@pytest.mark.regression
def test_BYT_T169_Eliminar_estado_sin_permisos_de_autenticacion(statuses_url, employment_status_create):
    """ 
    Descripción: El Administrador quiere eliminar un estado de empleado, pero no tiene permisos de autenticación
    """""
    payload = json.dumps({"ids": [employment_status_create["id"]]})
    headers_sin_auth = {
        "Content-Type": "application/json"
    }

    response = requests.delete(statuses_url, headers=headers_sin_auth, data=payload)
    assert response.status_code in [401, 403]
    log_request_response(statuses_url, response, None, payload)
    
@pytest.mark.funcional
@pytest.mark.negativo
@pytest.mark.regression
def test_BYT_T178_Eliminar_estado_mandando_id_de_letras(statuses_url, header):
    """ 
    Descripción: El Administrador quiere eliminar un estado de empleado, manda un id de letras
    """""
    payload = json.dumps({"ids": ["abc"]})


    response = requests.delete(statuses_url, headers=header, data=payload)
    assert response.status_code == 404
    assert_resource_response_schema(response, "delete_404_status_schema_response.json")
    log_request_response(statuses_url, response, header, payload)

@pytest.mark.funcional
@pytest.mark.negativo
@pytest.mark.regression
def test_BYT_T179_Eliminar_estado_con_id_de_caracteres_especiales(statuses_url, header):
    """ 
    Descripción: El Administrador quiere eliminar un estado de empleado, manda un id de caracteres especiales
    """""
    payload = json.dumps({"ids": ["%&/"]})


    response = requests.delete(statuses_url, headers=header, data=payload)
    assert response.status_code == 404
    assert_resource_response_schema(response, "delete_404_status_schema_response.json")
    log_request_response(statuses_url, response, header, payload)

@pytest.mark.funcional
@pytest.mark.negativo
@pytest.mark.regression
def test_BYT_T188_Eliminar_estado_con_id_negativo(statuses_url, header):
    """ 
    Descripción: El Administrador quiere eliminar un estado de empleado, manda un id negativo
    """""
    payload = json.dumps({"ids": [-1]})


    response = requests.delete(statuses_url, headers=header, data=payload)
    assert response.status_code == 404
    assert_resource_response_schema(response, "delete_404_status_schema_response.json")
    log_request_response(statuses_url, response, header, payload)

@pytest.mark.funcional
@pytest.mark.negativo
@pytest.mark.regression
def test_BYT_T190_Eliminar_estado_con_id_decimal(statuses_url, header):
    """ 
    Descripción: El Administrador quiere eliminar un estado de empleado, manda un id decimal
    """""
    payload = json.dumps({"ids": [1.2]})


    response = requests.delete(statuses_url, headers=header, data=payload)
    assert response.status_code == 404
    assert_resource_response_schema(response, "delete_404_status_schema_response.json")
    log_request_response(statuses_url, response, header, payload)    
    
@pytest.mark.funcional
@pytest.mark.negativo
@pytest.mark.regression
def test_BYT_T191_Intentar_eliminar_con_metodo_incorrecto(statuses_url, header, employment_status_create):
    """ 
    Descripción: El Administrador quiere eliminar un estado de empleado, se intentara eliminar un estado utilizando método get
    """""
    payload = json.dumps({"ids": [employment_status_create["id"]]})


    response = requests.get(statuses_url, headers=header, data=payload)
    assert response.status_code == 422
    log_request_response(statuses_url, response, header, payload) 
    