from framework.pages.page import Page
from framework.locators.side_bar_locators import SideBarLocators


class SideBarPage(Page):
    def click_app_setting_button(self):
        self.click_element(*SideBarLocators.APP_SETTINGS)

    def click_help_button(self):
        self.click_element(*SideBarLocators.HELP_BUTTON)

    def click_report_a_problem_button(self):
        self.click_element(*SideBarLocators.REPORT_A_PROBLEM)

    def click_video_surveillance_button(self):
        self.click_element(*SideBarLocators.VIDEO_SURVEILLANCE)

    def click_add_hub_button(self):
        self.click_element(*SideBarLocators.ADD_HUB_BUTTON)

    def click_terms_of_service(self):
        self.click_element(*SideBarLocators.TERMS_OF_SERVICE)

    def find_version(self):
        version = self.find_element(*SideBarLocators.VERSION).text
        return version