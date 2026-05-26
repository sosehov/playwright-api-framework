import requests

class APIClient:
  def __init__(self, base_url: str, headers: dict = None):
    self.base_url = base_url
    self.session = requests.Session()
    self.session.headers.update(headers or {})
  
  def get(self, endpoint: str, **kwargs):
    return self.session.get(f"{self.base_url}{endpoint}", **kwargs)
  
  def post(self, endpoint: str, json: dict = None, **kwargs):
    return self.session.post(f"{self.base_url}{endpoint}", json=json, **kwargs)
  
  def put(self, endpoint: str, json: dict = None, **kwargs):
    return self.session.put(f"{self.base_url}{endpoint}", json=json, **kwargs)
  
  def delete(self, endpoint: str, **kwargs):
    return self.session.delete(f"{self.base_url}{endpoint}", **kwargs)