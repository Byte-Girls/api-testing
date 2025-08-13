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

