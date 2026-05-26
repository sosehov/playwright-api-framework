class UserService:
  def __init__(self, api_client):
    self.api_client = api_client
    
  def get_user(self, user_id: int):
    return self.api_client.get(f"/users/{user_id}")
  
  def create_user(self, payload: dict):
    return self.api_client.post("/users", json=payload)
  