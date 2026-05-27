from core.data.user_data import UserData

def test_get_user(user_service):
  response = user_service.get_user(UserData.VALID_USER_ID)
  
  assert response.status_code == 200
  assert "data" in response.json()
  
def test_get_invalid_user(user_service):
  response = user_service.get_user(UserData.INVALID_USER_ID)
  assert response.status_code == 404