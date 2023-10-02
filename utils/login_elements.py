from framework.locators.login_locators import LoginLocators


def login_error_message_invalid_email(user_login_fixture):
    result = user_login_fixture.find_element(*LoginLocators.ERROR_MESSAGE_INVALID_EMAIL_FORMAT)
    return result


def login_error_message_wrong_login_or_password(user_login_fixture):
    result = user_login_fixture.find_element(*LoginLocators.ERROR_MESSAGE_WRONG_LOGIN_OR_PASSWORD)
    return result


def login_reset_password_button(user_login_fixture):
    result = user_login_fixture.find_element(*LoginLocators.CHANGE_PASSWORD_BUTTON)
    return result


def login_success_button_add_hub(user_login_fixture):
    result = user_login_fixture.find_element(*LoginLocators.ADD_HUB_BUTTON)
    return result
