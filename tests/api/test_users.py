from core.data.user_data import UserData
from core.validators.response_validator import ResponseValidator

def test_get_user(user_service):
  response = user_service.get_user(UserData.VALID_USER_ID)
  
  ResponseValidator.assert_status_code(response, 200)
  
  body = response.json()
  ResponseValidator.assert_key_in_response(body, "data")
  
def test_get_invalid_user(user_service):
    response = user_service.get_user(UserData.INVALID_USER_ID)
    ResponseValidator.assert_status_code(response, 404)
    
    body = response.json()
    ResponseValidator.assert_response_is_empty(body)
    
def test_get_negative_user_id(user_service):
    response = user_service.get_user(UserData.NEGATIVE_USER_ID)
    ResponseValidator.assert_status_code(response, 404)
  