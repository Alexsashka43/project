import allure

from framework.ui.page_objects.BasePage import BasePage
from framework.ui.page_objects.Elements.buttons import Buttons
from framework.ui.page_objects.Elements.fields import Fields
from framework.ui.page_objects.Elements.info_message import InfoMessage


class ListPage(BasePage):
    @allure.step
    def create_list(self, base_url, name, description):
        self.logger.info(f'Name list: {name}')
        self.driver.get(f'{base_url}u/qwerty43567/lists')
        Buttons(self.driver).click_create_list()
        Fields(self.driver).field_name(name)
        Fields(self.driver).field_description(description)
        Buttons(self.driver).click_continue()

    @allure.step
    def edit_list(self, base_url, list_id, name, description):
        self.logger.info(f'Edit list: {name}')
        self.driver.get(f'{base_url}list/{list_id}/edit')
        Fields(self.driver).field_name(f'Edit {name}')
        Fields(self.driver).field_description(f'Edit {description}')
        Buttons(self.driver).click_save()
        InfoMessage(self.driver).notification_success()

    @allure.step
    def remove_film_from_list(self, base_url, list_id):
        self.logger.info(f'Remove film')
        self.driver.get(f'{base_url}list/{list_id}/edit?active_nav_item=step_2&sort_by=original_order.desc')
        Buttons(self.driver).click_circle_remove()
        InfoMessage(self.driver).notification_success()

    @allure.step
    def delete_list(self, base_url, list_id):
        self.logger.info(f'Delete list_id: {list_id}')
        self.driver.get(f'{base_url}list/{list_id}/edit?active_nav_item=delete')
        Buttons(self.driver).click_delete_list()
        Buttons(self.driver).click_yes()
