import json
import pytest
from src.orange_api.api_request import OrangeRequest
from src.assertions.common_assertions import *
from src.assertions.update_category_assertions import *
from src.utils.loggers_helpers import log_request_response
from src.assertions.delete_category_assertions import *

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.funcional
@pytest.mark.positivo
def test_BYT_T93_Eliminación_exitosa_de_categoría_existente_(category_url, header, category):
    """
    Descripción: Verifica que la eliminación de una categoría de trabajo existente
    devuelva un código de estado HTTP 200 OK y que la categoría se elimine correctamente.

    Prioridad: Alta
    """
    
    category_id = category["id"]

    payload = json.dumps({
        "ids": [category_id]
    })

    response = OrangeRequest.delete(category_url, headers=header, payload=payload)

    # Validaciones
    assert_status_code(response, 200)
    assert_resource_response_schema(response, "delete_category_schema_response.json")
    log_request_response(category_url, response, header, payload)
    assert_category_not_exists(category_url, category_id, header)
    
@pytest.mark.regression
@pytest.mark.funcional
@pytest.mark.positivo
def test_BYT_T173_eliminar_categoria_con_ids_duplicados(category_url, header, fresh_category):
    """
    Descripción: Verifica que la eliminación funcione correctamente
    aunque el array de IDs contenga valores duplicados.

      Prioridad: Media
    """
    category_id = fresh_category["id"]
    payload = json.dumps({
        "ids": [category_id, category_id]
    })

    response = OrangeRequest.delete(category_url, headers=header, payload=payload)

    # Validaciones
    assert_status_code(response, 200)
    assert_resource_response_schema(response, "delete_category_schema_response.json")
    log_request_response(category_url, response, header, payload)
    assert_category_not_exists(category_url, category_id, header)
    assert_id_deleted_once(response, category_id)


@pytest.mark.regression
@pytest.mark.funcional
@pytest.mark.negativo
@pytest.mark.seguridad
def test_BYT_T100_Eliminar_categoria_sin_token_valido(category_url, category):
    """
    Descripción: Verifica que al intentar eliminar una categoría de trabajo sin un token válido,
    el sistema devuelva un código HTTP 401 Unauthorized y no permita la eliminación.
    
     Prioridad: Alta
    """
    category_id = category["id"]

    payload = json.dumps({
        "ids": [category_id]
    })

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer invalid_or_expired_token'
    }
    response = OrangeRequest.delete(category_url, headers=headers, payload=payload)

    # Validaciones
    assert_status_code(response, 401)
    assert_invalid_token(response)
    assert_resource_response_schema(response, "error_message_schema_response.json")
    log_request_response(category_url, response, headers, payload)


@pytest.mark.regression
@pytest.mark.funcional
@pytest.mark.negativo
def test_BYT_T172_Eliminar_categoria_con_id_negativo(category_url, header):
    """
    Descripción: Verifica que al enviar IDs negativos en la eliminación de categorías,
    el sistema responda 404 Not Found y no procese la eliminación.
    
     Prioridad: Media
    """
    payload = json.dumps({
        "ids": [-8]
    })

    response = OrangeRequest.delete(category_url, headers=header, payload=payload)

    # Validaciones
    assert_status_code(response, 404)
    assert_error_message(response, 404, "Records Not Found")
    assert_resource_response_schema(response, "error_message_schema_response.json")
    log_request_response(category_url, response, header, payload)


@pytest.mark.regression
@pytest.mark.funcional
@pytest.mark.negativo
def test_BYT_T176_Eliminar_categoria_con_ids_nulos_o_nan(category_url, header):
    """
    Descripción: Verifica que al enviar IDs nulos o NaN en la eliminación de categorías,
    el sistema responda 404 Not Found y no procese la eliminación.
    
    Prioridad: Media
    """
    payload = json.dumps({
        "ids": [None, "NaN"
    ]})

    response = OrangeRequest.delete(category_url, headers=header, payload=payload)

    # Validaciones
    assert_status_code(response, 404)
    assert_error_message(response, 404, "Records Not Found")
    assert_resource_response_schema(response, "error_message_schema_response.json")
    assert_response_time(response.elapsed.total_seconds(), max_seconds=2)
    log_request_response(category_url, response, header, payload)


@pytest.mark.regression
@pytest.mark.funcional
@pytest.mark.negativo
def test_BYT_T95_Eliminar_categoria_inexistente(category_url, header):
    """
    Descripción: Verifica que al intentar eliminar una categoría inexistente
    el sistema devuelva un código HTTP 404 Not Found y no procese la eliminación.
    
    Prioridad: Media
    """
    payload = json.dumps({
        "ids": [99999]
    }) 

    response = OrangeRequest.delete(category_url, headers=header, payload=payload)

    # Validaciones
    assert_status_code(response, 404)
    assert_error_message(response, 404, "Records Not Found")
    assert_resource_response_schema(response, "error_message_schema_response.json")
    log_request_response(category_url, response, header, payload)

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.funcional
@pytest.mark.negativo
@pytest.mark.seguridad
@pytest.mark.xfail(reason="Known Issue. BYT-90: La API permite ejecutar eliminación con payload malicioso (SQLi/XSS) en el campo IDs", run=False)
def test_BYT_T175_Eliminar_categoria_con_payload_malicioso(category_url, header):
    """
    Descripción: Verifica que al intentar eliminar categorías enviando payload con
    caracteres extraños o potencialmente maliciosos (SQLi, XSS), el sistema no ejecute
    código malicioso y responda de forma controlada.
    
     Prioridad : Alta
    """
    payload = json.dumps({
        "ids": [
            "1 OR 1=1",                  
            "<script>alert('x')</script>"
        ]
    })

    response = OrangeRequest.delete(category_url, headers=header, payload=payload)

    # Validaciones: según seguridad, debería ser 400 o 404; actualmente devuelve 200 → bug.
    assert_status_code(response, 200)
    assert_resource_response_schema(response, "delete_category_schema_response.json")
    log_request_response(category_url, response, header, payload)



@pytest.mark.regression
@pytest.mark.funcional
@pytest.mark.negativo
def test_BYT_T96_Eliminar_categoria_ya_eliminada(category_url, header, fresh_category):
    """
    Descripción: Verifica que al intentar eliminar una categoría que ya fue eliminada previamente,
    el sistema devuelva un código HTTP 404 Not Found y no procese la eliminación.
    
    Prioridad: Media
    """
    category_id = fresh_category["id"]
    payload = json.dumps({"ids": [category_id]})

    first_response = OrangeRequest.delete(category_url, headers=header, payload=payload)
    assert_status_code(first_response, 200)
    assert_resource_response_schema(first_response, "delete_category_schema_response.json")

    second_response = OrangeRequest.delete(category_url, headers=header, payload=payload)

    assert_status_code(second_response, 404)
    assert_error_message(second_response, 404, "Records Not Found")
    assert_resource_response_schema(second_response, "error_message_schema_response.json")
    log_request_response(category_url, second_response, header, payload)

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.funcional
@pytest.mark.positivo
def test_BYT_T94_Eliminar_multiples_categorias_a_la_vez(category_url, header, fresh_category):
    """
    Descripción: Verifica que el endpoint permita eliminar múltiples categorías en una sola petición.
    Se envía un ID existente y otros que no existen; se espera 200 OK y que el array 'data'
    contenga únicamente los IDs realmente eliminados.
    
    Prioridad: Media
    """
    existing_id = fresh_category["id"]
    non_existing_ids = [99999, 88888, 77777]  

    payload = json.dumps({"ids": [existing_id, *non_existing_ids]})

    response = OrangeRequest.delete(category_url, headers=header, payload=payload)

    # Validaciones
    assert_status_code(response, 200)
    assert_resource_response_schema(response, "delete_category_schema_response.json")
    log_request_response(category_url, response, header, payload)

    assert_deleted_category_ids(
        response,
        expected_ids=[existing_id],
        unexpected_ids=non_existing_ids
    )
    assert_category_not_exists(category_url, existing_id, header)


@pytest.mark.regression
@pytest.mark.funcional
@pytest.mark.negativo
def test_BYT_T98_Eliminar_categoria_con_id_formato_invalido(category_url, header):
    """
    Descripción: Verifica que al intentar eliminar una categoría enviando un ID en formato no numérico
    (string), el sistema devuelva un código HTTP 404 Not Found y no procese la eliminación.
    
    Prioridad: Media
    """
    payload = json.dumps({"ids": ["a"]})  
    response = OrangeRequest.delete(category_url, headers=header, payload=payload)

    # Validaciones
    assert_status_code(response, 404)
    assert_error_message(response, 404, "Records Not Found")
    assert_resource_response_schema(response, "error_message_schema_response.json")
    log_request_response(category_url, response, header, payload)

    
@pytest.mark.regression
@pytest.mark.funcional
@pytest.mark.negativo
def test_BYT_T97_Eliminar_categoria_con_body_vacio(category_url, header):
    """
    Descripción: Verifica que al intentar eliminar una categoría enviando el body vacío,
    el sistema devuelva un código HTTP 404 Not Found y no procese la eliminación.
    
    Prioridad: Media
    """
    payload = json.dumps({})
    response = OrangeRequest.delete(category_url, headers=header, payload=payload)

    # Validaciones
    assert_status_code(response, 404)
    assert_error_message(response, 404, "Records Not Found")
    assert_resource_response_schema(response, "error_message_schema_response.json")
    log_request_response(category_url, response, header, payload)