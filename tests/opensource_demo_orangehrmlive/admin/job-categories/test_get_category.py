import requests
import json
import pytest
from src.assertions.common_assertions import *

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.funcional
def test_BYT_T2_Obtener_una_categoria_de_trabajo_existente_con_id_valido(category_url, header):
  """
  Descripción:  Verificar que el administrador pueda consultar una categoría de trabajo existente 
  proporcionando un ID válido.
  """
  url = f"{category_url}/1"
  response = requests.get(url, headers=header)
  assert response.status_code == 200
  assert_resource_response_schema(response, "category_schema_response.json")

  
@pytest.mark.regression
@pytest.mark.funcional
@pytest.mark.negativo
def test_BYT_T4_Obtener_una_categoria_con_id_invalido(category_url, header):
  """
  Descripción: Verificar que el sistema responda adecuadamente cuando se intenta obtener 
  una categoría de trabajo utilizando un ID inválido (texto o símbolo).
  """
  id_invalido = "abc@!"  
  url = f"{category_url}/{id_invalido}"
  response = requests.get(url, headers=header)
  assert response.status_code == 422 


@pytest.mark.regression
@pytest.mark.funcional
@pytest.mark.negativo
def test_BYT_T3_Obtener_una_categoria_con_id_inexistente(category_url, header):
  """
  Descripción: Verificar que el sistema responda adecuadamente cuando se intenta obtener 
  una categoría de trabajo utilizando un ID que no existe en la base de datos.
  """
  id_inexistente = 99999
  url = f"{category_url}/{id_inexistente}"
  response = requests.get(url, headers=header)
  assert response.status_code == 404  

import time

@pytest.mark.regression
@pytest.mark.funcional
def test_BYT_T8_Tiempo_de_respuesta_al_obtener_categoria(category_url, header):
  """
  Descripción: Verificar que el tiempo de respuesta al consultar una categoría de trabajo 
  existente con un ID válido sea menor a 2 segundos.
  """
  url = f"{category_url}/7" 
  start_time = time.time()
  response = requests.get(url, headers=header)
  end_time = time.time()
  response_time = end_time - start_time

  assert response.status_code == 200
  assert response_time < 2, f"Tiempo de respuesta excedido: {response_time} segundos"


@pytest.mark.regression
@pytest.mark.funcional
@pytest.mark.positivo
def test_BYT_T7_Verificar_campos_id_y_name_en_respuesta(category_url, header):
  """
  Descripción: Verificar que al consultar una categoría de trabajo existente con un ID válido,
  la respuesta incluya los campos 'id' y 'name'.
  """
  url = f"{category_url}/8"  # ID válido
  response = requests.get(url, headers=header)
  assert response.status_code == 200
  data = response.json().get("data", {})
  assert "id" in data, "El campo 'id' no está presente en la respuesta."
  assert "name" in data, "El campo 'name' no está presente en la respuesta."
  assert isinstance(data["id"], int)
  assert isinstance(data["name"], str)

