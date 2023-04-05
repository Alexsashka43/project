from selenium.webdriver.common.by import By


class InfoMessage:
    def __init__(self, driver):
        self.driver = driver

    def error_status_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, '[class="error_status card"]')

    def notification_success(self):
        self.driver.find_element(By.CSS_SELECTOR, '[class="notification success"]')