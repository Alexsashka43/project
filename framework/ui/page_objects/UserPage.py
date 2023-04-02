import allure

from framework.ui.page_objects.BasePage import BasePage
from framework.ui.page_objects.Elements.buttons import Buttons
from framework.ui.page_objects.Elements.fields import Fields


class UserPage(BasePage):

    @allure.step
    def login(self, base_url, user_name, user_password):
        self.logger.info(f'Login: {user_name}')
        self.driver.get(f'{base_url}login')
        Fields(self.driver).field_username(user_name)
        Fields(self.driver).field_password(user_password)
        Buttons(self.driver).click_login()
