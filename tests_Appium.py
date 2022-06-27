import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from appium import webdriver

@pytest.fixture()
def driver():
    dc = {
        'platformName': 'Android',
        'platformVersion': ' 8.1',
        'deviceName': 'Pixel 2 API 27',
        'automationName': 'Appium',
        'browserName': 'Chrome'
    }
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities=dc)
    yield driver
    driver.close()

def test_google(driver):
    driver.get("https://www.google.com/webhp?hl=iw&sa=X&ved=0ahUKEwiaoaiVic74AhUogv0HHal2An8QPAgI")
    time.sleep(5)