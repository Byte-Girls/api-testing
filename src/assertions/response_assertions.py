def assert_http_status(response, expected_status):
    """
    Método para verificar el status code del request
    """
    assert response.status_code == expected_status, f"El código de estado deberi ser {expected_status} pero es {response.status_code}"
    