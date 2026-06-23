import pytest
from core.services.user_service import UserService

# In a real project with persistent data, use yield + teardown here:
# yield user_service
# user_service.delete_user(created_id)


@pytest.fixture
def user_service(api_client):
    return UserService(api_client)
