import pytest
from selenium import webdriver


@pytest.fixture
def get_webdriver():
    driver = webdriver.Firefox()
    return driver


@pytest.fixture(scope='function')
def setup_homepage(get_webdriver):
    driver = get_webdriver
    url = 'https://ginandjuice.shop/'
    driver.get(url)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def setup_login_page(get_webdriver):
    driver = get_webdriver
    url = 'https://ginandjuice.shop/login'
    driver.get(url)
    yield driver
    driver.quit()
