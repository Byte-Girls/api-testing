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
def test_BYT_T101_Actualizar_un_estado_de_empleado_y_guardar_con_nombre_valido(statuses_url, header,employment_status_create):
    """ 
    Descripción: El Administrador quiere actualizar un estado de empleado ya creado, con datos válidos, el sistema debe permitir
    """""
    id_estado= employment_status_create["id"]
    url = f"{statuses_url}/{id_estado}"


    payload = json.dumps({
    "id": id_estado,
    "name" : "Uvaldez" + str(random.randint(1000, 9999))
    })

    response = requests.put(url, headers=header, data=payload)
    assert response.status_code == 200
    log_request_response(url, response, header, payload)

@pytest.mark.funcional
@pytest.mark.negativo
@pytest.mark.regression
@pytest.mark.xfail(reason="La app permite actualizar un estado con nombre de puro caracteres especiales", run=False)
def test_BYT_T102_Actualizar_un_estado_de_empleo_y_guardar_con_nombre_con_puro_caracteres_especiales(statuses_url, header,employment_status_create):
    """ 
    Descripción: El Administrador quiere actualizar un estado de empleado ya creado, con nombre de puro caracteres especiales, el sistema no debe permitir
    """""
    id_estado= employment_status_create["id"]
    url = f"{statuses_url}/{id_estado}"
    caracteres_especiales = ''.join(random.choices(string.punctuation, k=10))

    payload = json.dumps({
    "id": id_estado,
    "name" : caracteres_especiales
    })

    response = requests.put(url, headers=header, data=payload)
    assert response.status_code == 400
    assert_resource_response_schema(response, "error_message_schema_response.json") 
    log_request_response(url, response, header, payload)
    
@pytest.mark.funcional
@pytest.mark.negativo
@pytest.mark.regression
@pytest.mark.xfail(reason="La app permite actualizar un estado con nombre de puro numeros", run=False)
def test_BYT_T103_Actualizar_un_estado_de_empleo_y_guardar_con_nombre_de_puro_números(statuses_url, header,employment_status_create):
    """ 
    Descripción: El Administrador quiere actualizar un estado de empleado ya creado, con nombre de puro numeros, el sistema no debe permitir
    """""
    id_estado= employment_status_create["id"]
    url = f"{statuses_url}/{id_estado}"
    numeros = str(random.randint(1000, 9999))

    payload = json.dumps({
    "id": id_estado,
    "name" : numeros
    })

    response = requests.put(url, headers=header, data=payload)
    assert response.status_code == 400
    assert_resource_response_schema(response, "error_message_schema_response.json") 
    log_request_response(url, response, header, payload)
    
@pytest.mark.smoke
@pytest.mark.funcional
@pytest.mark.negativo
@pytest.mark.regression
def test_BYT_T104_Actualizar_un_estado_de_empleo_y_guardar_con_nombre_vacio(statuses_url, header,employment_status_create):
    """ 
    Descripción: El Administrador quiere actualizar un estado de empleado ya creado, con el campo nombre (vacio), el sistema no debe permitir
    """""
    id_estado= employment_status_create["id"]
    url = f"{statuses_url}/{id_estado}"

    payload = json.dumps({
    "id": id_estado,
    "name" : ""
    })

    response = requests.put(url, headers=header, data=payload)
    assert response.status_code == 422
    assert_resource_response_schema(response, "error_message_schema_response.json")   
    log_request_response(url, response, header, payload)
    
@pytest.mark.funcional
@pytest.mark.positivo
@pytest.mark.valor_limite
@pytest.mark.regression
def test_BYT_T105_Actualizar_un_estado_de_empleo_y_guardar_con_nombre_de_50_caracteres(statuses_url, header,employment_status_create):
    """ 
    Descripción: El Administrador quiere actualizar un estado de empleado ya creado, con el campo nombre su máximo de caracteres que es 50, el sistema debe permitir
    """""
    nombre_valido = ''.join(random.choices(string.ascii_letters, k=50))
    id_estado= employment_status_create["id"]
    url = f"{statuses_url}/{id_estado}"

    payload = json.dumps({
    "id": id_estado,
    "name" : nombre_valido
    })

    response = requests.put(url, headers=header, data=payload)
    assert response.status_code == 200
    log_request_response(url, response, header, payload)
    
@pytest.mark.funcional
@pytest.mark.positivo
@pytest.mark.valor_limite
@pytest.mark.regression
def test_BYT_T106_Actualizar_un_estado_de_empleo_y_guardar_con_nombre_de_1_caracter(statuses_url, header,employment_status_create):
    """ 
    Descripción: El Administrador quiere actualizar un estado de empleado ya creado, con el campo nombre el mínimo de caracteres que es 1, el sistema debe permitir
    """""
    letra_un_caracter = random.choice(string.ascii_letters)
    id_estado= employment_status_create["id"]
    url = f"{statuses_url}/{id_estado}"

    payload = json.dumps({
    "id": id_estado,
    "name" : letra_un_caracter
    })

    response = requests.put(url, headers=header, data=payload)
    assert response.status_code == 200
    log_request_response(url, response, header, payload)

@pytest.mark.funcional
@pytest.mark.negativo
@pytest.mark.valor_limite
@pytest.mark.regression
def test_BYT_T107_Actualizar_un_estado_de_empleo_y_guardar_con_nombre_de_51_caracteres(statuses_url, header,employment_status_create):
    """ 
    Descripción: El Administrador quiere actualizar un estado de empleado ya creado, con el campo nombre de 51 caracteres, el sistema no debe permitir ya que su máximo es de 50 caracteres
    """""
    nombre_invalido = ''.join(random.choices(string.ascii_letters, k=51))
    id_estado= employment_status_create["id"]
    url = f"{statuses_url}/{id_estado}"

    payload = json.dumps({
    "id": id_estado,
    "name" : nombre_invalido
    })

    response = requests.put(url, headers=header, data=payload)
    assert response.status_code == 422
    assert_resource_response_schema(response, "error_message_schema_response.json") 
    log_request_response(url, response, header, payload)  

@pytest.mark.funcional
@pytest.mark.negativo
@pytest.mark.regression
def test_BYT_T108_Actualizar_un_estado_de_empleo_y_guardar_con_nombre_de_solo_espacio(statuses_url, header,employment_status_create):
    """ 
    Descripción: El Administrador quiere actualizar un estado de empleado ya creado, con el campo nombre de solo (espacio), el sistema no debe permitir
    """""
    id_estado= employment_status_create["id"]
    url = f"{statuses_url}/{id_estado}"

    payload = json.dumps({
    "id": id_estado,
    "name" : "   "
    })

    response = requests.put(url, headers=header, data=payload)
    assert response.status_code == 422
    assert_resource_response_schema(response, "error_message_schema_response.json") 
    log_request_response(url, response, header, payload)

@pytest.mark.smoke
@pytest.mark.seguridad
@pytest.mark.funcional
@pytest.mark.negativo
@pytest.mark.regression
def test_BYT_T110_Actualizar_un_estado_de_empleo_sin_autenticacion(statuses_url, employment_status_create):
    """ 
    Descripción: El Administrador quiere actualizar un estado de empleado ya creado, quiere actualizar un estado sin estar autenticado, el sistema no debe permitir
    """""
    id_estado= employment_status_create["id"]
    url = f"{statuses_url}/{id_estado}"

    payload = json.dumps({
    "id": id_estado,
    "name" : "   "
    })
    headers = {
        "Content-Type": "application/json"
    }
    
    response = requests.put(url, headers=headers, data=payload)
    assert response.status_code == 401
    assert_resource_response_schema(response, "error_message_schema_response.json") 
    log_request_response(url, response, None, payload)

@pytest.mark.smoke
@pytest.mark.funcional
@pytest.mark.positivo
@pytest.mark.regression
def test_BYT_T170_Cancelar_la_actualizacion_de_un_estado(statuses_url, header, employment_status_create):
    """ 
    Descripción: El Administrador quiere actualizar un estado de empleado ya creado, pero cancela la actualización, el sistema debe permitir
    """""
    id_estado= employment_status_create["id"]
    url = f"{statuses_url}/{id_estado}"

    payload = json.dumps({
    "id": id_estado,
    "name" : "Actualizar estado"
    })
    response_get = requests.get(url, headers=header)
    assert response_get.status_code == 200
    estado_original = response_get.json()["data"]

    # Simulamos "cancelar" NO enviando PUT

    response_get2 = requests.get(url, headers=header)
    assert response_get2.status_code == 200
    estado_actual = response_get2.json()["data"]

    assert estado_actual == estado_original, "El estado cambió a pesar de cancelar la actualización" 
    log_request_response(url, response_get2, header, payload)
    