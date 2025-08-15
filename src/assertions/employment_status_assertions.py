import requests

def assert_estado_no_presente_en_lista(statuses_url, status_id, header):
    """
    Verifica que el estado de empleado con el ID dado no aparezca en el listado de estados.
    """
    list_response = requests.get(statuses_url, headers=header)
    assert list_response.status_code == 200, f"Error al obtener listado: {list_response.status_code}"
    estados_list = list_response.json()["data"]
    assert all(str(u["id"]) != str(statuses_url) for u in estados_list), f"El usuario con ID {status_id} todavía aparece en el listado"
