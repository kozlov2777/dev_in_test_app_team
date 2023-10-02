import pytest
from utils.login_elements import login_error_message_invalid_email, login_error_message_wrong_login_or_password,\
    login_reset_password_button, login_success_button_add_hub


class TestLogin:
    @pytest.mark.parametrize("email, password", [
        pytest.param(
            "qa.ajax.app.automation",
            "qa_automation_password",
            id='test_login_error_email_wrong_format_without_email_domain'
        ),
        pytest.param(
            "qa.ajax.app.automationgmail.com",
            "qa_automation_password",
            id='test_login_error_email_wrong_format_without_@'
        ),
        pytest.param(
            "@gmail.com",
            "qa_automation_password",
            id='test_login_error_email_wrong_format_without_email_nickname'
        ),
        pytest.param(
            "qa.ajax.app.automation@gmai!l.com",
            "qa_automation_password",
            id='test_login_error_email_wrong_format_with_invalid_email_domain'
        ),
        pytest.param(
            "qa.ajax.app.automation@com",
            "qa_automation_password",
            id='test_login_error_email_wrong_format_without_domain'
        )

    ])
    def test_login_error_invalid_email_format(self, user_login_fixture, email, password):
        user_login_fixture.open_login()
        user_login_fixture.enter_username(username=email)
        user_login_fixture.enter_password(password=password)
        user_login_fixture.click_login_button()
        result = login_error_message_invalid_email(user_login_fixture=user_login_fixture)
        assert result.text == 'Invalid email format'

    @pytest.mark.parametrize("email, password", [
        pytest.param(
            "qa.ajax.app.automation@gmail.com",
            "qa_au",
            id='test_login_error_password_wrong_format_min_length-1'
        ),
        pytest.param(
            "qa.ajax.app.automation@gmail.com",
            "qa_automation_password1",
            id='test_login_error_password_wrong_format_without_upper_case_letter'
        ),
        pytest.param(
            "qa.ajax.app.automation@gmail.com",
            "qa_automation_password",
            id='test_login_error_password_wrong_format_without_upper_case_letter_and_digits'
        ),
        pytest.param(
            "qa.ajax.app.automation@gmail.com",
            "QA_AUTOMATION_PASSWORD",
            id='test_login_error_password_wrong_format_without_lower_case_letter'
        ),
        pytest.param(
            "qa.ajax.app.automation@gmail.com",
            "QA_automation_password",
            id='test_login_error_password_wrong_format_without_digits'
        ),
        pytest.param(
            "qa.ajax.app.automation@gmail.com",
            "QAautomationpassword1",
            id='test_login_error_password_wrong_format_without_special_character'
        )

    ])
    def test_login_error_invalid_password_format(self, user_login_fixture, email, password):
        user_login_fixture.open_login()
        user_login_fixture.enter_username(username=email)
        user_login_fixture.enter_password(password=password)
        user_login_fixture.click_login_button()
        result = login_error_message_wrong_login_or_password(user_login_fixture=user_login_fixture)
        assert result.text == 'Wrong login or password'

    @pytest.mark.parametrize("email, password", [
        pytest.param(
            "qa.ajax.app.automation",
            '',
            id='test_login_error_email_without_password'
        ),
        pytest.param(
            '',
            'qa_automation_password',
            id='test_login_error_email_without_password'
        )
    ])
    def test_login_error_button(self, user_login_fixture, email, password):
        user_login_fixture.open_login()
        user_login_fixture.enter_username(username=email)
        user_login_fixture.enter_password(password=password)
        is_button_clickable = user_login_fixture.is_clickable_login_button()
        assert is_button_clickable

    def test_reset_password_button(self, user_login_fixture):
        user_login_fixture.open_login()
        user_login_fixture.click_reset_password()
        result = login_reset_password_button(user_login_fixture=user_login_fixture)
        assert result.text == 'Change Password'


    @pytest.mark.parametrize("email, password", [
        pytest.param(
            "qa.ajax.app.automation@gmail.com",
            "qa_automation_password",
            id='test_login_success'
        )
    ])
    def test_login_success(self, user_login_fixture, email, password):
        user_login_fixture.open_login()
        user_login_fixture.enter_username(username=email)
        user_login_fixture.enter_password(password=password)
        user_login_fixture.click_login_button()
        result = login_success_button_add_hub(user_login_fixture=user_login_fixture)
        assert result.text == 'Add Hub'

