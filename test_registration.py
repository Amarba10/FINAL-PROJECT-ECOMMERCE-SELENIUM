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
    #     "browserName": "chrome",
    #     "platformName": "MAC"
    # }
    #
    # # selenium grid
    # driver = webdriver.Remote("http://localhost:4444",desired_capabilities= dc)

    yield driver
    driver.close()


# Positive Scenario
def test_registration(driver):
    driver.get('https://www.etsy.com/')
    driver.maximize_window()
    driver.find_element(By.CSS_SELECTOR,
                        "#gnav-header-inner > div.wt-flex-shrink-xs-0 > nav > ul > li:nth-child(1) > button").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR,
                        "#join-neu-form > div.wt-grid.wt-grid--block > div > div:nth-child(1) > div > button").click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, "#join_neu_email_field").send_keys("Barake10@gmail.com")
    driver.find_element(By.CSS_SELECTOR, "#join_neu_first_name_field").send_keys("Amar")
    driver.find_element(By.CSS_SELECTOR, "#join_neu_password_field").send_keys("12345678@")
    driver.find_element(By.CSS_SELECTOR, "#join-neu-form > div.wt-grid.wt-grid--block > div > div:nth-child(9) > div > button").click()
    time.sleep(5)
    msg = driver.find_element(By.CSS_SELECTOR,".wt-p-md-3")
    txt = msg.text
    assert "Welcome to Etsy,Amar!" == txt

# #Negative Scenario
def test_Invalid_Email(driver):
    driver.get('https://www.etsy.com/')
    driver.maximize_window()
    driver.find_element(By.CSS_SELECTOR,"#gnav-header-inner > div.wt-flex-shrink-xs-0 > nav > ul > li:nth-child(1) > button").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#join_neu_email_field").send_keys("amar@gmail.com")
    driver.find_element(By.CSS_SELECTOR, "#join_neu_password_field").send_keys("12345678@")
    time.sleep(4)
    driver.find_element(By.CSS_SELECTOR, "#join-neu-form > div.wt-grid.wt-grid--block > div > div:nth-child(10) > div > button").click()
    time.sleep(2)
    invalid_message = driver.find_element(By.CSS_SELECTOR, "#aria-join_neu_password_field-error")
    err_invalid = invalid_message.text
    assert "Password was incorrect" == err_invalid
    time.sleep(5)


def test_mandatory_message(driver):
    driver.get('https://www.etsy.com/')
    driver.maximize_window()
    driver.find_element(By.CSS_SELECTOR,"#gnav-header-inner > div.wt-flex-shrink-xs-0 > nav > ul > li:nth-child(1) > button").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#join-neu-form > div.wt-grid.wt-grid--block > div > div:nth-child(1) > div > button").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#join_neu_email_field").send_keys("amar.ba@gmail.com")
    driver.find_element(By.CSS_SELECTOR, "#join_neu_first_name_field").send_keys("")
    driver.find_element(By.CSS_SELECTOR, "#join_neu_password_field").send_keys("12345678@")
    driver.find_element(By.CSS_SELECTOR, "#join-neu-form > div.wt-grid.wt-grid--block > div > div:nth-child(9) > div > button").click()
    time.sleep(5)
    err_message = driver.find_element(By.CSS_SELECTOR, "#aria-join_neu_first_name_field-error")
    err_text = err_message.text
    assert "First name can't be blank." == err_text
    time.sleep(1)

def test_incoorect_values(driver):
    driver.get('https://www.etsy.com/')
    driver.maximize_window()
    driver.find_element(By.CSS_SELECTOR,"#gnav-header-inner > div.wt-flex-shrink-xs-0 > nav > ul > li:nth-child(1) > button").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#join-neu-form > div.wt-grid.wt-grid--block > div > div:nth-child(1) > div > button").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#join_neu_email_field").send_keys("121143424")
    driver.find_element(By.CSS_SELECTOR, "#join_neu_first_name_field").send_keys("2312")
    driver.find_element(By.CSS_SELECTOR, "#join_neu_password_field").send_keys("basdasd")
    driver.find_element(By.CSS_SELECTOR, "#join-neu-form > div.wt-grid.wt-grid--block > div > div:nth-child(9) > div > button").click()
    time.sleep(6)
    invalidContent = driver.find_element(By.CSS_SELECTOR,"#aria-join_neu_email_field-error")
    txt = invalidContent.text
    assert "Please enter a valid email address." == txt
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "#join_neu_email_field").send_keys("vsds@gmail.com")
    driver.find_element(By.CSS_SELECTOR, "#join_neu_first_name_field").send_keys("2312")
    driver.find_element(By.CSS_SELECTOR, "#join_neu_password_field").send_keys("basdasd")
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR,  "#join-neu-form > div.wt-grid.wt-grid--block > div > div:nth-child(9) > div > button").click()
    time.sleep(4)
    invalidUsername = driver.find_element(By.CSS_SELECTOR, "#aria-join_neu_first_name_field-error")
    txt1 = invalidUsername.text
    assert "Your first name contains invalid characters." == txt1

def test_search_product(driver):
    driver.get('https://www.etsy.com/')
    driver.maximize_window()
    # driver.find_element(By.CSS_SELECTOR, "#gnav-header-inner > div.wt-flex-shrink-xs-0 > nav > ul > li:nth-child(1) > button").click()
    # time.sleep(2)
    # driver.find_element(By.CSS_SELECTOR, "#join_neu_email_field").send_keys("amar.ba@gmail.com")
    # driver.find_element(By.CSS_SELECTOR, "#join_neu_password_field").send_keys("12345678@")
    # time.sleep(2)
    # driver.find_element(By.CSS_SELECTOR,"#join-neu-form > div.wt-grid.wt-grid--block > div > div:nth-child(10) > div > button").click()
    # time.sleep(2)
    element = driver.find_element(By.ID, "catnav-primary-link-10923")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(5)
    driver.find_element(By.ID, "catnav-l4-10927").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".wt-block-grid__item:nth-child(1) .wt-circle").click()
    name= driver.find_element(By.CSS_SELECTOR,"#content > div > div.wt-bg-white.wt-grid__item-md-12.wt-pl-xs-1.wt-pr-xs-0.wt-pr-md-1.wt-pl-lg-0.wt-pr-lg-0.wt-mt-xs-0.wt-overflow-x-hidden.wt-bb-xs-1 > div > div.wt-mt-xs-2.wt-text-black > div.wt-grid.wt-pl-xs-0.wt-pr-xs-1.search-listings-group > div:nth-child(2) > div.wt-bg-white.wt-display-block.wt-pb-xs-2.wt-mt-xs-0 > div > div > div > ul > li:nth-child(1) > div > div > a > div.v2-listing-card__info > div > h2")
    txt=name.text
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR,"#global-enhancements-search-query").send_keys(txt)
    driver.find_element(By.CSS_SELECTOR,"#gnav-search > div > div.wt-input-btn-group.global-enhancements-search-input-btn-group.wt-menu__trigger.emphasized_search_bar.emphasized_search_bar_grey_bg > button").click()
    time.sleep(3)
    tshirt = driver.find_element(By.CSS_SELECTOR,"#content > div > div.wt-bg-white.wt-grid__item-md-12.wt-pl-xs-1.wt-pr-xs-0.wt-pr-md-1.wt-pl-lg-0.wt-pr-lg-0.wt-bb-xs-1 > div > div.wt-mt-xs-3.wt-text-black > div.wt-grid.wt-pl-xs-0.wt-pr-xs-1.search-listings-group > div:nth-child(3) > div.wt-bg-white.wt-display-block.wt-pb-xs-2.wt-mt-xs-0 > div:nth-child(1) > div > div > ul > li:nth-child(1) > div > div > a.listing-link.wt-display-inline-block.bec759db0692125bd.logged > div.v2-listing-card__info > div > h3")
    result=tshirt.text
    assert result == txt
