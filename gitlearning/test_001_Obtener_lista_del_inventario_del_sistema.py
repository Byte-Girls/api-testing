import requests
import pytest
# Prioridad
# 1 High

# ID: 001
# - Título: 
# Verificar lista cantidades inventario de mascotas
@pytest.mark.smoke
def test_001_verificar_lista_cantidades_inventario_mascotas():    
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


# Prioridad
# Low


""" 
ID: 002  
- Título:  
Validar error 404 al consultar una orden con id inexistente

- Descripción:  
El usuario envía un id numérico que no existe en el sistema y debe recibir un error 404 Not Found.

- Pasos:

1. Abrir Postman o terminal con curl.  
2. Realizar una solicitud GET con un id numérico inexistente, por ejemplo id=99999.  
3. Enviar la solicitud.  
4. Verificar que el código HTTP sea 404.  
5. Confirmar que el mensaje indique que la orden no fue encontrada.

- Resultado esperado:  
Código HTTP: 404 Not Found  
Mensaje de error indicando que la orden no existe.
"""
@pytest.mark.functional
def test_002_error_404_al_consultar_orden_con_id_inexistente():    
    url = "https://petstore.swagger.io/v2"
    endpoint = "/store/order/999999"
    complete_url = url + endpoint
    response = requests.get(complete_url)
    assert response.status_code == 404

""" 
ID: 003
- Título:
Validar error 400 al enviar letras en el parámetro id de orden

- Descripción:
El usuario envía un valor no numérico en el parámetro id y debe recibir un error 400 Bad Request.

- Pasos:

1. Abrir Postman o terminal con curl.
2. Realizar una solicitud GET con id=abc123 (o cualquier cadena no numérica).
3. Enviar la solicitud.
4. Verificar que el código HTTP sea 400.
5. Confirmar que el mensaje indique que el parámetro id es inválido.

- Resultado esperado:
Código HTTP: 400 Bad Request
Mensaje del de error por parámetro inválido.
"""

@pytest.mark.functional
def test_003_validar_error_400_al_enviar_letras_en_el_parametro_id_de_orden():    
    url = "https://petstore.swagger.io/v2"
    endpoint = "/store/order/abc123"
    complete_url = url + endpoint
    response = requests.get(complete_url)
    assert response.status_code == 400