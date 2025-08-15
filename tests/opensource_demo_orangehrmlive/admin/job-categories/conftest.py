import json
from src.orange_api.api_request import OrangeRequest
import pytest
import json, requests, uuid, pytest
from faker import Faker

faker = Faker()

@pytest.fixture(scope="module")
def category(category_url, header):
  random_name = "Recursos" + str(faker.random_number(digits=5, fix_len=True))
  payload = json.dumps({
    "name": random_name
  })
  response = requests.post(category_url, headers=header,payload=payload)
  assert response.status_code == 200
  yield response.json()["data"]
  eliminar_categoria(category_url, header, response.json()["data"]["id"])


@pytest.fixture(scope="module")
def category(category_url, header):
    random_name = "Recursos" + str(faker.random_number(digits=5, fix_len=True))
    payload = json.dumps({"name": random_name})
    resp = OrangeRequest.post(category_url, headers=header, payload=payload)
    assert resp.status_code == 200
    data = resp.json()["data"]
    yield data
    eliminar_categoria(category_url, header, data["id"])

@pytest.fixture(scope="function")
def fresh_category(category_url, header):
    name = f"Recursos_{uuid.uuid4().hex[:6]}"
    payload = json.dumps({"name": name})
    resp = OrangeRequest.post(category_url, headers=header, payload=payload)
    assert resp.status_code == 200
    data = resp.json()["data"]
    yield data
    eliminar_categoria(category_url, header, data["id"])

def eliminar_categoria(category_url,header,id):
  #teardown 
  payload = json.dumps({
        "ids": [id]
  })
  response = OrangeRequest.delete(category_url, headers=header,payload=payload)
  assert response.status_code in (200, 404)


