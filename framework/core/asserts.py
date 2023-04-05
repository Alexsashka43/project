import allure
import json
import jsonref
from requests import Response
from jsonschema import validate
from os.path import dirname, join


class Asserts:
    @staticmethod
    def assert_equals(val1, val2, error_massage: str = ""):
        assert val1 == val2, f"Failed assertion that {val1} is equals {val2}. {error_massage}"

    @staticmethod
    def assert_code_status(response: Response, expected_code: int, message: str = ""):
        assert response.status_code == expected_code, \
            f'Expected status code {expected_code}, but got {response.status_code}. {response.text}'

    @staticmethod
    def assert_response_text(response: Response, expected_text: str, message: str = ""):
        assert response.text == expected_text, \
            f'Expected response text "{expected_text}", but got "{response.text}". {message}'

    @staticmethod
    def assert_response_success(response: Response, message: str = ""):
        assert response.json()["success"] == True, \
            f'Expected response text: true, but got {response.json()["success"]}. {message}'

    @staticmethod
    def assert_response_false(response: Response, message: str = ""):
        assert response.json()["success"] == False, \
            f'Expected response text: false, but got {response.json()["success"]}. {message}'

    @staticmethod
    def assert_response_text_find(response_text, expected_text, message: str = ""):
        if expected_text not in response_text:
            assert False, f'Expected response text "{expected_text}", but got "{response_text}". {message}'

    @staticmethod
    def assert_json_value_by_key(response: Response, key: str, val: str):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f'Response is not in JSON format. Response text is "{response.text}"'

        assert key in response_as_dict, \
            f'Response json does\'n have key "{key}"'

        assert response_as_dict[key] == val, \
            f'Response key "{key}" has value {response_as_dict[key]} but expected is {val}'

    @staticmethod
    def assert_json_has_key(response: Response, key: str):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f'Response is not in JSON format. Response text is "{response.text}"'

        assert key in response_as_dict, \
            f'Response json does not have a key "{key}" which is expected. JSON text: "{response.text}"'

    @staticmethod
    def assert_json_has_no_key(response: Response, key: str):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f'Response is not in JSON format. Response text is "{response.text}"'

        assert key not in response_as_dict, \
            f'Response json has key "{key}" which is not expected.'

    @staticmethod
    def assert_response_has_headers(response: Response, key: str):
        assert key in response.headers, \
            f'Cannot find header with name {key} in the response. All headers in the response: ' \
            + str(response.headers)

    @staticmethod
    def assert_response_not_has_headers(response: Response, key: str):
        assert key not in response.headers, \
            f'Found header with name {key} in the response which is not expected.'

    @staticmethod
    def assert_time_is_less_than(response: Response, max_time=1):
        assert response.elapsed.total_seconds() <= max_time, "Request is too long."

    @staticmethod
    @allure.step('Returned JSON schema is correct')
    def assert_valid_schema(data, schema_file):
        """
        Verifies that the given data matches the JSON schema
        """
        schema_base_dir = join(dirname(dirname(__file__)), 'resources/json_schemas/')
        schema_file_path = f'{schema_base_dir}/{schema_file}'
        base_uri = f'file://{schema_base_dir}/'

        with open(schema_file_path) as schema_file:
            schema = jsonref.loads(schema_file.read(), base_uri=base_uri, jsonschema=True)
            return validate(data, schema)
