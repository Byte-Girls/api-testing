from src.utils.load_resources import load_schema_resource
import jsonschema
import pytest

def assert_create_object_response_schema(response):
    schema = load_schema_resource("add_object_schema_response.json")
    try:
        jsonschema.validate(instance=response.json(), schema=schema)
        return True
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"JSON schema dont match {err}")
