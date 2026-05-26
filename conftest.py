import pytest
from core.client.api_client import APIClient
from core.services.user_service import UserService
from core.config.config import BASE_URL_API, API_KEY

@pytest.fixture(scope="session")
def headers():
  return {
    "x-api-key": API_KEY,
    "Content_Type": "application/json"
  }

@pytest.fixture
def api_client(headers):
  return APIClient(BASE_URL_API, headers)

@pytest.fixture
def user_service(api_client):
  return UserService(api_client)