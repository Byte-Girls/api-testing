import random
import requests
import json
import pytest
from src.assertions.common_assertions import *

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.funcional
def test_BYT_T9_crear_una_categoria_con_nombre_valido(category_url, header):
  """
  Descripción:Validar que el administrador pueda crear correctamente una categoría 
  de trabajo con un nombre válido.Al enviar una solicitud POST al endpoint /admin/job-categories 
  con un JSON que contenga un nombre de categoría único
  """
  expected_name = "Recursos Humanos" + str(random.randint(1000, 9999))
  payload = json.dumps({
    "name": expected_name
  })

  response = requests.post(category_url, headers=header, data=payload)
  assert response.status_code == 200
  assert_resource_response_schema(response, "category_schema_response.json")
  response = response.json()["data"]
  assert response["name"] == expected_name
  # Validación con el get
  url = f"{category_url}/{response['id']}" 
  response = requests.get(url, headers=header)
  assert response.status_code == 200
  response = response.json()["data"]
  assert response["name"] == expected_name
 
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.funcional
@pytest.mark.negativo
@pytest.mark.xfail(reason="Known Issue. BYT-31: La creación de una categoría permite números en el campo nombre", run=False)
def test_BYT_T14_crear_una_categoria_con_el_campo_nombre_como_numero(category_url, header):
  """
  Descripción: Verifica que el campo "nombre" no acepte valores numéricos
  """
  payload = json.dumps({
    "name": "78945"
  })

  response = requests.post(category_url, headers=header, data=payload)
  assert response.status_code == 400  

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.funcional
@pytest.mark.negativo
@pytest.mark.xfail(reason="Known Issue. BYT-33: La creación de una categoría permite caracteres especiales en el campo nombre", run=False)
def test_BYT_T12_crear_una_categoria_con_caracteres_especiales_en_el_campo_name(get_url, get_token):
  """
    Descripción: Verifica que el campo "nombre" no acepte caracteres especiales
    """
  url = f"{get_url}/admin/job-categories"
      
  payload = json.dumps({
    "name": "  #$%()*| "
  })
  headers = {
    'Content-Type': 'application/json',
    'Authorization':f'{get_token}'
  }

  response = requests.post(url, headers=headers, data=payload)
  assert response.status_code == 400  
  

@pytest.mark.regression
@pytest.mark.funcional
@pytest.mark.negativo
def test_BYT_T10_crear_una_categoria_con_nombre_duplicado(get_url, get_token):
  """
  Validar que el sistema no permita la creación de una nueva categoría de trabajo 
  con un nombre que ya existe en el sistema.
  """

  url = f"{get_url}/admin/job-categories"
  

  payload = json.dumps({
    "name": "Administrador"
  })
  headers = {
    'Content-Type': 'application/json',
    'Authorization':f'{get_token}'
  }
  #Primera creación 
  requests.post(url, headers=headers, data=payload)
  #Segunda creación con nombre duplicado
  response = requests.post(url, headers=headers, data=payload)
  assert response.status_code == 422
