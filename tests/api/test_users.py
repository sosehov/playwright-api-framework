import pytest
from core.data.user_data import UserData
from core.factories.user_factory import UserFactory
from core.validators.response_validator import ResponseValidator


@pytest.mark.api
def test_get_user(user_service):
    response = user_service.get_user(UserData.VALID_USER_ID)

    ResponseValidator.assert_status_code(response, 200)

    body = response.json()
    ResponseValidator.assert_key_in_response(body, "data")


@pytest.mark.api
@pytest.mark.parametrize(
    "user_id", [UserData.INVALID_USER_ID, UserData.NEGATIVE_USER_ID]
)
def test_get_user_invalid_ids(user_service, user_id):
    response = user_service.get_user(user_id)
    ResponseValidator.assert_status_code(response, 404)

    body = response.json()
    ResponseValidator.assert_response_is_empty(body)


@pytest.mark.api
def test_create_dynamic_user(user_service):
    payload = UserFactory.valid_user()
    response = user_service.create_user(payload)
    ResponseValidator.assert_status_code(response, 201)
    body = response.json()
    ResponseValidator.assert_key_in_response(body, "id")


@pytest.mark.api
def test_update_user(user_service):
    payload = UserFactory.updated_user()
    response = user_service.update_user(UserData.VALID_USER_ID, payload)
    ResponseValidator.assert_status_code(response, 200)
    body = response.json()
    ResponseValidator.assert_key_in_response(body, "name")


@pytest.mark.api
def test_delete_user(user_service):
    response = user_service.delete_user(UserData.VALID_USER_ID)
    ResponseValidator.assert_status_code(response, 204)
