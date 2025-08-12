import time
import pytest
import json
import requests
from src.utils.loggers_helpers import log_request_response

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.funcional
@pytest.mark.positivo
def test_BYT_T24_actualizar_categoria_existente_devuelve_200(category_url, header,category ):
    """
    Descripción: Verifica que la actualización de una categoría de trabajo existente
    devuelva un código de estado HTTP 200 OK y que el nombre de la categoría se actualice correctamente.
    """
    category_id =category["id"]
    updated_name = "Supervisores"

    payload = json.dumps({
        "name": updated_name
    })

    url = f"{category_url}/{category_id}"
    response = requests.put(url, headers=header, data=payload)

    # Validaciones
    assert response.status_code == 200
    assert response.json()["data"]["id"] == category_id
    assert response.json()["data"]["name"] == updated_name

    log_request_response(url, response, header, payload)



@pytest.mark.regression
@pytest.mark.funcional
@pytest.mark.negativo
def test_BYT_T22_actualizar_categoria_inexistente_(category_url, header):
    """
    Descripción: Verifica que intentar actualizar una categoría que no existe
    devuelve HTTP 404 Not Found con el mensaje "Record Not Found".
    """
    non_existing_id = 999999
    url = f"{category_url}/{non_existing_id}"

    payload = json.dumps({"name": "Supervisores Actualizado"})
    response = requests.put(url, headers=header, data=payload)

    assert response.status_code == 404
    body = response.json()
    assert body.get("error", {}).get("status") in [404, "404"]
    assert body.get("error", {}).get("message") == "Record Not Found"

    log_request_response(url, response, header, payload)


@pytest.mark.regression
@pytest.mark.funcional
@pytest.mark.negativo
def test_BYT_T21_actualizar_categoria_con_id_invalido_string_(category_url, header):
    """
    Descripción: Verifica que al intentar actualizar una categoría con un ID de formato inválido
    (String), se reciba un código de estado HTTP 422 Unprocessable Content con el mensaje 
    de parámetro inválido.
    """
    invalid_id = "qwertty"
    url = f"{category_url}/{invalid_id}"

    payload = json.dumps({"name": "Supervisores Actualizado"})
    response = requests.put(url, headers=header, data=payload)

    # Validaciones
    assert response.status_code == 422
    body = response.json()
    assert body.get("error", {}).get("status") == "422"
    assert body.get("error", {}).get("message") == "Invalid Parameter"
    assert "id" in body.get("error", {}).get("data", {}).get("invalidParamKeys", [])

    log_request_response(url, response, header, payload)


@pytest.mark.regression
@pytest.mark.funcional
@pytest.mark.negativo
def test_BYT_T174_actualizar_categoria_con_name_vacio(category_url, header,category):
    """
    Descripción: Verifica que al intentar actualizar una categoría con el campo 'name' vacío,
    se reciba un código de estado HTTP 422 Unprocessable Content con el mensaje de parámetro inválido.
    """
    valid_id = category["id"]
    url = f"{category_url}/{valid_id}"

    payload = json.dumps({"name": ""})
    response = requests.put(url, headers=header, data=payload)

    # Validaciones
    assert response.status_code == 422
    body = response.json()
    assert str(body.get("error", {}).get("status")) == "422"
    assert body.get("error", {}).get("message") == "Invalid Parameter"
    assert "name" in body.get("error", {}).get("data", {}).get("invalidParamKeys", [])

    log_request_response(url, response, header, payload)


@pytest.mark.regression
@pytest.mark.funcional
@pytest.mark.negativo
def test_BYT_T25_actualizar_categoria_sin_name_en_body(category_url, header,category):
    """
    Descripción: Verifica que al intentar actualizar una categoría sin incluir el campo 'name' en el body,
    se reciba un código de estado HTTP 422 Unprocessable Content con el mensaje de parámetro inválido.
    """
    valid_id = category["id"]
    url = f"{category_url}/{valid_id}"

    payload = json.dumps({})
    response = requests.put(url, headers=header, data=payload)

    # Validaciones
    assert response.status_code == 422
    body = response.json()
    assert str(body.get("error", {}).get("status")) == "422"
    assert body.get("error", {}).get("message") == "Invalid Parameter"
    assert "name" in body.get("error", {}).get("data", {}).get("invalidParamKeys", [])

    log_request_response(url, response, header, payload)


@pytest.mark.smoke
@pytest.mark.funcional
@pytest.mark.negativo
@pytest.mark.regression
@pytest.mark.seguridad
def test_BYT_T177_actualizar_categoria_con_token_invalido_(category_url):
    """
    Descripción: Verifica que al intentar actualizar una categoría con un token inválido,
    se reciba un código de estado HTTP 401 Unauthorized.
    """
    valid_id = 31
    url = f"{category_url}/{valid_id}"

    payload = json.dumps({"name": "Supervisores Actualizados"})
    
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer invalid_or_expired_token'
    }

    response = requests.put(url, headers=headers, data=payload)

    # Validaciones
    assert response.status_code == 401
    body = response.json()
    assert "error" in body
    assert "message" in body["error"]
    
    log_request_response(url, response, headers, payload)


@pytest.mark.smoke
@pytest.mark.funcional
@pytest.mark.negativo
@pytest.mark.regression
@pytest.mark.seguridad
def test_BYT_T36_actualizar_categoria_sin_token_(category_url,category):
    """
    Descripción: Verifica que al intentar actualizar una categoría sin token de autenticación,
    se reciba un código de estado HTTP 401 Unauthorized.
    """
    valid_id = category["id"]
    url = f"{category_url}/{valid_id}"

    payload = json.dumps({"name": "Supervisores Actualizados"})
    
    response = requests.put(url, data=payload)

    # Validaciones
    assert response.status_code == 401
    body = response.json()
    assert "error" in body
    assert "message" in body["error"]
    
    log_request_response(url, response, None, payload)

   
@pytest.mark.regression
@pytest.mark.funcional
@pytest.mark.rendimiento
def test_BYT_T23_Tiempo_de_respuesta_al_actualizar_categoria(category_url, header, category):
    """
    Descripción: Verificar que el tiempo de respuesta al actualizar una categoría 
    de trabajo existente con un ID válido sea menor a 2 segundos.
    """
    category_id = category["id"]
    url = f"{category_url}/{category_id}"

    payload = json.dumps({"name": "Supervisores Actualizados"})
    start_time = time.time()

    response = requests.put(url, headers=header, data=payload)
    end_time = time.time()
    response_time = end_time - start_time

    # Validaciones
    assert response.status_code == 200
    assert response_time < 2, f"Tiempo de respuesta excedido: {response_time:.4f} segundos"

    log_request_response(url, response, header, payload)


@pytest.mark.regression
@pytest.mark.funcional
@pytest.mark.negativo
@pytest.mark.xfail(reason="Known Issue. BYT-85: Se permite actualizar una categoría con caracteres especiales en el nombre", run=False)
def test_BYT_T181_actualizar_categoria_con_caracteres_especiales(category_url, header,category):
    """
    Descripción: Verifica que al intentar actualizar una categoría con caracteres especiales en el nombre,
    se reciba un código de estado HTTP 422 Unprocessable Content con el mensaje de parámetro inválido.
    """
    valid_id = category["id"] 
    url = f"{category_url}/{valid_id}"

    payload = json.dumps({"name": "@#$%()"})
    response = requests.put(url, headers=header, data=payload)

    # Validaciones
    assert response.status_code == 422
    body = response.json()
    assert body.get("error", {}).get("status") == "422"
    assert body.get("error", {}).get("message") == "Invalid Parameter"
    assert "name" in body.get("error", {}).get("data", {}).get("invalidParamKeys", [])

    log_request_response(url, response, header, payload)


@pytest.mark.regression
@pytest.mark.funcional
@pytest.mark.negativo
@pytest.mark.xfail(reason="Known Issue. BYT-84: La API permite actualizar una categoría con un ID decimal ", run=False)
def test_BYT_T182_actualizar_categoria_con_id_decimal(category_url, header):
    """
    Descripción: Verifica que al intentar actualizar una categoría con un ID decimal,
    se reciba un código de estado HTTP 422 Unprocessable Content 
    """
    category_id = "2.5"
    url = f"{category_url}/{category_id}"

    payload = json.dumps({"name": "Freelance"})
    response = requests.put(url, headers=header, data=payload)

    # Validaciones
    assert response.status_code == 422 
    body = response.json()
    assert body.get("error", {}).get("status") == "422"  
    assert body.get("error", {}).get("message") == "Invalid Parameter"  
    assert "id" in body.get("error", {}).get("data", {}).get("invalidParamKeys", []) 
    log_request_response(url, response, header, payload)


@pytest.mark.regression
@pytest.mark.funcional
@pytest.mark.negativo
def test_BYT_T183_actualizar_categoria_con_id_cero(category_url, header):
    """
    Descripción: Verifica que al intentar actualizar una categoría con un ID igual a 0,
    se reciba un código de estado HTTP 422 Unprocessable Content con el mensaje de parámetro inválido.
    """
    invalid_id = 0
    url = f"{category_url}/{invalid_id}"

    payload = json.dumps({"name": "Supervisores Actualizados"})
    
    response = requests.put(url, headers=header, data=payload)

    # Validaciones
    assert response.status_code == 422  
    body = response.json()
    assert body.get("error", {}).get("status") == "422" 
    assert body.get("error", {}).get("message") == "Invalid Parameter" 
    assert "id" in body.get("error", {}).get("data", {}).get("invalidParamKeys", []) 

    log_request_response(url, response, header, payload)


@pytest.mark.regression
@pytest.mark.funcional
@pytest.mark.negativo
def test_BYT_T186_actualizar_categoria_con_id_alfanumerico(category_url, header):
    """
    Descripción: Verifica que al intentar actualizar una categoría con un ID alfanumérico,
    se reciba un código de estado HTTP 422 Unprocessable Content con el mensaje de parámetro inválido.
    """
    alphanumeric_id = "abcdar" 
    url = f"{category_url}/{alphanumeric_id}"

    payload = json.dumps({"name": "Freelance"})
    
    response = requests.put(url, headers=header, data=payload)

    # Validaciones
    assert response.status_code == 422  
    body = response.json()
    assert body.get("error", {}).get("status") == "422"  
    assert body.get("error", {}).get("message") == "Invalid Parameter"  
    assert "id" in body.get("error", {}).get("data", {}).get("invalidParamKeys", []) 

    log_request_response(url, response, header, payload)


@pytest.mark.regression
@pytest.mark.funcional
@pytest.mark.negativo
def test_BYT_T187_actualizar_categoria_con_id_con_caracteres_especiales(category_url, header):
    """
    Descripción: Verifica que al intentar actualizar una categoría con un ID que contiene caracteres especiales,
    se reciba un código de estado HTTP 422 Unprocessable Content con el mensaje de parámetro inválido.
    """
    invalid_id = "@#%&*"
    url = f"{category_url}/{invalid_id}"

    payload = json.dumps({"name": "Freelance"})
    
    response = requests.put(url, headers=header, data=payload)

    # Validaciones
    assert response.status_code == 422  
    body = response.json()
    assert body.get("error", {}).get("status") == "422"  
    assert body.get("error", {}).get("message") == "Invalid Parameter"  
    assert "id" in body.get("error", {}).get("data", {}).get("invalidParamKeys", [])  

    log_request_response(url, response, header, payload)

