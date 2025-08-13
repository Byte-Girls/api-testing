import requests

def assert_updated_category(category_url, category_id, updated_name, header):
    """
    Verifica que la categoría actualizada tenga el ID correcto y el nombre actualizado.
    """
    url = f"{category_url}/{category_id}"
    response = requests.get(url, headers=header)

    assert response.json()["data"]["id"] == category_id, f"Se esperaba el ID {category_id}, pero se recibió {response.json()['data']['id']}"
    assert response.json()["data"]["name"] == updated_name, f"Se esperaba el nombre {updated_name}, pero se recibió {response.json()['data']['name']}"


def assert_invalid_token(response):
    """
    Verifica que el token inválido cause un error de autenticación (HTTP 401 Unauthorized).
    """
    body = response.json()
    assert response.status_code == 401, f"Se esperaba el código 401, pero se recibió {response.status_code}"
    assert "error" in body, "No se recibió el error esperado en la respuesta."
    assert "message" in body["error"], "No se recibió el mensaje de error esperado."
    
    # Hacer la validación más flexible, aceptando múltiples mensajes de error
    expected_messages = ["Unexpected error occurred while evaluating the `Bearer` token", "Session expired"]
    
    # Verifica que el mensaje esté dentro de los posibles errores
    assert body["error"]["message"] in expected_messages, \
        f"Se esperaba uno de los mensajes {expected_messages}, pero se recibió {body['error']['message']}"
