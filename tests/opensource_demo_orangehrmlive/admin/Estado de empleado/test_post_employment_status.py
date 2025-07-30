import requests
import json
import jsonschema
import pytest


@pytest.mark.smoke
@pytest.mark.regression

def test_001_obtener_la_lista_de_estado_de_empleado():
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/api/v2/admin/employment-statuses"

    payload = {}
    headers = {
    'Authorization': '••••••'
    }
    
    response = requests.request("GET", url, headers=headers, data=payload)
    assert response.status_code == 200
 
 
    
@pytest.mark.funtional_positive
@pytest.mark.regression

def test_002_crear_un_estado_de_empleado():
    
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/api/v2/admin/employment-statuses"

    payload = json.dumps({
    "name": "Cielo"
    })
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer def502001f64fdfdc63165f8f62269dba1e133d0727e6ef8c84b9ce32ca18ee0a9f05f7f63f3704af82ed481dcf76956ea382fabf8b66a5668e94d190071d6d1d2e1eed28ac86645eb6d4b0900efcf6e5da9e9dfd87527a2b2da77019089b3be8a2cc8a8f9ff073f8a64933cc54967ce440462c01142766f071771d19fcd37015cb6de198df5be6ed000fd6ef1408f32641769d8746d3539cd52c8b53c3ea442fafafce0'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    assert response.status_code == 200
    schema = {
        "type": "object",
        "required": [
            "name"
        ],
        "properties": {
            "name": {
            "type": "string"
            }
        }
    }
    try:
        jsonschema.validate(instance=response.json(), schema=schema)
        assert_crear_estado_response_schema(response)
    except jsonschema.exceptions.validationError as err:
        pytest.fail(f"JSON schema dont match {err}")