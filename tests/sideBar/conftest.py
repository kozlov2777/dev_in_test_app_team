import pytest
from framework.pages.sidebar_page import SideBarPage
from framework.locators.login_locators import LoginLocators


@pytest.fixture(scope='function')
def side_bar_fixture(driver):
    driver.find_element(*LoginLocators.BUTTON_LOGIN).click()
    driver.implicitly_wait(20)
    driver.find_element(*LoginLocators.USERNAME_INPUT).send_keys('qa.ajax.app.automation@gmail.com')
    driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys('qa_automation_password')
    driver.find_element(*LoginLocators.LOGIN_BUTTON).click()
    driver.implicitly_wait(20)
    driver.find_element(*LoginLocators.SIDEBAR_BUTTON).click()
    driver.implicitly_wait(20)
    yield SideBarPage(driver)