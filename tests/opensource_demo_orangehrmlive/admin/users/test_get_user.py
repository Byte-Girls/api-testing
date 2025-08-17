import time
from src.assertions.common_assertions import *
from src.assertions.user_assertions import *

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.funcional
@pytest.mark.positivo
def test_BYT_T26_obtener_detalles_del_usuario_con_ID_válido_devuelve_código_200_OK(user_api, user):
    """
    Descripción: Verifica que al solicitar un usuario existente por su ID, 
    el sistema responde con código 200 y devuelve los datos esperados.

    Prioridad: Alta
    """
    response = user_api.get_by_id(user["id"])
    assert_status_code(response, 200)
    assert_resource_response_schema(response, "user_schema_response.json")

@pytest.mark.funcional
@pytest.mark.positivo
def test_BYT_T49_obtener_usuario_con_ID_mínimo_válido_1_devuelve_200_OK_si_el_usuario_existe(user_api):
    """
    Descripción: Verifica que el sistema devuelve 200 OK 
    cuando se solicita el usuario con ID 1, si existe.

    Prioridad: Media
    """
    response = user_api.get_by_id(1)
    assert_status_code(response, 200)
    assert_resource_response_schema(response, "user_schema_response.json")

@pytest.mark.regression
@pytest.mark.funcional
@pytest.mark.negativo
def test_BYT_T27_obtener_usuario_con_ID_inexistente_devuelve_código_404_y_mensaje_de_error(user_api):
    """
    Descripción: Verifica que al solicitar un usuario inexistente, 
    el sistema devuelve código 404 y un mensaje de error adecuado.

    Prioridad: Baja
    """
    response = user_api.get_by_id("999999")
    assert_status_code(response, 404)
    assert_resource_response_schema(response, "error_message_schema_response.json")

@pytest.mark.regression
@pytest.mark.funcional
@pytest.mark.negativo
def test_BYT_T50_obtener_usuario_con_ID_mínimo_inválido_0_devuelve_422_unprocessable_content(user_api):
    """
    Descripción: Verifica que el sistema devuelve 422 Unprocessable Content al enviar ID 0.

    Prioridad: Baja
    """
    response = user_api.get_by_id(0)
    assert_status_code(response, 422)
    assert_resource_response_schema(response, "error_422_schema_response.json")

@pytest.mark.regression
@pytest.mark.funcional
@pytest.mark.negativo
def test_BYT_T51_obtener_usuario_con_ID_negativo_menos_1_devuelve_422_unprocessable_content(user_api):
    """
    Descripción: Verifica que el sistema devuelve 422 Unprocessable Content al enviar un ID negativo (-1).

    Prioridad: Baja
    """
    response = user_api.get_by_id(-1)
    assert_status_code(response, 422)
    assert_resource_response_schema(response, "error_422_schema_response.json")

@pytest.mark.regression
@pytest.mark.funcional
@pytest.mark.negativo
def test_BYT_T52_obtener_usuario_con_ID_no_numérico_abc123_devuelve_422_unprocessable_content(user_api):
    """
    Descripción: Verifica que el sistema devuelve 422 Unprocessable Content al enviar un ID no numérico (abc123).

    Prioridad: Baja
    """
    response = user_api.get_by_id("abc123")
    assert_status_code(response, 422)
    assert_resource_response_schema(response, "error_422_schema_response.json")

@pytest.mark.regression
@pytest.mark.funcional
@pytest.mark.negativo
@pytest.mark.xfail(reason="Known Issue. BYT-37: GET /users/ sin parámetro {id} devuelve 404 en lugar de 422", run=False)
def test_BYT_T53_obtener_usuario_con_ID_vacío_sin_parámetro_id_devuelve_422_unprocessable_content(user_api):
    """
    Descripción: Verifica que al omitir el parámetro ID, el sistema devuelve 422 Unprocessable Content.

    Prioridad: Baja
    """
    response = user_api.get_by_id("")
    assert_status_code(response, 422)
    assert_resource_response_schema(response, "error_422_schema_response.json")

@pytest.mark.regression
@pytest.mark.funcional
@pytest.mark.negativo
def test_BYT_T54_obtener_usuario_con_ID_numérico_máximo_válido_4004_cifras_devuelve_404_not_found(user_api):
    """
    Descripción: Verifica que al enviar un ID numérico con 4004 cifras (válido pero inexistente), se devuelve 404 Not Found.

    Prioridad: Baja
    """
    id_4004_digits = "1" * 4004
    response = user_api.get_by_id(id_4004_digits)
    assert_status_code(response, 404)
    assert_resource_response_schema(response, "error_message_schema_response.json")

@pytest.mark.regression
@pytest.mark.funcional
@pytest.mark.negativo
def test_BYT_T55_obtener_usuario_con_ID_numérico_máximo_inválido_8144_cifras_devuelve_414_request_uri_too_large(user_api):
    """
    Descripción: Verifica que al enviar un ID numérico con 8144 cifras (inválido), se devuelve 414 Request-URI Too Large.

    Prioridad: Baja
    """
    id_8144_digits = "1" * 8144
    response = user_api.get_by_id(id_8144_digits)
    assert_status_code(response, 414)

@pytest.mark.regression
@pytest.mark.funcional
@pytest.mark.negativo
def test_BYT_T56_obtener_usuario_con_ID_de_8143_cifras_devuelve_403_forbidden(user_api):
    """
    Descripción: Verifica que al enviar un ID con 8143 cifras, se devuelve 403 Forbidden.

    Prioridad: Baja
    """
    id_8143_digits = "1" * 8143
    response = user_api.get_by_id(id_8143_digits)
    assert_status_code(response, 403)

@pytest.mark.regression
@pytest.mark.funcional
@pytest.mark.negativo
@pytest.mark.smoke
@pytest.mark.seguridad
def test_BYT_T28_solicitud_sin_autenticacion_devuelve_401_unauthorized(user_api, user):
    """
    Descripción: Verifica que una solicitud sin encabezado de autenticación devuelva un código 401 Unauthorized.

    Prioridad: Alta
    """
    user_id = user["id"]
    header_without_token = {
        'Content-Type': 'application/json',
        'Authorization': ''
    }

    response = user_api.get_by_id(user_id, specific_header=header_without_token)
    assert_status_code(response, 401)
    assert_resource_response_schema(response, "error_message_schema_response.json")

@pytest.mark.regression
@pytest.mark.funcional
@pytest.mark.negativo
@pytest.mark.seguridad
def test_BYT_T59_solicitud_con_token_invalido_devuelve_401_unauthorized(user_api, user):
    """
    Descripción: Verifica que una solicitud con un token inválido en el encabezado devuelva un código 401 Unauthorized.

    Prioridad: Media
    """
    invalid_header = {
        'Content-Type': 'application/json',
        "Authorization": "Bearer token_invalido"
    }

    user_id = user["id"]
    response = user_api.get_by_id(user_id, specific_header=invalid_header)
    assert_status_code(response, 401)
    assert_resource_response_schema(response, "error_message_schema_response.json")

@pytest.mark.regression
@pytest.mark.funcional
@pytest.mark.smoke
@pytest.mark.positivo
def test_BYT_T29_verificar_que_el_campo_contrasena_no_se_incluya_en_respuesta(user_api, user):
    """
    Descripción: Verifica que el campo 'contraseña' (password) no esté presente en la respuesta al obtener los datos de un usuario.

    Prioridad: Media
    """
    user_id = user["id"]
    response = user_api.get_by_id(user_id)
    assert_status_code(response, 200)
    assert_no_password_in_response(response)
    assert_resource_response_schema(response, "user_schema_response.json")

@pytest.mark.regression
@pytest.mark.funcional
def test_BYT_T57_validar_respuesta_cuando_usuario_esta_deshabilitado(user_api, disabled_user):
    """
    Descripción: Valida que al consultar un usuario deshabilitado, la API igualmente devuelve el usuario.

    Prioridad: Media
    """
    disabled_user_id = disabled_user["id"]
    response = user_api.get_by_id(disabled_user_id)
    assert_status_code(response, 200)
    assert_user_status(response, False)

@pytest.mark.regression
@pytest.mark.rendimiento
def test_BYT_T58_tiempo_respuesta_menor_a_2_segundos(user_api, user):
    """
    Descripción: Verifica que la respuesta de la API al consultar un usuario sea menor a 2 segundos.

    Prioridad: Media
    """
    user_id = user["id"]
    start_time = time.time()
    response = user_api.get_by_id(user_id)
    response_time = time.time()- start_time
    assert_status_code(response, 200)
    assert_response_time(response_time, max_seconds=2)
    assert_resource_response_schema(response, "user_schema_response.json")

