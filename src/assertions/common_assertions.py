from src.utils.load_resources import load_schema_resource
import jsonschema
import pytest

def assert_resource_response_schema(response, schema_file_name):
    schema = load_schema_resource(schema_file_name)
    try:
        jsonschema.validate(instance=response.json(), schema=schema)
    except jsonschema.exceptions.ValitoionError  as err:
        pytest.fail(f"JSON schema no coincide. Error: {err}")


def assert_response_time(elapsed, max_seconds):
    """
    Valida que la respuesta tenga código 200 y que el tiempo de respuesta
    sea menor al máximo permitido.
    """
    assert elapsed < max_seconds, f"Tiempo de respuesta excedido: {elapsed:.3f}s (máximo {max_seconds}s)"

def assert_status_code(response, expected_status):
    """
    Verifica que el código de estado HTTP sea el esperado.
    """
    assert response.status_code == expected_status, f"Se esperaba el código {expected_status}, pero se recibió {response.status_code}"


def assert_error_message(response, expected_status, expected_message):
    """
    Verifica que el mensaje de error en la respuesta sea el esperado.
    """
    body = response.json()
    assert body.get("error", {}).get("status") == str(expected_status), f"Se esperaba el código de error {expected_status}, pero se recibió {body.get('error', {}).get('status')}"
    assert body.get("error", {}).get("message") == expected_message, f"Se esperaba el mensaje de error '{expected_message}', pero se recibió {body.get('error', {}).get('message')}"

def assert_response_time_less_than(response_time, max_time=2):
    """
    Verifica que el tiempo de respuesta sea menor que el tiempo máximo permitido.
    """
    assert response_time < max_time, f"Tiempo de respuesta excedido: {response_time:.4f} segundos"


