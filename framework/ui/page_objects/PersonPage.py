import allure
from selenium.webdriver.common.by import By

from framework.ui.page_objects.BasePage import BasePage


class PersonPage(BasePage):
    @allure.step
    def open_page_person(self, base_url):
        self.logger.info(f'Open page')
        self.driver.get(f'{base_url}person')
        assert self.driver.find_element(By.CSS_SELECTOR, '[class ="results flex results_profile_card"]')

    @allure.step
    def profile(self, base_url):
        self.logger.info(f'Person profile')
        self.driver.get(f'{base_url}person')
        self.driver.find_element(By.CSS_SELECTOR, '[class="item profile card"]').click()
        assert self.driver.find_element(By.CSS_SELECTOR, '[class="page_wrap person_wrap"]')
