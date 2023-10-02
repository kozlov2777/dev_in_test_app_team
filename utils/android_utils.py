def capabilities(udid):
    capabilities = dict(
        autoGrantPermissions=True,
        automationName='uiautomator2',
        newCommandTimeout=500,
        noSign=True,
        deviceName=udid,
        platformName='Android',
        platformVersion='11',
        resetKeyboard=True,
        systemPort=8301,
        takesScreenshot=True,
        udid=udid,
        appPackage='com.ajaxsystems',
        appActivity='com.ajaxsystems.ui.activity.LauncherActivity',
    )
    return capabilities
