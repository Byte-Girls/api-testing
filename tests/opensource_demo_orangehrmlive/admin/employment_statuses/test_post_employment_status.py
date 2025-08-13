import json
import random
import pytest
import requests
import string
from src.assertions.common_assertions import * 
from src.utils.loggers_helpers import log_request_response
   
@pytest.mark.funcional
@pytest.mark.positivo
@pytest.mark.smoke
@pytest.mark.regression
def test_BYT_T37_crear_un_estado_de_empleado(statuses_url, header):
    """
    Descripción: El admin debe poder crear un nuevo estado de empleado
    """
    
    payload = json.dumps({
        "name" : "Maria" + str(random.randint(1000, 9999))
    })
    
    response = requests.post(statuses_url, headers=header, data=payload)
    assert response.status_code == 200
    assert_resource_response_schema(response, "create_employment_status_schema_response.json")
    response_data = response.json()["data"]
    #comparación directa con el campo
    expected_payload_dict = json.loads(payload)
    assert response_data["name"] == expected_payload_dict["name"]
    #validación del get
    url = f"{statuses_url}/{response_data['id']}"
    response = requests.get(url, headers=header)
    assert response.status_code == 200
    response_data = response.json()["data"]
    # comparacion dierecta campo a campo
    assert response_data["name"] == expected_payload_dict["name"]
    id_nombre= response.json()["data"]["id"] 
    delete_status(statuses_url, header, id_nombre)
    # Logging informacion
    log_request_response(url, response, header, payload)

@pytest.mark.funcional
@pytest.mark.valor_limite
@pytest.mark.negativo
@pytest.mark.regression
def test_BYT_T38_crear_estado_sin_nombre(statuses_url, header):
    """
    Descripción: El admin crea un estado sin nombre, vacio, no debe permitir el sistema
    """
    
    payload = json.dumps({
        "name" : "" 
    })
    
    response = requests.post(statuses_url, headers=header, data=payload)
    assert response.status_code == 422
    log_request_response(statuses_url, response, header, payload)

  
@pytest.mark.funcional
@pytest.mark.valor_limite
@pytest.mark.negativo
@pytest.mark.regression
def test_BYT_T40_crear_estado_con_nombre_de_51_caracteres(statuses_url, header):
    """
    Descripción: El admin crea un estado de nombre que contiene 51 caractes y el sistema no debe permitir
    """
        
    payload = json.dumps({
        "name" : "Lorem Ipsum is simply dummy text of the printing an" 
    })
        
    response = requests.post(statuses_url, headers=header, data=payload)
    assert response.status_code == 422
    log_request_response(statuses_url, response, header, payload)


@pytest.mark.funcional
@pytest.mark.valor_limite
@pytest.mark.positivo
@pytest.mark.regression
def test_BYT_T47_crear_estado_con_nombre_de_1_caracteres(statuses_url, header):
    """
    Descripción: El admin crea un estado de nombre que contiene 1 caracter y el sistema si permite
    """
    letra_un_caracter = random.choice(string.ascii_letters)
    
    payload = json.dumps({
        "name" : letra_un_caracter 
    })
    
    response = requests.post(statuses_url, headers=header, data=payload)
    assert response.status_code == 200
    assert_resource_response_schema(response, "create_employment_status_schema_response.json")
    id_nombre= response.json()["data"]["id"] 
    delete_status(statuses_url, header, id_nombre)
    
    log_request_response(statuses_url, response, header, payload)
    
@pytest.mark.funcional
@pytest.mark.negativo
@pytest.mark.regression
@pytest.mark.xfail(reason="La app permite crear un estado con solo número BYT-51", run=False)
def test_BYT_T85_crear_un_estado_de_empleado_con_nombre_de_numeros(statuses_url, header):
    """
    Descripción: El admin quiere crear un nuevo estado de empleado con el campo name, de solo números
    """
    
    payload = json.dumps({
        "name" : "123" + str(random.randint(1000, 9999))
    })
    
    response = requests.post(statuses_url, headers=header, data=payload)
    assert response.status_code == 400
    assert_resource_response_schema(response, "create_employment_status_schema_response.json")
    id_nombre= response.json()["data"]["id"] 
    delete_status(statuses_url, header, id_nombre)
    
    log_request_response(statuses_url, response, header, payload)
    
@pytest.mark.funcional
@pytest.mark.negativo
@pytest.mark.regression
@pytest.mark.xfail(reason="La app permite crear un estado con solo caracteres especiales BYT-52", run=False)
def test_BYT_T86_crear_un_estado_de_empleado_con_caracteres_especiales(statuses_url, header):
    """
    Descripción: El admin quiere crear un nuevo estado de empleado con el campo name, de solo caracteres especiales
    """
    caracteres_especiales = ''.join(random.choices(string.punctuation, k=10))
    payload = json.dumps({
        "name" : caracteres_especiales
    })
    
    response = requests.post(statuses_url, headers=header, data=payload)
    assert response.status_code == 400
    assert_resource_response_schema(response, "create_employment_status_schema_response.json")
    id_nombre= response.json()["data"]["id"] 
    delete_status(statuses_url, header, id_nombre)
    
    log_request_response(statuses_url, response, header, payload)
    
@pytest.mark.funcional
@pytest.mark.valor_limite
@pytest.mark.positivo
@pytest.mark.regression
def test_BYT_T40_crear_un_estado_de_empleado_con_caracteres_de_50_caracteres(statuses_url, header):
    """
    Descripción: El admin quiere crear un nuevo estado de empleado con el campo name, de 50 caracteres especiales, el cual es el sistema debe permitir
    """
    nombre_valido = ''.join(random.choices(string.ascii_letters, k=50))

    payload = json.dumps({
        "name" : nombre_valido
    })
 
    response = requests.post(statuses_url, headers=header, data=payload)
    assert response.status_code == 200
    assert_resource_response_schema(response, "create_employment_status_schema_response.json")
    id_nombre= response.json()["data"]["id"] 
    delete_status(statuses_url, header, id_nombre)
    
    log_request_response(statuses_url, response, header, payload)
    
@pytest.mark.funcional
@pytest.mark.negativo
@pytest.mark.smoke
@pytest.mark.regression
def test_BYT_T39_crear_un_estado_de_empleado_duplicado(statuses_url, header):
    """
    Descripción: El admin quiere crear un estado de empleado duplicado, el sistema no debe permitir
    """
    nombre_duplicado = ''.join(random.choices(string.ascii_letters, k=6))
    
    payload = json.dumps({
        "name" : nombre_duplicado
    })
    
    response_one = requests.post(statuses_url, headers=header, data=payload)
    assert response_one.status_code == 200
    
    response_two = requests.post(statuses_url, headers=header, data=payload)
    assert response_two.status_code == 422
    assert_resource_response_schema(response_one, "create_employment_status_schema_response.json")
    id_nombre= response_one.json()["data"]["id"] 
    delete_status(statuses_url, header, id_nombre)
    
    log_request_response(statuses_url, response_two, header, payload)
    
@pytest.mark.funcional
@pytest.mark.seguridad
@pytest.mark.negativo
@pytest.mark.regression
def test_BYT_T39_crear_un_estado_de_empleado_sin_autenticacion(statuses_url):
    """
    Descripción: El admin quiere crear un nuevo estado de empleado, pero sin autenticación
    """
    payload = json.dumps({
        "name" : "Calani" + str(random.randint(1000, 9999))
    })
    #sin el token
    headers = {
        "Content-Type": "application/json"
    }
    
    response = requests.post(statuses_url, headers=headers, data=payload)
    assert response.status_code == 401
    log_request_response(statuses_url, response, None, payload)
    
@pytest.mark.funcional
@pytest.mark.negativo
@pytest.mark.regression
def test_BYT_T92_crear_un_estado_de_empleado_con_el_campo_name_de_espacio(statuses_url, header):
    """
    Descripción: El admin quiere crear un nuevo estado de empleado, con el campo name que solo contenga espacio
    """
    name_espacio=" "
    payload = json.dumps({
        "name" : name_espacio
    })
    
    response = requests.post(statuses_url, headers=header, data=payload)
    assert response.status_code == 422 
    log_request_response(statuses_url, response, header, payload)

def delete_status(statuses_url, header, id_nombre):
    payload = json.dumps({
        "ids": [id_nombre]
    })
    response = requests.delete(statuses_url, headers=header, data=payload)
    assert response.status_code == 200 
    