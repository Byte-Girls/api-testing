import requests
import pytest  


@pytest.mark.regresion
def test_001_verificar_que_se_pueda_mostrar_la_lista_de_todos_los_departamentos():
    
    url = "https://collectionapi.metmuseum.org/public/collection/v1/departments"

    payload = {}
    headers = {
    'Cookie': 'incap_ses_1720_1662004=6WEXYw29iRD1PUM9QKveF0DGgmgAAAAA2rN4rpra+Gn1uz922fkJRQ==; visid_incap_1662004=Q/Qivtu9RgiQGNrtHytd6QckgGgAAAAAQUIPAAAAAAAATI5qPUOY0nqVVjYfylO8'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)
    assert response.status_code == 200
    
"""
Titulo
Verificar que se pueda mostrar la lista de todos los departamentos

Descripción
Obtener una lista de todos los departamentos del museo que
contienen colecciones. Esta información me permite conocer cómo está organizada la
colección del museo y es útil si quiero categorizar obras de arte o permitir que los usuarios

Precondiciones


Ambiente
-Aceeso a metmuseum.github.io

Pasos
1. Abrir postman
2. Copiar URL
3. Seleccionar el método get
4. clic en botón send

Resultado esperado
Mostrar la lista de departamentos
    
Evidencias 
{
  "departments": [
    {
      "departmentId": 1,
      "displayName": "American Decorative Arts"
    },
    {
      "departmentId": 3,
      "displayName": "Ancient Near Eastern Art"
    },
    {
      "departmentId": 4,
      "displayName": "Arms and Armor"
    },
    {
      "departmentId": 5,
      "displayName": "Arts of Africa, Oceania, and the Americas"
    },
    
Prioridad
Media

Post condition

"""