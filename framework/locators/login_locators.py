from appium.webdriver.common.appiumby import By


class LoginLocators:
    BUTTON_LOGIN = (By.XPATH, '//android.widget.Button')
    USERNAME_INPUT = (By.XPATH, '//android.widget.FrameLayout[1]/androidx.compose.ui.platform.ComposeView/android.view.View/android.widget.EditText')
    PASSWORD_INPUT = (By.XPATH, '//android.widget.FrameLayout[2]/androidx.compose.ui.platform.ComposeView/android.view.View/android.widget.EditText')
    RESET_PASSWORD = (By.XPATH,'//androidx.recyclerview.widget.RecyclerView[1]/android.widget.FrameLayout[3]/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.TextView')
    LOGIN_BUTTON = (By.XPATH, '//androidx.recyclerview.widget.RecyclerView[2]/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.Button')
    ERROR_MESSAGE_INVALID_EMAIL_FORMAT = (By.XPATH, '//android.widget.LinearLayout/android.widget.TextView')
    ERROR_MESSAGE_WRONG_LOGIN_OR_PASSWORD = (By.XPATH, '//android.widget.LinearLayout/android.widget.TextView')
    CHANGE_PASSWORD_BUTTON = (By.XPATH, '//android.view.View[1]/android.widget.TextView')
    ADD_HUB_BUTTON = (By.XPATH, '//android.widget.LinearLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView')
    SIDEBAR_BUTTON = (By.XPATH, '//android.view.ViewGroup/android.widget.FrameLayout/android.widget.ImageView')
