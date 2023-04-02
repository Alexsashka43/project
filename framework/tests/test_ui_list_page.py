import allure
import pytest

from framework.api.methods.api_methods_movie import MethodsTheMovieDB
from framework.configuration import User, UserList
from framework.ui.page_objects.ListPage import ListPage
from framework.ui.page_objects.UserPage import UserPage


@allure.step(f'Create_list: Name list: {UserList.NAME}, description list: {UserList.DESCRIPTION}')
@pytest.mark.parametrize("name, description", [(f'{UserList.NAME}', f'{UserList.DESCRIPTION}')])
def test_create_list(driver, base_url, name, description):
    UserPage(driver).login(base_url, User.LOGIN, User.PASSWORD)
    ListPage(driver).create_list(base_url, name, description)

@allure.step(f'Edit_list:Name list: Edit {UserList.NAME}, description list: Edit {UserList.DESCRIPTION}')
@pytest.mark.ui
@pytest.mark.parametrize("list_id", ['8247295'])
def test_edit_list(driver, base_url, list_id):
    UserPage(driver).login(base_url, User.LOGIN, User.PASSWORD)
    ListPage(driver).edit_list(base_url, list_id, UserList.NAME, UserList.DESCRIPTION)

@allure.step(f'Remove film')
@pytest.mark.ui
@pytest.mark.skip("Movie not added")
@pytest.mark.parametrize("list_id", ['8247295'])
def test_remote_film_to_list(driver, base_url, list_id, session_id):
    UserPage(driver).login(base_url, User.LOGIN, User.PASSWORD)
    MethodsTheMovieDB().add_movie_to_list(base_url, User.API_KEY, session_id, list_id, '76600')
    ListPage(driver).remove_film_from_list(base_url, list_id)

@allure.step('Delete_list')
@pytest.mark.ui
@pytest.mark.parametrize("list_id", ['8247157'])
def test_delete_list(driver, base_url, list_id):
    UserPage(driver).login(base_url, User.LOGIN, User.PASSWORD)
    ListPage(driver).delete_list(base_url, list_id)

