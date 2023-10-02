import re
from utils.sidebar_elements import sidebar_help_title, sidebar_add_hub_title, sidebar_app_settings_title,\
    sidebar_video_surveillance, sidebar_report_a_problem, sidebar_terms_of_service


def test_sidebar_settings_button(side_bar_fixture):
    side_bar_fixture.click_app_setting_button()
    result = sidebar_app_settings_title(side_bar_fixture=side_bar_fixture)
    assert result.text == 'Settings'


def test_sidebar_help_button(side_bar_fixture):
    side_bar_fixture.click_help_button()
    result = sidebar_help_title(side_bar_fixture=side_bar_fixture)
    assert result.text == 'Installation Manuals'


def test_sidebar_report_a_problem_button(side_bar_fixture):
    side_bar_fixture.click_report_a_problem_button()
    result = sidebar_report_a_problem(side_bar_fixture=side_bar_fixture)
    assert result.text == 'Report a Problem'


def test_video_surveillance_button(side_bar_fixture):
    side_bar_fixture.click_video_surveillance_button()
    result = sidebar_video_surveillance(side_bar_fixture=side_bar_fixture)
    assert result.text == 'Video Surveillance'


def test_add_hub_button(side_bar_fixture):
    side_bar_fixture.click_add_hub_button()
    result = sidebar_add_hub_title(side_bar_fixture=side_bar_fixture)
    assert result.text == 'Add Hub'


def test_terms_of_service(side_bar_fixture):
    side_bar_fixture.click_terms_of_service()
    result = sidebar_terms_of_service(side_bar_fixture=side_bar_fixture)
    assert result.text == 'Terms of Service'


def test_version_format(side_bar_fixture):
    version = side_bar_fixture.find_version()
    version_pattern = r'^v \d+\.\d+\.\d+ \(build #\d+\)$'
    assert re.match(version_pattern, version)