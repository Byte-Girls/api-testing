def assert_valid_field(response, expected_valid: bool):
    actual_valid = response.json()["data"]["valid"]
    assert actual_valid is expected_valid, f"Valid campo esperado: {expected_valid}, pero se obtuvo {actual_valid}"

