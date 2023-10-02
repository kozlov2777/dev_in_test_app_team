from framework.pages.page import Page
from framework.locators.login_locators import LoginLocators


class LoginPage(Page):
    def __init__(self, driver):
        super().__init__(driver)

    def open_login(self):
        self.click_element(*LoginLocators.BUTTON_LOGIN)

    def enter_username(self, username):
        self.enter_text(*LoginLocators.USERNAME_INPUT, username)

    def enter_password(self, password):
        self.enter_text(*LoginLocators.PASSWORD_INPUT, password)

    def click_login_button(self):
        self.click_element(*LoginLocators.LOGIN_BUTTON)

    def is_clickable_login_button(self):
        return self.find_element(*LoginLocators.LOGIN_BUTTON).get_attribute("clickable")

    def click_reset_password(self):
        self.click_element(*LoginLocators.RESET_PASSWORD)

