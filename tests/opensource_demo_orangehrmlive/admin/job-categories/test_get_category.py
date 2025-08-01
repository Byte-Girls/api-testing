import requests
import json
import pytest
from src.assertions.get_category_assertions import *

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.funcional
def test_BYT_T2_Obtener_una_categoria_de_trabajo_existente_con_id_válido(get_url,get_token):
  """
  Descripción:  Verificar que el administrador pueda consultar una categoría de trabajo existente 
  proporcionando un ID válido.
  """
  url = f"{get_url}/admin/job-categories/1" 

  response =requests.get(url) 
  headers = {
    'Authorization': f'{get_token}'
  }
  response = requests.get(url, headers=headers)
  assert response.status_code == 200
  assert_get_category_response_schema(response)  
  