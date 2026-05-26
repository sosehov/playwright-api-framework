def test_get_user(api_client):
  response = api_client.get("/users/2")
  
  assert response.status_code == 200
  assert "data" in response.json()