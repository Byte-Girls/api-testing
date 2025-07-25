import requests
import pytest
# Prioridad
# 1 High

# - Título: 
# Obtener lista del inventario del sistema
@pytest.mark.smoke
def test_001_Obtener_lista_del_inventario_del_sistema():    
    # - Descripción:
    # El usuario debe obtener las cantidades disponibles de cada tipo de ítem en el inventario de una tienda de mascotas.


    # - Precondiciones:
    # El inventario debe contener al menos un ítem registrado en la tienda.

    # - Ambiente:
    # URL base: https://petstore.swagger.io/v2
    url = "https://petstore.swagger.io/v2"
    endpoint = "/store/inventory"
    # Endpoint: /store/inventory
    # Método: GET
    # No requiere autenticación
    # Acceso a Postman o curl desde termina


    # - Pasos:
    # 1. Abrir Postman o terminal con curl.
    # 2. Copiar y pegar la URL: https://petstore.swagger.io/v2/store/inventory
    complete_url = url + endpoint

    # 3. Seleccionar el método GET.
    # 4. Hacer clic en el botón "Send" (Postman) o ejecutar el comando curl.
    response = requests.get(complete_url)

    # 5. Verificar que el código de respuesta HTTP sea 200 OK.
    assert response.status_code == 200
    # 6. Validar que el cuerpo de respuesta contenga un objeto JSON.
    # 7. Confirmar que los valores asociados a cada clave sean números enteros.

# - Resultado esperado:
# {
#    "totvs": 2,
#    " Not available": 1,
#    "Null": 1,
# }
# Tipo de respuesta: application/json
# Código HTTP: 200
# Claves esperadas: estados del inventario
# Valores: cantidad por estado (integer)

#- Postcondición
# Eliminar el objeto si fue creado en las precondiciones
