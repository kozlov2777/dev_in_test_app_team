import logging
from appium.webdriver.webdriver import WebDriver


class Page:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.driver.implicitly_wait(25)

    def find_element(self, by, value):
        try:
            element = self.driver.find_element(by, value)
            return element
        except Exception as e:
            logging.error(e)
            raise e

    def click_element(self, by, value):
        element = self.find_element(by, value)
        try:
            element.click()
        except Exception as e:
            logging.error(e)
            raise e

    def enter_text(self, by, value, text):
        element = self.find_element(by, value)
        try:
            element.clear()
            element.send_keys(text)

        except Exception as e:
            logging.error(e)
            raise e