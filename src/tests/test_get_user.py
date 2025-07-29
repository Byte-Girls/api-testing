import requests
import pytest
from src.assertions.response_assertions import *
from src.common.common_globals import *

# Obtener detalles del usuario con ID válido devuelve código 200
@pytest.mark.smoke
def test_get_user_with_valid_id_returns_code_200():
    response = requests.get(ENDPOINT_USERS, headers=HEADERS)
    assert_http_status(response, 200)
