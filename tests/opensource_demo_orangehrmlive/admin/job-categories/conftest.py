
from email import header
import json
import random
import requests
import pytest


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

def eliminar_categoria(category_url,header,id):
  #teardown 
  payload = json.dumps({
        "ids": [id]
  })
  response = requests.delete(category_url, headers=header,data=payload)
  assert response.status_code == 200  

  