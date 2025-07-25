import requests
import pytest

@pytest.mark.smoke
def test_Obtener_los_datos_del_objeto_con_ID_5(): 
    print ("hola1")
    url = "https://collectionapi.metmuseum.org"

    list_url = url + "/public/collection/v1/objects/5"

    response = requests.get(list_url)
    print ("hola")
    assert response.status_code == 200

""" Título: Obtener los datos del objeto con ID 5
Descripción
El usuario debe poder consultar la información completa del objeto con ID 
5 en la API del Met Museum, verificando que los datos coincidan con el esquema esperado que son (ID, título, material, dimensiones, etc.).
 E.g.
 (Pegar llamada o prueba de Postman)
Precondiciones
El objeto con ID 5 debe existir en la API pública del Met Museum.
Contar con acceso a la API mediante una herramienta como Postman.
Ambiente
API URL: https://collectionapi.metmuseum.org/public/collection/v1/objects/5
Herramienta: Postman.
Usuario: No se requiere autenticación (API pública).
Pasos
Abrir Postman.
Crear una nueva solicitud.
Copiar la URL:
https://collectionapi.metmuseum.org/public/collection/v1/objects/5
Seleccionar el método GET.
Hacer clic en el botón Send.
Verificar el código de respuesta y el contenido del JSON.
Resultado Esperado
Comparar el body de salida contiene:


"objectID": 5
"objectName": "Coin"
"title": "Two-and-a-Half Dollar Coin"
"medium": "Gold"
"repository": "Metropolitan Museum of Art, New York, NY"
"objectURL" válido.
  """