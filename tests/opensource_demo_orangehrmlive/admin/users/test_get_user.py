import requests
import pytest
from src.assertions.common_assertions import *

@pytest.mark.smoke
def test_BYT_T26_obtener_detalles_del_usuario_con_ID_válido_devuelve_código_200(user_url, header):
    """
    Descripción: Verifica que al solicitar un usuario existente por su ID, el sistema responde con código 200 
    y devuelve los datos esperados.
    """
    url = f"{user_url}/1"
    response = requests.get(url, headers=header)
    assert response.status_code == 200
    assert_resource_response_schema(response, "user_schema_response.json")  

