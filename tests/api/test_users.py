def test_get_user(user_service):
  response = user_service.get_user(2)
  
  assert response.status_code == 200
  assert "data" in response.json()