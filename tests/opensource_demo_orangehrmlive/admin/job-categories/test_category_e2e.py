import pytest
import json
from faker import Faker
from src.assertions.common_assertions import assert_status_code
from src.utils.loggers_helpers import log_request_response
from src.orange_api.api_request import OrangeRequest

faker = Faker()

@pytest.mark.e2e
def test_E2E_job_category(category_url, header):
    """
    Escenario E2E: Crear, actualizar, obtener y eliminar una categoría de trabajo.
    """

    # ---------- 0) nombre único para evitar 422 por duplicado ----------
    name = faker.unique.word().capitalize() + " " + faker.unique.lexify(text="????")

    # ---------- 1) Crear categoría (con 1 reintento si 422) ----------
    create_payload = json.dumps({"name": name})
    create_response = OrangeRequest.post(category_url, headers=header, payload=create_payload)
    log_request_response(category_url, create_response, header, payload=create_payload)

    if create_response.status_code == 422:
        # Reintento con otro nombre
        name = faker.unique.word().capitalize() + " " + faker.unique.lexify(text="????")
        create_payload = json.dumps({"name": name})
        create_response = OrangeRequest.post(category_url, headers=header, payload=create_payload)
        log_request_response(category_url, create_response, header, payload=create_payload)

    assert_status_code(create_response, expected_status=200)
    category_id = create_response.json()["data"]["id"]

    # ---------- 2) Actualizar categoría ----------
    new_name = f"{name} - {faker.word().capitalize()}"
    update_payload = json.dumps({"name": new_name})
    update_url = f"{category_url}/{category_id}"
    update_response = OrangeRequest.put(update_url, headers=header, payload=update_payload)
    log_request_response(update_url, update_response, header, payload=update_payload)
    assert_status_code(update_response, expected_status=200)

    # ---------- 3) Obtener categoría actualizada ----------
    get_url = f"{category_url}/{category_id}"
    get_response = OrangeRequest.get(get_url, headers=header)
    log_request_response(get_url, get_response, header)
    assert_status_code(get_response, expected_status=200)
    assert get_response.json()["data"]["name"] == new_name, \
        f"El nombre no se actualizó correctamente: {get_response.text}"

    # ---------- 4) Eliminar categoría ----------
    delete_payload = json.dumps({"ids": [category_id]})
    delete_response = OrangeRequest.delete(category_url, headers=header, payload=delete_payload)
    log_request_response(category_url, delete_response, header, payload=delete_payload)
    assert_status_code(delete_response, expected_status=200)

    # ---------- 5) Verificar eliminación ----------
    get_after_delete = OrangeRequest.get(get_url, headers=header)
    log_request_response(get_url, get_after_delete, header)
    assert_status_code(get_after_delete, expected_status=404)
