from src.utils.load_resources import load_schema_resource
import jsonschema
import pytest

def assert_resource_response_schema(response, schema_file_name):
    schema = load_schema_resource(schema_file_name)
    try:
        jsonschema.validate(instance=response.json(), schema=schema)
    except jsonschema.exceptions.ValitoionError  as err:
        pytest.fail(f"JSON schema no coincide. Error: {err}")

