import random
import requests
import json
import pytest
from src.assertions.create_category_assertions import *

@pytest.mark.smoke
@pytest.mark.regression
def test_BYT_15_crear_una_categoria_con_nombre_valido(get_url, get_token):
#Descripción:  El admin debe crear una categoria de trabajo

  url = f"{get_url}/admin/job-categories"
    
  payload = json.dumps({
    "name": "Recursos Humanos" + str(random.randint(1000, 9999)),
  })
  headers = {
    'Content-Type': 'application/json',
    'Authorization':f'{get_token}'
  }
  
  response = requests.post( url, headers=headers, data=payload)
  assert response.status_code ==200
  assert_create_category_response_schema(response)





