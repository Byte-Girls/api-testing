import pytest
import requests

@pytest.mark.smoke
def test_BIG_03_Obtener_lista_departamentos():
    """
    Descripción: El usuario debe obtener la lista completa de departamentos con su departmentId y displayName
    """

    # Ambiente
    url = "https://collectionapi.metmuseum.org/public/collection/v1/"

    # Pasos
    # 1. Seleccionar GET
    list_url = url + "departments"

    # 2. Llamar al recurso departments
    # 3. Click en el botón send
    response = requests.get(list_url)

    # 4. Verificar que el estado correcto sea 200
    assert response.status_code == 200

    # 5. Verificar que la respuesta sea un objeto con la clave "departments"
    data = response.json()
    assert "departments" in data
    assert isinstance(data["departments"], list)

""""

ID
TC-01
Título
Obtener la lista de departamentos del museo
Descripción
El usuario debe obtener la lista completa de departamentos disponibles con su departmentId y displayName.
Precondiciones
1. Tener acceso a Internet.
2. Postman instalado.
3. Endpoint https://collectionapi.metmuseum.org/public/collection/v1/departments disponible.
Ambiente
- Acceso al collectionapi.metmuseum.org
 - Usuario con permisos para ejecutar solicitudes GET.
Pasos
1. Abrir Postman.
2. Crear una nueva solicitud GET.
3. Ingresar la URL: https://collectionapi.metmuseum.org/public/collection/v1/departments.
4. Hacer clic en Send.
5. Verificar el código de estado de la respuesta (200 OK).
6. Validar que el cuerpo contiene la lista de departamentos con departmentId y displayName.

Resultado Esperado
- Código HTTP: 200 OK.- Respuesta con una lista JSON que contenga los departamentos:{
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
...

Evidencias

curl --location 'https://collectionapi.metmuseum.org/public/collection/v1/departments' \
--header 'Cookie: incap_ses_1725_1662004=kcxLdeqmn0Wup9cdt27wF19UgmgAAAAA1vcYvZ9XBZQNp2b2wdgWLA==; visid_incap_1662004=R99t4J7PSEyGuAQSL4/ThYsjgGgAAAAAQUIPAAAAAABs4JPntilbdiOwf5BU6p+o'
Prioridad
2 (Alta).
Post Condición
Teardown
Clasificación
Funcional, Smoke.

"""