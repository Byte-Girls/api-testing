def assert_all_users_have_username(response, expected_username):
    assert_all_users_field_equals(response, ["userName"], expected_username, field_name="username")

def assert_all_users_have_userRoleId(response, expected_role_id):
    assert_all_users_field_equals(response, ["userRole", "id"], expected_role_id, field_name="userRoleId")

def assert_all_users_have_nroEmpleado(response, expected_emp_number):
    assert_all_users_field_equals(response, ["employee", "empNumber"], expected_emp_number, field_name="nroEmpleado")

def assert_all_users_have_status(response, expected_status):
    assert_all_users_field_equals(response, ["status"], expected_status, field_name="status")

def assert_all_users_field_equals(response, field_path, expected_value, field_name=None):
    """
    Verifica que todos los usuarios tengan el valor esperado en un campo específico.

    :param response: Response de la API con la lista de usuarios.
    :param field_path: Lista de claves para acceder al campo dentro de cada usuario.
                       Ej: ["userName"], ["userRole", "id"], ["employee", "empNumber"]
    :param expected_value: Valor esperado para ese campo.
    :param field_name: Nombre amigable del campo para el mensaje de error (opcional).
    """
    users = response.json()["data"]
    assert users, "La lista de usuarios está vacía."

    def get_nested_value(user, path):
        for key in path:
            user = user[key]
        return user

    mismatched = [get_nested_value(user, field_path) for user in users if
                  get_nested_value(user, field_path) != expected_value]

    assert not mismatched, (
        f"Se encontraron usuarios con {field_name or 'campo'} distinto a '{expected_value}': {mismatched}"
    )

def assert_users_count_within_limit(response, max_users):
    """
    Verifica que la lista de usuarios no exceda el número máximo permitido.
    """
    users = response.json().get("data", [])
    assert len(users) <= max_users, f"Se esperaban como máximo {max_users} usuarios, pero se recibieron {len(users)}."

def assert_users_sorted(response, sort_order="asc", key="userName"):
    """
    Verifica que los usuarios en la respuesta estén ordenados según el campo especificado.
    """
    users = response.json().get("data", [])
    values = [user[key] for user in users]
    print("----sort_order.lower() == desc -->", sort_order.lower() == "desc")
    expected = sorted(values, reverse=(sort_order.lower() == "desc"))
    assert values == expected, (
        f"Usuarios no fueron ordenados correctamente.\n"
        f"Esperado: {expected}\n"
        f"Obtenido: {values}"
    )

def assert_user_matches_expected(actual_user, expected_user):
    assert actual_user == expected_user, (
        f"El primer usuario no coincide con el esperado.\n"
        f"Esperado: {expected_user}\n"
        f"Obtenido: {actual_user}"
    )

