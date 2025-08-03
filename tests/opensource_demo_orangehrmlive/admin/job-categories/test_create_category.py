import random
import string
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
  response_data = response.json()["data"]
  assert response_data["name"] == expected_name

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

@pytest.mark.regression
@pytest.mark.funcional
@pytest.mark.positivo
def test_BYT_T19_Crear_una_categoría_con_exactamente_50_caracteres(category_url, header):
  """
  Verificar que el sistema permita crear una categoría de trabajo cuando el valor del 
  campo name sea exactamente 50 caracteres.
  """
  letter_one_character = random.choice(string.ascii_letters)
  name_with_50_characters = letter_one_character * 50
  payload = json.dumps({
    "name": name_with_50_characters
  })
  
  response = requests.post(category_url, headers=header, data=payload)
  assert response.status_code == 200
  assert_resource_response_schema(response, "category_schema_response.json")
  response = response.json()["data"]
  assert response["name"] == name_with_50_characters  


@pytest.mark.regression
@pytest.mark.funcional
@pytest.mark.positivo
def test_BYT_T20_Crear_categoria_con_1_caracter(category_url, header):
  """
  Verificar que el sistema permita crear una categoría de trabajo cuando el valor 
  del campo name tiene exactamente 1 carácter.
  """
  letter_one_character = random.choice(string.ascii_letters)
  name_with_1_character = letter_one_character
  payload = json.dumps({
    "name": name_with_1_character
  })

  response = requests.post(category_url, headers=header, data=payload)
  assert response.status_code == 200
  assert_resource_response_schema(response, "category_schema_response.json")
  response = response.json()["data"]
  assert response["name"] == name_with_1_character

@pytest.mark.regression
@pytest.mark.funcional
def test_BYT_T18_Verificar_tiempo_de_respuesta_menor_a_2s_al_crear_categoria(category_url, header):
  """
  Verificar que el tiempo de respuesta al crear una categoría de trabajo sea menor a 2 segundos.
  """
  name_for_timing = "CategoriaTiempo_" + str(random.randint(1000, 9999))
  payload = json.dumps({
    "name": name_for_timing
  })

  response = requests.post(category_url, headers=header, data=payload)
  assert response.status_code == 200
  assert_resource_response_schema(response, "category_schema_response.json")
  response_data = response.json()["data"]
  assert response_data["name"] == name_for_timing
  # Validar tiempo de respuesta menor a 2 segundos
  assert response.elapsed.total_seconds() < 2, f"Tiempo de respuesta excedido: {response.elapsed.total_seconds()}s"


@pytest.mark.regression
@pytest.mark.funcional
@pytest.mark.positivo
def test_BYT_T17_Categoria_creada_aparece_en_listado(category_url, header):
  """
  Validar que una categoría de trabajo creada aparezca luego en la lista obtenida 
  mediante GET /admin/job-categories.
  """
  unique_name = "Categoria_" + str(random.randint(1000, 9999))
  payload = json.dumps({
    "name": unique_name
  })

  # Crear la categoría
  response = requests.post(category_url, headers=header, data=payload)
  assert response.status_code == 200
  assert_resource_response_schema(response, "category_schema_response.json")
  created_data = response.json()["data"]
  assert created_data["name"] == unique_name
  # Obtener listado de categorías
  response = requests.get(category_url, headers=header)
  assert response.status_code == 200
  response = response.json()["data"]
  # Validar que la categoría creada esté en el listado
  category_names = [item["name"] for item in response]
  assert unique_name in category_names

