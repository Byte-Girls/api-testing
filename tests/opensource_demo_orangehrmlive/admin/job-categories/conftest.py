
from email import header
import json
import random
import requests
import pytest
import json, requests, uuid, pytest


@pytest.fixture(scope="module")
def category(category_url, header):
  random_name = "Recursos" + str(random.randint(1000, 9999))
  payload = json.dumps({
    "name": random_name
  })
  response = requests.post(category_url, headers=header,data=payload)
  assert response.status_code == 200
  yield response.json()["data"]
  eliminar_categoria(category_url, header, response.json()["data"]["id"])


@pytest.fixture(scope="module")
def category(category_url, header):
    random_name = "Recursos" + str(random.randint(1000, 9999))
    payload = json.dumps({"name": random_name})
    resp = requests.post(category_url, headers=header, data=payload)
    assert resp.status_code == 200
    data = resp.json()["data"]
    yield data
    eliminar_categoria(category_url, header, data["id"])

@pytest.fixture(scope="function")
def fresh_category(category_url, header):
    # Úsalo en tests que SÍ eliminen (delete/update)
    name = f"Recursos_{uuid.uuid4().hex[:6]}"
    payload = json.dumps({"name": name})
    resp = requests.post(category_url, headers=header, data=payload)
    assert resp.status_code == 200
    data = resp.json()["data"]
    yield data
    eliminar_categoria(category_url, header, data["id"])

def eliminar_categoria(category_url,header,id):
  #teardown 
  payload = json.dumps({
        "ids": [id]
  })
  response = requests.delete(category_url, headers=header,data=payload)
  assert response.status_code in (200, 404)

