import pytest
from faker import Faker
from src.assertions.common_assertions import *
from src.assertions.validate_username_assertions import *
from src.utils.loggers_helpers import log_request_response
from src.orange_api.api_request import OrangeRequest

faker = Faker()

@pytest.mark.funcional
@pytest.mark.positivo
@pytest.mark.regression
def test_BYT_T113_username_unico_sin_userid_valido(validation_username_url, header):
    """Descripción: Validar unicidad username sin userID devuelve valid=true si username no existe."""
    username = faker.user_name()
    url_with_path_params = f"{validation_username_url}?userName={username}"
    response = OrangeRequest.get(url_with_path_params, header)
    assert response.status_code == 200
    assert_resource_response_schema(response, "validation_username_schema_response.json")
    assert_valid_field(response, True)
    log_request_response(url_with_path_params, response, header)

@pytest.mark.funcional
@pytest.mark.positivo
@pytest.mark.regression
@pytest.mark.smoke
def test_BYT_T114_username_unico_con_userid_pertenece_al_mismo_usuario(validation_username_url, header, user):
    """Descripción: Validar unicidad username con userID devuelve valid=true si username pertenece al mismo usuario."""
    username = user["userName"]  
    user_id = user["id"]       
    url = f"{validation_username_url}?userName={username}&userId={user_id}"
    response = OrangeRequest.get(url, header)
    assert response.status_code == 200
    assert_resource_response_schema(response, "validation_username_schema_response.json")
    assert_valid_field(response, True)
    log_request_response(url, response, header)

@pytest.mark.funcional
@pytest.mark.positivo
@pytest.mark.regression
@pytest.mark.smoke
def test_BYT_T123_username_unico_sin_userid_valido_cloned(validation_username_url, header):
    """Descripción: Validar unicidad username sin userID devuelve valid=true si username no existe (clonado)."""
    username = faker.user_name() + "_clone"
    url = f"{validation_username_url}?userName={username}"
    response = OrangeRequest.get(url, header)
    assert response.status_code == 200
    assert_resource_response_schema(response, "validation_username_schema_response.json")
    assert_valid_field(response, True)
    log_request_response(url, response, header)

@pytest.mark.funcional
@pytest.mark.negativo
@pytest.mark.regression
@pytest.mark.seguridad
def test_BYT_T122_unicidad_sin_token_devuelve_401(validation_username_url):
    """Descripción: Validar unicidad sin token devuelve 401 unauthorized."""
    username = faker.user_name()
    url = f"{validation_username_url}?userName={username}"
    response = OrangeRequest.get(url, headers={})  # Sin token
    assert response.status_code == 401
    assert_resource_response_schema(response, "error_message_schema_response.json")
    log_request_response(url, response)

@pytest.mark.funcional
@pytest.mark.negativo
@pytest.mark.regression
@pytest.mark.seguridad
def test_BYT_T124_unicidad_con_token_invalido_devuelve_401(validation_username_url):
    """Descripción: Validar unicidad con token inválido devuelve 401 unauthorized."""
    username = faker.user_name()
    url = f"{validation_username_url}?userName={username}"
    invalid_header = {'Content-Type': 'application/json', "Authorization": "Bearer token_invalido"}
    response = OrangeRequest.get(url, invalid_header)
    assert response.status_code == 401
    assert_resource_response_schema(response, "error_message_schema_response.json")
    log_request_response(url, response)

@pytest.mark.funcional
@pytest.mark.negativo
@pytest.mark.regression
def test_BYT_T115_username_mayusculas_sensibles_devuelve_false(validation_username_url, header, user):
    """Descripción: Validar unicidad username con mayúsculas sensibles devuelve valid=false si difiere en case."""
    username_existente = user["userName"]
    username_mayus = username_existente.upper()
    url = f"{validation_username_url}?userName={username_mayus}"
    response = OrangeRequest.get(url, header)
    assert response.status_code == 200
    assert_resource_response_schema(response, "validation_username_schema_response.json")
    assert_valid_field(response, False)
    log_request_response(url, response)

@pytest.mark.funcional
@pytest.mark.negativo
@pytest.mark.regression
def test_BYT_T116_username_minusculas_sensibles_devuelve_false(validation_username_url, header, user):
    """Descripción: Validar unicidad username con minúsculas sensibles devuelve valid=false si difiere en case."""
    username_existente = user["userName"]
    username_minus = username_existente.lower()
    url = f"{validation_username_url}?userName={username_minus}"
    response = OrangeRequest.get(url, header)
    assert response.status_code == 200
    assert_resource_response_schema(response, "validation_username_schema_response.json")
    assert_valid_field(response, False)
    log_request_response(url, response)

@pytest.mark.funcional
@pytest.mark.negativo
@pytest.mark.regression
def test_BYT_T117_username_mix_mayus_minus_sensibles_devuelve_false(validation_username_url, header, user):
    """Descripción: Validar unicidad username con mix de mayúsculas/minúsculas sensibles devuelve valid=false si difiere en case."""
    username_existente = user["userName"]
    mitad = len(username_existente) // 2
    username_mix = username_existente[:mitad].lower() + username_existente[mitad:].upper()
    url = f"{validation_username_url}?userName={username_mix}"
    response = OrangeRequest.get(url, header)
    assert response.status_code == 200
    assert_resource_response_schema(response, "validation_username_schema_response.json")
    assert_valid_field(response, False)
    log_request_response(url, response)

@pytest.mark.funcional
@pytest.mark.negativo
@pytest.mark.regression
def test_BYT_T118_username_sin_userid_username_ya_existe_devuelve_false(validation_username_url, header, user):
    """Descripción: Validar unicidad username sin userID devuelve valid=false si username ya existe."""
    username_existente = user["userName"]
    url = f"{validation_username_url}?userName={username_existente}"
    response = OrangeRequest.get(url, header)
    assert response.status_code == 200
    assert_resource_response_schema(response, "validation_username_schema_response.json")
    assert_valid_field(response, False)
    log_request_response(url, response)

@pytest.mark.funcional
@pytest.mark.negativo
@pytest.mark.regression
@pytest.mark.xfail(reason="Known Issue. BYT-87: Validación de unicidad de username con userID diferente devuelve 404 en vez de 200 y no incluye campo valid en la respuesta", run=False)
def test_BYT_T119_username_con_userid_username_en_otro_usuario_devuelve_false(validation_username_url, header, user):
    """Descripción: Validar unicidad username con userID devuelve valid=false si username existe en otro usuario."""
    username_existente = user["userName"]
    otro_user_id = faker.random_number(digits=5, fix_len=True)
    url = f"{validation_username_url}?userName={username_existente}&userId={otro_user_id}"
    response = OrangeRequest.get(url, header)
    assert response.status_code == 200
    assert_resource_response_schema(response, "validation_username_schema_response.json")
    assert_valid_field(response, False)
    log_request_response(url, response)

@pytest.mark.funcional
@pytest.mark.negativo
@pytest.mark.regression
@pytest.mark.xfail(reason="Known Issue. BYT-88: Validación de username vacío devuelve status 200 en vez de 422 Unprocessable Content", run=False)
def test_BYT_T120_username_vacio_devuelve_422(validation_username_url, header):
    """Descripción: Validar unicidad con username vacío devuelve 422 Unprocessable Content."""
    url = f"{validation_username_url}?userName="
    response = OrangeRequest.get(url, header)
    assert response.status_code == 422
    assert_resource_response_schema(response, "error_message_schema_response.json")
    log_request_response(url, response)

@pytest.mark.funcional
@pytest.mark.negativo
@pytest.mark.regression
@pytest.mark.xfail(reason="Known Issue. BYT-89: Validación con userId inexistente y username vacío devuelve 501 en vez de 422 indicando falta de username", run=False)
def test_BYT_T121_username_vacio_con_userid_inexistente_devuelve_422(validation_username_url, header):
    """Descripción: Validar unicidad con userId inexistente y username vacío devuelve 422 indicando falta de username."""
    user_id_inexistente = faker.random_number(digits=5, fix_len=True)
    url = f"{validation_username_url}?userId={user_id_inexistente}"
    response = OrangeRequest.get(url, header)
    assert response.status_code == 422
    assert_resource_response_schema(response, "error_message_schema_response.json")
    log_request_response(url, response)

