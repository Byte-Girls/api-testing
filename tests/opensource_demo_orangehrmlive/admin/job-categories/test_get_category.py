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
  
  