import allure
import pytest

from framework.ui.page_objects.PersonPage import PersonPage


@allure.step(f'Open page')
@pytest.mark.ui
def test_open_page(driver, base_url):
    PersonPage(driver).open_page_person(base_url)

@allure.step(f'Open profile')
@pytest.mark.ui
def test_profile(driver, base_url):
    PersonPage(driver).profile(base_url)






