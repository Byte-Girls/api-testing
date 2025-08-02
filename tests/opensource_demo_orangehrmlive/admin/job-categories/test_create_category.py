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
def test_BYT_T12_crear_una_categoria_con_caracteres_especiales_en_el_campo_name(category_url, header):
  """
  Descripción: Verifica que el campo "nombre" no acepte caracteres especiales
  """   
  payload = json.dumps({
    "name": "  #$%()*| "
  })

  response = requests.post(category_url, headers=header, data=payload)
  assert response.status_code == 400  

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.funcional
@pytest.mark.negativo
def test_BYT_T10_crear_una_categoria_con_nombre_duplicado(category_url, header):
  """
  Validar que el sistema no permita la creación de una nueva categoría de trabajo 
  con un nombre que ya existe en el sistema.
  """
  url = f"{get_url}/admin/job-categories"
  payload = json.dumps({
    "name": "Administrador"
  })

  #Primera creación 
  requests.post(category_url, headers=header, data=payload)
  #Segunda creación con nombre duplicado
  response = requests.post(category_url, headers=header, data=payload)
  assert response.status_code == 422
  

@pytest.mark.regression
@pytest.mark.funcional
@pytest.mark.positivo
def test_BYT_T15_Verificar_que_el_JSON_de_respuesta_contenga_los_campos_id_name(category_url, header):
  """
  Validar que, al crear una categoría de trabajo exitosamente mediante el endpoint correspondiente, 
  el cuerpo de la respuesta contenga los campos id y name.
  """
  expected_name = "Recursos" + str(random.randint(1000, 9999))
  payload = json.dumps({
    "name": expected_name
  })
  
  response = requests.post(category_url, headers=header, data=payload)
  assert_resource_response_schema(response, "category_schema_response.json")
  assert response.status_code == 200  
  response = response.json()["data"]
  assert response["name"] == expected_name

@pytest.mark.regression
@pytest.mark.funcional
@pytest.mark.negativo
def test_BYT_T13_Crear_una_categoría_con_nombre_mayor_a_50_caracteres(category_url, header):
  """
  Verificar que el sistema no permita crear una categoría de trabajo cuando el valor del 
  campo name supera los 50 caracteres permitidos.
  """
  name_with_more_than_50_characters = "a" * 51
  payload = json.dumps({
    "name": name_with_more_than_50_characters
  })
  
  response = requests.post(category_url, headers=header, data=payload)
  assert response.status_code == 422
  

@pytest.mark.negativo
def test_BYT_T11_Crear_una_categoria_sin_enviar_el_campo_nombre(category_url, header):
  """
  Verificar que el sistema no permita la creación de una categoría de trabajo cuando no se incluye el campo name  
  Enviar una solicitud POST al endpoint /admin/job-categories con el cuerpo vacío {}.
  """
  payload = json.dumps({})

  response = requests.post(category_url, headers=header, data=payload)
  assert response.status_code == 422
  assert_resource_response_schema(response, "error_422_schema_response.json")

