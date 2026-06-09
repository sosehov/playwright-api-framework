from pydantic import ValidationError


class ResponseValidator:

    @staticmethod
    def assert_status_code(response, expected_code: int):
        assert (
            response.status_code == expected_code
        ), f"Expected {expected_code}, got {response.status_code}"

    @staticmethod
    def assert_key_in_response(response_json: dict, key: str):
        assert key in response_json, f"Missing key: {key}"

    @staticmethod
    def assert_response_is_empty(response_json: dict):
        assert response_json == {}, f"Expected empty response, got {response_json}"

    @staticmethod
    def assert_valid_schema(response_json, model):
        try:
            model(**response_json)
        except ValidationError as e:
            assert False, f"Schema validation failed: {e}"
