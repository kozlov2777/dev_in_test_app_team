import subprocess
import time
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from utils.android_utils import capabilities
from selenium.common.exceptions import UnknownMethodException
import logging
import re


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


@pytest.fixture(autouse=True)
def set_log_level():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    yield


@pytest.fixture(scope='session')
def run_appium_server():
    subprocess.Popen(
        ['appium', '-a', '0.0.0.0', '-p', '4723', '--allow-insecure', 'adb_shell'],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        stdin=subprocess.DEVNULL,
        shell=True
    )
    time.sleep(5)


@pytest.fixture(scope='session')
def udid():
    result = subprocess.run(['adb', 'devices'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    devices = re.findall(r'^(\S+)\s+device$', result.stdout, re.M)
    if devices:
        return devices[0]
    else:
        raise Exception("No connected devices found.")


@pytest.fixture
def driver(udid, run_appium_server):
    capabilities_options = UiAutomator2Options().load_capabilities(capabilities(udid=udid))
    driver = webdriver.Remote(command_executor='http://localhost:4723',
                              options=capabilities_options)
    yield driver
    try:
        driver.delete_all_cookies()
    except UnknownMethodException as e:
        print('No cookies not found')
    driver.quit()



