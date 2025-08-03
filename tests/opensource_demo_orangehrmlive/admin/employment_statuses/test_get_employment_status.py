import requests
import pytest
import string
import random
from src.assertions.common_assertions import *

@pytest.mark.smoke
@pytest.mark.regression
def test_BYT_T79_obtener_informacion_de_un_estado_de_empleado(statuses_url, header):
    """
    Descripción: El Admin debe poder obtener información de un estado de empleado en específico
    """
    url = f"{statuses_url}/3"
    response = requests.get(url, headers=header)
    assert response.status_code == 200
    assert_resource_response_schema(response, "get_employment_status_schema_response.json")  

@pytest.mark.smoke
@pytest.mark.regression
def test_BYT_T42_obtener_informacion_de_un_estado_con_ID_de_letras(statuses_url, header):
    """
    Descripción: El Admin no debe poder obtener información de un estado de empleado si el id es de solo letras
    """
    id_invalido = ''.join(random.choices(string.ascii_letters, k=2))
    url = f"{statuses_url}/{id_invalido}"
    response = requests.get(url, headers=header)
    assert response.status_code == 422

@pytest.mark.smoke
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

@pytest.mark.smoke
@pytest.mark.regression
def test_BYT_T44_obtener_informacion_de_un_estado_con_caracteres_especiales(statuses_url, header):
    """
    Descripción: El admin intenta obtener un estado usando un ID que contiene solo caracteres especiales.
    El sistema debe rechazar la solicitud con un error como 400 o 404.
    """
    caracteres_especiales = ''.join(random.choices(string.punctuation, k=2))
    url = f"{statuses_url}/{caracteres_especiales}"
    
    response = requests.get(url, headers=header)
    assert response.status_code == 422
    
