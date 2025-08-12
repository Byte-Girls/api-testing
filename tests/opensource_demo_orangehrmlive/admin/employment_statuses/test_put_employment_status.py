import json
import random
import pytest
import requests
import string
import logging
from src.assertions.common_assertions import * 
logger = logging.getLogger(__name__) # Crear instancia del logger

@pytest.mark.smoke
@pytest.mark.funcional
@pytest.mark.positivo
@pytest.mark.regression
def test_BYT_T101_Actualizar_un_estado_de_empleado_y_guardar_con_nombre_valido(statuses_url, header,employment_tastus_create):
    """ 
    Descripción: El Administrador quiere actualizar un estado de empleado ya creado, con datos válidos, el sistema debe permitir
    """""
    id_estado= employment_tastus_create["id"]
    url = f"{statuses_url}/{id_estado}"


    payload = json.dumps({
    "id": id_estado,
    "name" : "Uvaldez" + str(random.randint(1000, 9999))
    })

    response = requests.put(url, headers=header, data=payload)
    assert response.status_code == 200
    logger.info("domain: %s", statuses_url)
    logger.debug("request+headers: PUT %s %s", statuses_url, header)
    logger.info("status code: %s", response.status_code)
    logger.debug("response: %s", response.json())
    