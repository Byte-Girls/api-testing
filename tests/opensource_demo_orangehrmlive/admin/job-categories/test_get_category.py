import logging
from venv import logger
import json
import pytest
import time
from src.assertions.common_assertions import *
from src.orange_api.api_request import OrangeRequest
from src.utils.loggers_helpers import log_request_response

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.funcional
@pytest.mark.positivo
def test_BYT_T2_Obtener_una_categoria_de_trabajo_existente_con_id_valido(category_url, header,category):
  """
  Descripción:  Verificar que el administrador pueda consultar una categoría de trabajo existente 
  proporcionando un ID válido.

  Prioridad: Alta 
  """
  category_id = category["id"]
  url = f"{category_url}/{category_id}"
  response = OrangeRequest.get(url, headers=header)
  assert response.status_code == 200
  assert_resource_response_schema(response, "category_schema_response.json")
  log_request_response(url, response, header)

  
@pytest.mark.regression
@pytest.mark.funcional
@pytest.mark.negativo
def test_BYT_T87_Obtener_categoria_con_id_negativo(category_url, header):
  """
  Descripción: Verificar que el sistema responda adecuadamente cuando se intenta obtener 
  una categoría de trabajo utilizando un ID negativo (-5).
  
  Prioridad: Media 
  """
  id_negativo = -5
  url = f"{category_url}/{id_negativo}"
  response = OrangeRequest.get(url, headers=header)
  assert response.status_code == 422
  log_request_response(url, response, header)

  
@pytest.mark.regression
@pytest.mark.funcional
@pytest.mark.negativo
def test_BYT_T4_Obtener_una_categoria_con_id_invalido(category_url, header):
  """
  Descripción: Verificar que el sistema responda adecuadamente cuando se intenta obtener 
  una categoría de trabajo utilizando un ID inválido (texto o símbolo).
  
  Prioridad: Media
  """
  id_invalido = "abc@!"  
  url = f"{category_url}/{id_invalido}"
  response = OrangeRequest.get(url, headers=header)
  assert response.status_code == 422 
  log_request_response(url, response, header)

  
@pytest.mark.regression
@pytest.mark.funcional
@pytest.mark.negativo
def test_BYT_T88_Obtener_categoria_con_id_extremadamente_grande(category_url, header):
  """
  Descripción: Verificar que el sistema responda adecuadamente cuando se intenta obtener 
  una categoría de trabajo utilizando un ID extremadamente grande (999999999999).
  
  Prioridad: Media
  """
  id_grande = 999999999999
  url = f"{category_url}/{id_grande}"
  response = OrangeRequest.get(url, headers=header)
  assert response.status_code == 404, \
    f"Se esperaba 404 Not Found, pero se recibió {response.status_code}"
  log_request_response(url, response, header)

  
@pytest.mark.regression
@pytest.mark.funcional
@pytest.mark.negativo
def test_BYT_T89_Obtener_categoria_con_id_cero(category_url, header):
  """
  Descripción: Verificar que el sistema responda adecuadamente cuando se intenta obtener 
  una categoría de trabajo utilizando un ID igual a cero (0).
  
  Prioridad: Media
  """
  id_cero = 0
  url = f"{category_url}/{id_cero}"
  response = OrangeRequest.get(url, headers=header)
  assert response.status_code == 422
  log_request_response(url, response, header)

  
@pytest.mark.regression
@pytest.mark.funcional
@pytest.mark.negativo
@pytest.mark.xfail(reason="Known Issue. BYT-57: Al buscar una categoría con decimal la API interpreta ID decimal como entero", run=False)
def test_BYT_T90_Obtener_categoria_con_id_decimal_interpreta_como_entero(category_url, header):
  """
  Descripción: Verificar que el sistema rechace un ID decimal (1.5) al obtener una categoría de trabajo.
  
  Prioridad: Media
  """
  id_decimal = 1.5
  url = f"{category_url}/{id_decimal}"
  response = OrangeRequest.get(url, headers=header)
  assert response.status_code == 400
  log_request_response(url, response, header)

  
@pytest.mark.regression
@pytest.mark.funcional 
@pytest.mark.negativo
def test_BYT_T3_Obtener_una_categoria_con_id_inexistente(category_url, header):
  """
  Descripción: Verificar que el sistema responda adecuadamente cuando se intenta obtener 
  una categoría de trabajo utilizando un ID que no existe en la base de datos.
  
  Prioridad: Media
  """
  id_inexistente = 99999
  url = f"{category_url}/{id_inexistente}"
  response = OrangeRequest.get(url, headers=header)
  assert response.status_code == 404  
  log_request_response(url, response, header)

  
@pytest.mark.regression
@pytest.mark.funcional
@pytest.mark.rendimiento
def test_BYT_T8_Tiempo_de_respuesta_al_obtener_categoria(category_url, header,category):
  """
  Descripción: Verificar que el tiempo de respuesta al consultar una categoría de trabajo 
  existente con un ID válido sea menor a 2 segundos.
  
  Prioridad: Media
  """
  category_id = category["id"]
  url = f"{category_url}/{category_id}" 
  start_time = time.time()
  response = OrangeRequest.get(url, headers=header)
  end_time = time.time()
  response_time = end_time - start_time

  assert response.status_code == 200
  assert response_time < 2, f"Tiempo de respuesta excedido: {response_time:.4f} segundos"
  log_request_response(url, response, header)

  
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.funcional
@pytest.mark.positivo
def test_BYT_T7_Verificar_campos_id_y_name_en_respuesta(category_url, header,category):
  """
  Descripción: Verificar que al consultar una categoría de trabajo existente con un ID válido,
  la respuesta incluya los campos 'id' y 'name'.
  
  Prioridad: Alta
  """
  category_id = category["id"]
  url = f"{category_url}/{category_id}"  # ID válido
  response = OrangeRequest.get(url, headers=header)
  assert response.status_code == 200
  data = response.json().get("data", {})
  assert "id" in data, "El campo 'id' no está presente en la respuesta."
  assert "name" in data, "El campo 'name' no está presente en la respuesta."
  assert isinstance(data["id"], int)
  assert isinstance(data["name"], str)
  log_request_response(url, response, header)


@pytest.mark.regression
@pytest.mark.funcional 
@pytest.mark.negativo
@pytest.mark.seguridad
def test_BYT_T6_Obtener_categoria_con_token_invalido(category_url):
  """
  Descripción: Verificar que el sistema rechace la solicitud de obtener una categoría 
  con token inválido.
  
  Prioridad: Alta
  """
  category_id = 1
  url = f"{category_url}/{category_id}"

  headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer invalid_or_expired_token'
    }
  
  response = OrangeRequest.get(url, headers=headers)
  assert response.status_code == 401  
  log_request_response(url, response)


@pytest.mark.regression
@pytest.mark.funcional 
@pytest.mark.negativo
@pytest.mark.seguridad
def test_BYT_T5_Obtener_categoria_sin_autenticacion(category_url):
  """
  Descripción: Verificar que el sistema rechace la solicitud de obtener una categoría de trabajo 
  cuando no se envía el token de autenticación.
  
   Prioridad: Alta 
  """

  category_id = 1
  url = f"{category_url}/{category_id}"
  
  response = OrangeRequest.get(url, headers={})
  assert response.status_code == 401  
  log_request_response(url, response)


