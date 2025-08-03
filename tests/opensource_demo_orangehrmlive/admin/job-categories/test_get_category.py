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
def test_BYT_T87_Obtener_categoria_con_id_negativo(category_url, header):
  """
  Descripción: Verificar que el sistema responda adecuadamente cuando se intenta obtener 
  una categoría de trabajo utilizando un ID negativo (-5).
  """
  id_negativo = -5
  url = f"{category_url}/{id_negativo}"
  response = requests.get(url, headers=header)
  assert response.status_code == 422
  f"Se esperaba 422, pero se recibió {response.status_code}"

@pytest.mark.regression
@pytest.mark.funcional
@pytest.mark.negativo
def test_BYT_T88_Obtener_categoria_con_id_extremadamente_grande(category_url, header):
  """
  Descripción: Verificar que el sistema responda adecuadamente cuando se intenta obtener 
  una categoría de trabajo utilizando un ID extremadamente grande (999999999999).
  """
  id_grande = 999999999999
  url = f"{category_url}/{id_grande}"
  response = requests.get(url, headers=header)
  assert response.status_code == 404, \
    f"Se esperaba 404 Not Found, pero se recibió {response.status_code}"

@pytest.mark.regression
@pytest.mark.funcional
@pytest.mark.negativo
def test_BYT_T89_Obtener_categoria_con_id_cero(category_url, header):
  """
  Descripción: Verificar que el sistema responda adecuadamente cuando se intenta obtener 
  una categoría de trabajo utilizando un ID igual a cero (0).
  """
  id_cero = 0
  url = f"{category_url}/{id_cero}"
  response = requests.get(url, headers=header)
  assert response.status_code == 422, \
    f"Se esperaba 422, pero se recibió {response.status_code}"

@pytest.mark.regression
@pytest.mark.funcional
@pytest.mark.xfail(reason="Known Issue. BYT-57: Al buscar una categoría con decimal la API interpreta ID decimal como entero", run=False)
def test_BYT_T90_Obtener_categoria_con_id_decimal_interpreta_como_entero(category_url, header):
  """
  Descripción: Verificar que el sistema rechace un ID decimal (1.5) al obtener una categoría de trabajo.
  """
  id_decimal = 1.5
  url = f"{category_url}/{id_decimal}"
  response = requests.get(url, headers=header)
  assert response.status_code == 200