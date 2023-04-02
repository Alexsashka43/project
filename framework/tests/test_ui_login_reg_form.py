import allure
import pytest
from selenium.webdriver.common.by import By

from framework.configuration import User
from framework.ui.page_objects.Elements.info_message import InfoMessage
from framework.ui.page_objects.UserPage import UserPage


@allure.step(f'login success: login {User.LOGIN}, password {User.PASSWORD}')
@pytest.mark.ui
@pytest.mark.parametrize("user_name, user_password", [(f'{User.LOGIN}', f'{User.PASSWORD}')])
def test_positive_login(driver, base_url, user_name, user_password):
    UserPage(driver).login(base_url, user_name, user_password)
    assert driver.find_element(By.LINK_TEXT, f'{user_name}')


@allure.step(f'login success: login {User.LOGIN}, password {User.PASSWORD}')
@pytest.mark.skip("Limited number of login attempts.")
@pytest.mark.ui
@pytest.mark.regress
@pytest.mark.parametrize("user_name, user_password", [('', ''),
                                                      (f'test', f'test'),
                                                      (f'test', f'{User.PASSWORD}'),
                                                      (f'{User.LOGIN}', f'test')])
def test_negative_login(driver, base_url, user_name, user_password):
    UserPage(driver).login(base_url, user_name, user_password)
    InfoMessage(driver).error_status_cart()
