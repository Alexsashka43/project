import allure
import pytest

from framework.ui.page_objects.MoviePage import MoviePage


# @allure.step(f'Create_list: Name list: {UserList.NAME}, description list: {UserList.DESCRIPTION}')
# @pytest.mark.parametrize("name, description", [(f'{UserList.NAME}', f'{UserList.DESCRIPTION}')])
# def test_sort_list(driver, base_url, name, description):
#     MoviePage(driver).login(base_url, User.LOGIN, User.PASSWORD)
#     ListPage(driver).create_list(base_url, name, description)