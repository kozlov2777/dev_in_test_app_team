from framework.locators.side_bar_locators import SideBarLocators


def sidebar_app_settings_title(side_bar_fixture):
    result = side_bar_fixture.find_element(*SideBarLocators.TITLE_SETTING)
    return result


def sidebar_help_title(side_bar_fixture):
    result = side_bar_fixture.find_element(*SideBarLocators.TITLE_HELP)
    return result


def sidebar_report_a_problem(side_bar_fixture):
    result = side_bar_fixture.find_element(*SideBarLocators.TITLE_REPORT_A_PROBLEM)
    return result


def sidebar_video_surveillance(side_bar_fixture):
    result = side_bar_fixture.find_element(*SideBarLocators.TITLE_VIDEO)
    return result


def sidebar_add_hub_title(side_bar_fixture):
    result = side_bar_fixture.find_element(*SideBarLocators.TITLE_ADD_HUB)
    return result


def sidebar_terms_of_service(side_bar_fixture):
    result = side_bar_fixture.find_element(*SideBarLocators.TITLE_TERMS_OF_SERVICE)
    return result

