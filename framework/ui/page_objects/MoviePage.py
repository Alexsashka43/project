import allure
from selenium.webdriver.common.by import By

from framework.ui.page_objects.BasePage import BasePage


class MoviePage(BasePage):
    @allure.step
    def sort_movie(self, base_url):
        self.logger.info(f'Sort film')
        self.driver.get(f'{base_url}movie')
        self.driver.find_element(By.LINK_TEXT, 'Sort').click()

