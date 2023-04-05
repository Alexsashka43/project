import logging

import allure
import pytest

from framework.configuration import User
from framework.core.logger import Logger
import json
import os.path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from framework.core.data import Data

drivers = os.path.expanduser('drivers')
target = None
web_config = None
bearer_token = None


def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="https://www.themoviedb.org/")
    parser.addoption("--url_api", action="store", default="https://api.themoviedb.org/")
    parser.addoption("--bearer_token", action="store", default=bearer_token)
    parser.addoption("--drivers", default=os.path.expanduser("~/Downloads/drivers"))
    parser.addoption("--browser", default="chrome")
    parser.addoption("--executor", default="192.168.1.7")
    parser.addoption("--bversion")
    parser.addoption("--vnc", action="store_true", default=False)
    parser.addoption("--logs", action="store_true", default=False)
    parser.addoption("--video", action="store_true", default=True)


@pytest.fixture(scope="session", autouse=True)
def set_up():
    yield
    Logger.get_instance().write_log_to_file()


@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture
def base_url_api(request):
    return request.config.getoption("--url_api")


@pytest.fixture()
def api_key():
    api_key = User.API_KEY
    return api_key


@pytest.fixture()
def request_token():
    request_token = Data.file_open('new_token.json')['request_token']
    return request_token


@pytest.fixture()
def access_token():
    access_token = User.ACCESS_TOKEN
    return access_token


@pytest.fixture()
def session_id():
    session_id = Data.file_open('session_id.json')['session_id']
    return session_id


@pytest.fixture()
def list_id():
    list_id = Data.file_open('list_id.json')['list_id']
    return list_id


@pytest.fixture
def driver(request):
    driver = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")
    vnc = request.config.getoption("--vnc")
    logs = request.config.getoption("--logs")
    video = request.config.getoption("--video")
    version = request.config.getoption("--bversion")
    drivers = request.config.getoption("--drivers")

    options = webdriver.ChromeOptions()
    options.add_experimental_option('w3c', True)
    executor_url = f"http://{executor}:4444/wd/hub"

    if executor == 'local':
        if driver == "chrome":
            service = Service(executable_path=os.path.join(drivers, "chromedriver.exe"))
            browser = webdriver.Chrome(service=service, options=options)
        elif driver == "yandex":
            browser = webdriver.Chrome(executable_path=os.path.join(drivers, "yandexdriver.exe"), options=options)
        elif driver == "firefox":
            browser = webdriver.Firefox(executable_path=os.path.join(drivers, "geckodriver.exe"), options=options)
        elif driver == "edge":
            browser = webdriver.Edge(executable_path=os.path.join(drivers, "msedgedriver.exe"), options=options)
        elif driver == "safari":
            browser = webdriver.Safari(executable_path=os.path.join(drivers, "safaridriver.exe"), options=options)
        else:
            raise Exception("Driver not supported")


    else:

        capabilities = {
            'browserName': driver,
            'browserVersion': version,
            'selenoid:options': {
                'enableVNC': vnc,
                'enableVideo': video,
                'enableLog': logs,
            },
            'name': 'test',
        }

        browser = webdriver.Remote(
            desired_capabilities=capabilities,
            command_executor=executor_url,
            options=options
        )

    allure.attach(
        name=browser.session_id,
        body=json.dumps(browser.capabilities),
        attachment_type=allure.attachment_type.JSON,
    )

    def finalizer():
        browser.quit()

        # Add environment info to allure-report
        with open("allure-results/environment.xml", "w+") as file:
            file.write(f"""<environment>
                               <parameter>
                                   <key>Browser</key>
                                   <value>{browser}</value>
                               </parameter>
                               <parameter>
                                   <key>Browser.Version</key>
                                   <value>{version}</value>
                               </parameter>
                               <parameter>
                                   <key>Executor</key>
                                   <value>{executor_url}</value>
                               </parameter>
                           </environment>
                           """)

    browser.test_name = request.node.name
    browser.log_level = logging.DEBUG

    request.addfinalizer(finalizer)
    return browser
