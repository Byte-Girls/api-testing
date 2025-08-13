import requests

def assert_user_not_exists(user_url, user_id, header):
    """
    Valida que el usuario con el ID dado no exista (retorne 404 al hacer GET).
    """
    get_response = requests.get(f"{user_url}/{user_id}", headers=header)
    assert get_response.status_code == 404, f"El usuario con ID {user_id} aún existe"
    
def assert_deleted_ids(response, expected_ids=None, unexpected_ids=None):
    """
    Valida que ciertos IDs estén presentes y otros ausentes en 'deletedIds' de la respuesta.
    """
    deleted_ids = response.json()["data"]
    if expected_ids:
        for eid in expected_ids:
            assert str(eid) in deleted_ids, f"ID esperado {eid} no está en deletedIds"

    if unexpected_ids:
        for uid in unexpected_ids:
            assert str(uid) not in deleted_ids, f"ID no esperado {uid} aparece en deletedIds"

def assert_user_not_in_list(user_url, user_id, header):
    """
    Valida que el usuario con el ID dado no aparezca en el listado de usuarios.
    """
    list_response = requests.get(user_url, headers=header)
    assert list_response.status_code == 200, f"Error al obtener listado: {list_response.status_code}"
    users_list = list_response.json()["data"]
    assert all(str(u["id"]) != str(user_id) for u in users_list), f"El usuario con ID {user_id} todavía aparece en el listado"

def assert_id_deleted_once(response, user_id):
    """
    Verifica que un ID aparezca exactamente una vez en deletedIds, sin importar el tipo (str/int).
    """
    deleted_ids = response.json()["data"]
    deleted_ids_str = [str(i) for i in deleted_ids]
    count = deleted_ids_str.count(str(user_id))
    assert count == 1, f"El ID {user_id} aparece {count} veces en deletedIds, se esperaba 1"

