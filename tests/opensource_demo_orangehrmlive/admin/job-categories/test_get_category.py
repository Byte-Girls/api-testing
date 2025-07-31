import requests
import json
import pytest

@pytest.mark.smoke
@pytest.mark.regression
def test_BYT_16_obtener_una_categoria_de_trabajo_existente_con_id_válido(get_url,get_token):
#Descripción:  El admin obtiene una cat de trabajo

  url = f"{get_url}/admin/job-categories/1" 

  response =requests.get(url) 
  headers = {
    'Authorization': f'{get_token}'
  }
  response = requests.get(url, headers=headers)
  assert response.status_code ==200
