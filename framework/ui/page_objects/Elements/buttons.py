from selenium.webdriver.common.by import By


class Buttons:

    def __init__(self, driver):
        self.driver = driver

    def click_login(self):
        self.driver.find_element(By.CSS_SELECTOR, '[id="login_button"]').click()

    def click_create_list(self):
        self.driver.find_element(By.CSS_SELECTOR, '[class ="rounded button border_color background_color teal"]').click()

    def click_continue(self):
        self.driver.find_element(By.CSS_SELECTOR, '[value="Continue"]').click()

    def click_save(self):
        self.driver.find_element(By.CSS_SELECTOR, '[value="Save"]').click()

    def click_delete_list(self):
        self.driver.find_element(By.CSS_SELECTOR, '[id="delete_list"]').click()

    def click_circle_remove(self):
        self.driver.find_element(By.CSS_SELECTOR, '[class ="glyphicons_v2 circle-remove"]').click()

    def click_yes(self):
        self.driver.find_element(By.CSS_SELECTOR, '[class="k-widget k-window k-dialog"]').\
            find_element(By.CSS_SELECTOR, '[class="k-button k-primary"]').click()



    def click_no(self):
        self.driver.find_element(By.LINK_TEXT, 'no').click()