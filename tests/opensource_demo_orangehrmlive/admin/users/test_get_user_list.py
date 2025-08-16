#import pytest
from src.utils.loggers_helpers import log_request_response
from src.orange_api.api_request import OrangeRequest
from src.assertions.common_assertions import *
from src.assertions.get_user_list_assertions import *

@pytest.mark.smoke
@pytest.mark.funcional
@pytest.mark.positivo
@pytest.mark.regression
def test_BYT_T141_get_users_with_exact_username(user_api, user):
    """
    Descripción: Verifica que al obtener la lista de usuarios con un filtro de username exacto
    solo se devuelvan usuarios con ese username.

    Prioridad: Alta
    """
    params = {"username": user["userName"]}
    response = user_api.get_all(params=params)
    assert_status_code(response, expected_status=200)
    assert_all_users_have_username(response, expected_username=user["userName"])

@pytest.mark.smoke
@pytest.mark.funcional
@pytest.mark.positivo
@pytest.mark.regression
@pytest.mark.xfail(reason="Known Issue. BYT-94: Búsqueda por username parcial no devuelve usuarios", run=False)
def test_BYT_T142_get_users_with_partial_username(user_api, new_user):
    """
    Descripción: Verifica que al obtener la lista de usuarios con un filtro de username parcial
    se devuelvan usuarios cuyo username contenga el valor filtrado.

    Prioridad: Alta
    """
    partial_username = new_user["userName"][:3]
    params = {"username": partial_username}
    response = user_api.get_all(params=params)
    assert_status_code(response, expected_status=200)
    assert_all_users_have_username(response, expected_username=partial_username)

@pytest.mark.smoke
@pytest.mark.funcional
@pytest.mark.positivo
@pytest.mark.regression
def test_BYT_T143_get_users_with_userRoleId_filter(user_api, new_user):
    """
    Descripción: Verifica que al obtener la lista de usuarios con un filtro de userRoleId
    se devuelvan usuarios que tengan ese rol.

    Prioridad: Alta
    """
    user_role_id = new_user["userRole"]["id"]
    params = {"userRoleId": user_role_id}
    response = user_api.get_all(params=params)
    assert_status_code(response, expected_status=200)
    assert_all_users_have_userRoleId(response, user_role_id)

@pytest.mark.smoke
@pytest.mark.funcional
@pytest.mark.positivo
@pytest.mark.regression
def test_BYT_T144_get_users_with_empNumber_filter(user_api, new_user):
    """
    Descripción: Verifica que al obtener la lista de usuarios con un filtro de empNumber
    se devuelvan usuarios con ese número de empleado.

    Prioridad: Alta
    """
    new_user_emp_number = new_user["employee"]["empNumber"]
    params = {"empNumber": new_user_emp_number}
    response = user_api.get_all(params=params)
    assert_status_code(response, expected_status=200)
    assert_all_users_have_nroEmpleado(response, new_user_emp_number)

@pytest.mark.smoke
@pytest.mark.funcional
@pytest.mark.positivo
@pytest.mark.regression
def test_BYT_T145_get_users_with_status_true(user_api):
    """
    Descripción: Verifica que al obtener la lista de usuarios con un filtro status=true
    solo se devuelvan usuarios activos.

    Prioridad: Alta
    """
    params = {"status": "true"}
    response = user_api.get_all(params=params)
    assert_status_code(response, expected_status=200)
    assert_all_users_have_status(response, True)

@pytest.mark.smoke
@pytest.mark.funcional
@pytest.mark.positivo
@pytest.mark.regression
@pytest.mark.parametrize("multiple_users", [60], indirect=True)
def test_BYT_T140_get_users_without_filters_returns_max_50(user_api,  multiple_users):
    """
    Descripción: Verifica que al obtener la lista de usuarios sin filtros
    se devuelva un código 200 y un máximo de 50 usuarios por defecto.

    Prioridad: Alta
    """
    response = user_api.get_all()
    assert_status_code(response, expected_status=200)
    assert_users_count_within_limit(response, 50)

@pytest.mark.funcional
@pytest.mark.positivo
@pytest.mark.regression
def test_BYT_T146_get_users_with_status_false(user_api, disabled_user):
    """
    Descripción: Verifica que al obtener la lista de usuarios con un filtro status=false
    solo se devuelvan usuarios inactivos.

    Prioridad: Media
    """
    params = {"status": "false"}
    response = user_api.get_all(params=params)
    assert_status_code(response, expected_status=200)
    assert_all_users_have_status(response, False)

@pytest.mark.funcional
@pytest.mark.positivo
@pytest.mark.regression
@pytest.mark.parametrize("sort_field, sort_order", [
    ("u.userName", "ASC"),
    ("u.userName", "DESC")
])
def test_BYT_T147_T148_get_users_sorted(user_api, sort_field, sort_order):
    """
    Descripción: Verifica que la lista de usuarios se devuelva ordenada según sortField y sortOrder.

    Prioridad: Media
    """
    params = {"sortField": sort_field, "sortOrder": sort_order}
    response = user_api.get_all(params=params)
    assert_status_code(response, expected_status=200)
    assert_users_sorted(response, sort_order)

@pytest.mark.funcional
@pytest.mark.positivo
@pytest.mark.regression
def test_BYT_T151_get_users_with_limit_10(user_api):
    """
    Descripción: Verifica que al usar limit=10 se devuelvan solo 10 usuarios.

    Prioridad: Media
    """
    params = {"limit": 10}
    response = user_api.get_all(params=params)
    assert_status_code(response, expected_status=200)
    assert_users_count_within_limit(response, 10)

@pytest.mark.funcional
@pytest.mark.positivo
@pytest.mark.regression
@pytest.mark.parametrize("multiple_users", [11], indirect=True)
@pytest.mark.parametrize("get_nth_user", [10], indirect=True)
def test_BYT_T154_get_users_with_offset_10(user_api, multiple_users, get_nth_user):
    """
    Descripción: Verifica que al usar offset=10 se devuelvan usuarios desde la posición 11 en adelante.

    Prioridad: Media
    """
    params = {"offset": 10}
    response = user_api.get_all(params=params)
    assert_status_code(response, expected_status=200)
    assert_user_matches_expected(response.json()["data"][0], get_nth_user)

@pytest.mark.funcional
@pytest.mark.positivo
@pytest.mark.regression
@pytest.mark.xfail(reason="Known Issue. BYT-95 Filtro de ordenamiento de usuarios no acepta variaciones en mayúsculas/minúsculas", run=False)
@pytest.mark.parametrize("sort_field, sort_order", [
    ("userName", "ASC"),
    ("userName", "DESC"),
    ("userName", "asC"),
    ("userName", "DEsC")
])
def test_BYT_T163_T164_case_sensitive_sort(user_api, sort_field, sort_order):
    """
    Descripción: Verifica que la lista de usuarios respete sensibilidad a mayúsculas/minúsculas.

    Prioridad: Media
    """
    params = {"sortField": sort_field, "sortOrder": sort_order}
    response = user_api.get_all(params=params)
    assert_status_code(response, expected_status=200)
    assert_users_sorted(response, sort_order)

@pytest.mark.funcional
@pytest.mark.negativo
@pytest.mark.regression
@pytest.mark.seguridad
def test_BYT_T34_obtener_lista_de_usuarios_sin_autenticacion_devuelve_401(user_api):
    """
    Descripción: Verifica que la obtención de usuariossin autenticación devuelva un código de estado HTTP 401 Unauthorized.

    Prioridad: Bajo
    """
    header_without_token = {
        'Content-Type': 'application/json',
        'Authorization': ''
    }

    response = user_api.get_all(specific_header=header_without_token)
    assert_status_code(response, expected_status=401)

@pytest.mark.funcional
@pytest.mark.negativo
@pytest.mark.regression
@pytest.mark.parametrize("params, expected_status", [
    ({"offset": -1}, 422),                 # BYT-T155
    ({"userRoleId": "invalido"}, 422),     # BYT-T156
    ({"status": "noBoolean"}, 422),        # BYT-T157
    ({"sortOrder": "invalid"}, 422),       # BYT-T158
    ({"sortField": "invalid"}, 422),       # BYT-T159
    ({"extraParam": "test"}, 422)          # BYT-T161
])
def test_get_users_negative_cases(user_api, params, expected_status):
    """
    Tests automatizados para casos negativos de la obtención de usuarios.
    Prioridad: Bajo
    """
    response = user_api.get_all(params=params)
    assert_status_code(response, expected_status=expected_status)
    assert_resource_response_schema(response, "error_message_schema_response.json")

@pytest.mark.funcional
@pytest.mark.negativo
@pytest.mark.regression
@pytest.mark.xfail(reason="Known Issue. BYT-97: El endpoint GET /api/v2/admin/users devuelve 200 en lugar de 422 cuando limit=0", run=False)
def test_BYT_T152_get_users_with_limit_00(user_api):
    """
    Descripción: Verifica que al usar limit=0 se devuelvan status code 422

    Prioridad: Bajo
    """
    params = {"limit": 0}
    response = user_api.get_all(params=params)
    assert_status_code(response, expected_status=422)

@pytest.mark.funcional
@pytest.mark.positivo
@pytest.mark.regression
#@pytest.mark.skip
def test_BYT_T162_get_users_when_empty(user_api, delete_all_users):
    """
    Descripción: Verifica que cuando no existen usuarios se devuelva 200 OK con lista vacía.

    Prioridad: Media
    """
    response = user_api.get_all()
    assert_status_code(response, expected_status=200)
    # Note: No se puede eliminar la cuenta del admin, as que quedara 1 al limpiar todos los users
    assert_users_count_within_limit(response, 1)

