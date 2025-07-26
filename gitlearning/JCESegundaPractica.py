
import pytest
import requests

@pytest.mark.smoke
def test_Obtener_objeto_no_existente_():

 # Ambiente
url = "https://jsonplaceholder.typicode.com/posts/999999"

# Pasos
    # 1. Seleccionar GET
list_url = url +"objects"
  #2.llamar al recurso objects
  #3. Click en el boton send
  response = requests.get(list_url)
  #4. verificar que el estado sea 404

assert response.status_code==404

#Prioridad
# media.
#Post Condición
#Teardown
#Clasificación
#Funcional, Smoke,Negative.