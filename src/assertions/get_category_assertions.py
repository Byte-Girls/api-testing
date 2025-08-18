# Añadir assertions especificos para el recurso de get category
from src.orange_api.api_request import OrangeRequest

def assert_category_persisted(category_url, category_id, expected_name, headers, logger=None):
    """
    Valida que la categoría creada exista y coincida con el nombre esperado.
    """
    url = f"{category_url}/{category_id}"
    response = OrangeRequest.get(url, headers=headers)

    if logger:
        logger.debug("GET URL: %s", url)
        logger.info("GET status code: %s", response.status_code)
        logger.debug("GET response: %s", response.json())

    assert response.status_code == 200, f"Status esperado 200, obtenido {response.status_code}"
    data = response.json()["data"]
    assert data["name"] == expected_name, f"Nombre esperado {expected_name}, obtenido {data['name']}"

