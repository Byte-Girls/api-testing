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
      