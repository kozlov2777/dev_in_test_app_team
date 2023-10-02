import pytest

from framework.pages.login_page import LoginPage


@pytest.fixture(scope='function')
def user_login_fixture(driver):
    yield LoginPage(driver)