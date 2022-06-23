import time

from selenium.common import NoSuchElementException, ElementNotInteractableException, TimeoutException, \
    StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome import webdriver
# from selenium.webdriver.firefox import webdriver
from selenium import webdriver
# from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.firefox.service import Service as firefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


import pytest


@pytest.fixture()
def driver():
    chrome_driver_binary = r"./chromedriver 2"
    ser_chrome = ChromeService(chrome_driver_binary)
    driver = webdriver.Chrome(service=ser_chrome)

    # driver = webdriver.Safari()

    # Firefox_driver_binary = r"./drivers/geckodriver"
    # ser_firefox = FirefoxService(Firefox_driver_binary)
    # driver = webdriver.Firefox(service=ser_firefox)

    # dc = {
    #     "browseName": "chrome",
    #     "platformName": "MAC"
    # }
    #
    # # selenium grid
    # driver = webdriver.Remote("http://localhost:4444",desired_capabilities= dc)

    yield driver
    driver.close()


def test_registration(driver):
    driver.get('https://www.etsy.com/')
    driver.maximize_window()
    driver.find_element(By.CSS_SELECTOR,"#gnav-header-inner > div.wt-flex-shrink-xs-0 > nav > ul > li:nth-child(1) > button").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,"#join-neu-form > div.wt-grid.wt-grid--block > div > div:nth-child(1) > div > button").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR,"#join_neu_email_field").send_keys("amar.ba@gmail.com")
    driver.find_element(By.CSS_SELECTOR,"#join_neu_first_name_field").send_keys("Amar")
    driver.find_element(By.CSS_SELECTOR, "#join_neu_password_field").send_keys("12345678@")
    driver.find_element(By.CSS_SELECTOR,"#join-neu-form > div.wt-grid.wt-grid--block > div > div:nth-child(9) > div > button").click()
    time.sleep(2)
    err_message=driver.find_element(By.CSS_SELECTOR,"#aria-join_neu_email_field-error")
    err_text=err_message.text
    assert "Sorry, the email you have entered is already in use." == err_text