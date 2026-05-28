class ResponseValidator:
  
  @staticmethod
  def assert_status_code(response, expected_code: int):
    assert response.status_code == expected_code, (
      f"Expected {expected_code}, got {response.status_code}"
    )
    
  @staticmethod
  def assert_key_in_response(response_json: dict, key: str):
    assert key in response_json, f"Missing key: {key}"
