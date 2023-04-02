from selenium.webdriver.common.by import By


class Fields:

    def __init__(self, driver):
        self.driver = driver

    def field_username(self, username):
        self.driver.find_element(By.CSS_SELECTOR, '[id="username"]').send_keys(username)

    def field_password(self, password):
        self.driver.find_element(By.CSS_SELECTOR, '[id="password"]').send_keys(password)

    def field_name(self, name):
        self.driver.find_element(By.CSS_SELECTOR, '[id="name"]').send_keys(name)

    def field_description(self, description):
        self.driver.find_element(By.CSS_SELECTOR, '[id="description"]').send_keys(description)

    def field_item_search(self, name_film):
        self.driver.find_element(By.CSS_SELECTOR, '[id="list_item_search"]').send_keys(name_film)



