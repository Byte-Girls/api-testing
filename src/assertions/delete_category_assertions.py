import requests

def assert_category_not_exists(category_url, category_id, header):
    """
    Valida que la categoría con el ID dado no exista (retorne 404 al hacer GET).
    """
    get_response = requests.get(f"{category_url}/{category_id}", headers=header)
    assert get_response.status_code == 404, f"La categoría con ID {category_id} aún existe"

def assert_deleted_category_ids(response, expected_ids=None, unexpected_ids=None):
    """
    Valida que ciertos IDs estén presentes y otros ausentes en 'data' (ids eliminados) de la respuesta.
    """
    deleted_ids = response.json()["data"]
    if expected_ids:
        for eid in expected_ids:
            assert str(eid) in deleted_ids, f"ID esperado {eid} no está en los ids eliminados"

    if unexpected_ids:
        for uid in unexpected_ids:
            assert str(uid) not in deleted_ids, f"ID no esperado {uid} aparece en los ids eliminados"


def assert_id_deleted_once(response, category_id):
    """
    Verifica que un ID aparezca exactamente una vez en 'data' (ids eliminados), sin importar el tipo (str/int).
    """
    deleted_ids = response.json()["data"]
    deleted_ids_str = [str(i) for i in deleted_ids]
    count = deleted_ids_str.count(str(category_id))
    assert count == 1, f"El ID {category_id} aparece {count} veces en los ids eliminados, se esperaba 1"

