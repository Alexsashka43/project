import allure
import pytest

from selenium.webdriver.common.by import By

from framework.configuration import User
from framework.api.methods.api_methods_movie import MethodsTheMovieDB
from framework.core.data import Data
from framework.ui.page_objects.UserPage import UserPage


@allure.step
@allure.title("Create request_token")
@pytest.mark.api
def test_create_request_token(base_url_api, api_key):
    response = MethodsTheMovieDB.create_request_token(base_url_api, api_key)
    data_response = response.json()
    Data.file_write(data_response, f'new_token.json')


@allure.step
@allure.title("Access token")
@pytest.mark.api
def test_access_token(driver, base_url, request_token):
    UserPage(driver).login(base_url, User.LOGIN, User.PASSWORD)
    driver.get(f'{base_url}authenticate/{request_token}')
    driver.find_element(By.CSS_SELECTOR, '[id="allow_authentication"]').click()


@allure.step
@allure.title("Create session")
@pytest.mark.api
def test_create_session_id(base_url_api, api_key, request_token):
    response = MethodsTheMovieDB.create_session_id(base_url_api, api_key, request_token)
    data_response = response.json()
    Data.file_write(data_response, f'session_id.json')


@allure.step
@allure.title("Create list with incorrect session_id")
@pytest.mark.api
def test_negative_create_list(base_url_api, api_key, session_id='test'):
    response = MethodsTheMovieDB.negative_create_list(base_url_api, api_key, session_id)
    data_response = response.json()
    Data.file_write(data_response, f'list_id.json')


@allure.step
@allure.title("Create list")
@pytest.mark.api
def test_create_list(base_url_api, api_key, session_id):
    response = MethodsTheMovieDB.create_list(base_url_api, api_key, session_id)
    data_response = response.json()
    Data.file_write(data_response, f'list_id.json')


@allure.step
@allure.title("Add film to list")
@pytest.mark.api
@pytest.mark.parametrize('movie_id', ['980078', '603692', '804150', '842945', '315162', '943822'])
def test_add_movie_list(base_url_api, api_key, list_id, movie_id, session_id):
    response = MethodsTheMovieDB.add_movie_to_list(base_url_api, api_key, session_id, list_id, movie_id)
    data_response = response.json()
    Data.file_write(data_response, f'add_to_list.json')


@allure.step
@allure.title("Add movie with incorrect id to list")
@pytest.mark.regress
@pytest.mark.api
@pytest.mark.parametrize('movie_id', ['-6576', '0', '603765435678', '****', 'test', 'тест'])
def test_negative_add_movie_list(base_url_api, api_key, list_id, movie_id, session_id):
    response = MethodsTheMovieDB.negative_add_movie_to_list(base_url_api, api_key, session_id, list_id, movie_id)
    data_response = response.json()
    Data.file_write(data_response, f'add_to_list.json')


@allure.step
@allure.title("Remove a movie")
@pytest.mark.api
@pytest.mark.parametrize('movie_id', ['980078', '804150', '842945'])
def test_remove_movie_list(base_url_api, api_key, list_id, movie_id, session_id):
    response = MethodsTheMovieDB.remove_movie_from_list(base_url_api, api_key, session_id, list_id, movie_id)
    data_response = response.json()
    Data.file_write(data_response, f'remove_from_list.json')


@allure.step
@allure.title("Remove a movie that is not in the list")
@pytest.mark.regress
@pytest.mark.api
@pytest.mark.parametrize('movie_id', ['1023313', '948276', '615173'])
def test_negative_remove_movie_list(base_url_api, api_key, list_id, movie_id, session_id):
    response = MethodsTheMovieDB.negative_remove_movie_from_list(base_url_api, api_key, session_id, list_id, movie_id)
    data_response = response.json()
    Data.file_write(data_response, f'remove_from_list.json')


@allure.step
@allure.title("Get list details")
@pytest.mark.regress
@pytest.mark.api
def test_get_details(base_url_api, api_key, list_id, language='en-US'):
    response = MethodsTheMovieDB.get_detail_list(base_url_api, api_key, list_id, language)
    data_response = response.json()
    Data.file_write(data_response, f'details_of_list.json')


@allure.step
@allure.title("Clear list")
@pytest.mark.regress
@pytest.mark.api
def test_clear_list(base_url_api, api_key, session_id, list_id):
    response = MethodsTheMovieDB.clear_list(base_url_api, api_key, session_id, list_id)
    data_response = response.json()
    Data.file_write(data_response, f'clear_list.json')


@allure.step
@pytest.mark.skip("Something went wrong with your request. Usually this is a permanent error.")
@pytest.mark.api
@allure.title("Delete list")
def test_delete_list(base_url_api, api_key, session_id, list_id):
    response = MethodsTheMovieDB.delete_list(base_url_api, api_key, session_id, list_id)
    data_response = response.json()
    Data.file_write(data_response, f'delete_list.json')
