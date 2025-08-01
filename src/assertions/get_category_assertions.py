from src.utils.load_resources import load_schema_resource
import jsonschema
import pytest

def assert_get_category_response_schema(response):
    schema = load_schema_resource("get_category_schema_response.json")
    try:
        jsonschema.validate(instance=response.json(), schema=schema)
    except jsonschema.exceptions.ValitoionError  as err:
        pytest.fail(f"JSON schema no coincide. Error: {err}")
