from appium.webdriver.common.appiumby import By


class SideBarLocators:
    APP_SETTINGS = (By.XPATH, "//android.widget.ScrollView[1]/android.view.View[1]")
    HELP_BUTTON = (By.XPATH, "//android.widget.ScrollView[1]/android.view.View[2]")
    REPORT_A_PROBLEM = (By.XPATH, "//android.widget.ScrollView[1]/android.view.View[3]")
    VIDEO_SURVEILLANCE = (By.XPATH, "//android.widget.ScrollView[1]/android.view.View[4]")
    ADD_HUB_BUTTON = (By.XPATH, "//android.widget.ScrollView[1]/android.view.View[5]/android.widget.Button")
    TERMS_OF_SERVICE = (By.XPATH, "//android.widget.ScrollView[3]/android.widget.TextView[1]")
    VERSION = (By.XPATH, '//android.widget.ScrollView[3]/android.widget.TextView[2]')
    TITLE_SETTING = (By.XPATH, "//android.widget.TextView")
    TITLE_HELP = (By.XPATH, "//android.widget.TextView")
    TITLE_REPORT_A_PROBLEM = (By.XPATH, "//android.widget.TextView")
    TITLE_VIDEO = (By.XPATH, "//android.view.ViewGroup[1]/android.widget.TextView")
    TITLE_ADD_HUB = (By.XPATH, "//android.widget.TextView")
    TITLE_TERMS_OF_SERVICE = (By.XPATH, '//android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView')
