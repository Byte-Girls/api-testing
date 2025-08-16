def create_and_cleanup(api, payload, id_key):
    """Función auxiliar para crear un recurso, cederlo y eliminarlo posteriormente."""
    response = api.create(payload)
    assert response.status_code == 200
    data = response.json()["data"]
    yield data
    api.delete({"ids": [data[id_key]]})

