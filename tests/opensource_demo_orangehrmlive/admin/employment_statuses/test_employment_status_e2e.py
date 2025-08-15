import pytest
import json
from src.assertions.common_assertions import assert_status_code
from src.utils.loggers_helpers import log_request_response
from src.orange_api.api_request import OrangeRequest
from faker import Faker

faker = Faker()

@pytest.mark.e2e
def test_employment_status_e2e(statuses_url, header, new_employment_status):
    
    # Create employment status
    create_response = OrangeRequest.post(statuses_url, headers=header, payload=new_employment_status)
    assert_status_code(create_response, expected_status=200)
    log_request_response(statuses_url, create_response, header, payload=new_employment_status)
    
    # Get employment status
    status_id = create_response.json()["data"]["id"]
    statuses_url_with_id = f"{statuses_url}/{status_id}"
    get_response = OrangeRequest.get(statuses_url_with_id, headers=header)
    assert_status_code(get_response, expected_status=200)
    log_request_response(statuses_url, get_response, header)
    
    # Put employment status
    url = f"{statuses_url}/{status_id}"
    payload_put = json.dumps({
    "id": status_id,
    "name" : "Short-Term Part-Time123"
    })
    put_response = OrangeRequest.put(url, headers=header, payload=payload_put)
    assert_status_code(put_response, expected_status=200)
    
    # Delete employment status
    status_id_to_delete = json.dumps({"ids": [status_id]})
    delete_response = OrangeRequest.delete(statuses_url, headers=header, payload=status_id_to_delete)
    assert_status_code(get_response, expected_status=200)
    log_request_response(statuses_url, delete_response, header, payload=status_id_to_delete)

    # Employee status does not exist
    statuses_url_with_id = f"{statuses_url}/{status_id}"
    get_response = OrangeRequest.get(statuses_url_with_id, headers=header)
    assert_status_code(get_response, expected_status=404)
    log_request_response(statuses_url, get_response, header)
    