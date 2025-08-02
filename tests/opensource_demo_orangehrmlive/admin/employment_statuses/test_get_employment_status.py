import requests
import pytest
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
    