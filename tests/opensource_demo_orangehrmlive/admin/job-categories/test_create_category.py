import random
import requests
import json
import pytest
from src.assertions.create_category_assertions import *

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.funcional
def test_BYT_T9_crear_una_categoria_con_nombre_valido(get_url, get_token):
#Descripción:Validar que el administrador pueda crear correctamente una categoría de trabajo con un nombre válido.Al enviar una solicitud POST al endpoint /admin/job-categories con un JSON que contenga un nombre de categoría único

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





