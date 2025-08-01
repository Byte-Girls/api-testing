import random
import requests
import json
import pytest
from src.assertions.create_category_assertions import *

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.funcional
def test_BYT_T9_crear_una_categoria_con_nombre_valido(get_url, get_token):
  """
  Descripción:Validar que el administrador pueda crear correctamente una categoría 
  de trabajo con un nombre válido.Al enviar una solicitud POST al endpoint /admin/job-categories 
  con un JSON que contenga un nombre de categoría único
  """

  url = f"{get_url}/admin/job-categories"
  expected_name = "Recursos Humanos" + str(random.randint(1000, 9999))

  payload = json.dumps({
    "name": expected_name
  })
  headers = {
    'Content-Type': 'application/json',
    'Authorization':f'{get_token}'
  }
  
  response = requests.post( url, headers=headers, data=payload)
  assert response.status_code == 200
  assert_create_category_response_schema(response)
  response=response.json()["data"]
  assert response["name"] == expected_name
  #Validación con el get
  url = f"{get_url}/admin/job-categories/{response['id']}" 

  response =requests.get(url) 
  headers = {
    'Authorization': f'{get_token}'
  }
  response = requests.get(url, headers=headers)
  assert response.status_code == 200
  response = response.json()["data"]
  assert response["name"] == expected_name
 
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.funcional
@pytest.mark.negativo
@pytest.mark.xfail(reason="Known Issue. BYT-31: La creación de una categoría permite números en el campo nombre", run=False)
def test_BYT_T14_crear_una_categoria_con_el_campo_nombre_como_numero(get_url, get_token):
  """
  Descripción: Verifica que el campo "nombre" no acepte valores numéricos
  """

  url = f"{get_url}/admin/job-categories"
  
  payload = json.dumps({
    "name": "78945"
  })
  headers = {
    'Content-Type': 'application/json',
    'Authorization':f'{get_token}'
  }

  response = requests.post( url, headers=headers, data=payload)
  assert response.status_code == 400  
  


