import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions as EC

class TestTestRegistration():
    def setup_method(self):
        chrome_driver_binary = "./drivers/chromedriver 2"
        ser_chrome = ChromeService(chrome_driver_binary)
        self.driver = webdriver.Chrome(service=ser_chrome)

    def teardown_method(self):
        self.driver.quit()



    def test_testRegistration(self):
        self.driver.get("https://www.calvinklein.us/en")

        self.driver.maximize_window()
        time.sleep(3)
        login_btn = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#headerLogin")))
        login_btn.click()
        self.driver.find_element(By.CSS_SELECTOR, "#loginMenu > div:nth-child(1) > a").click()
        self.driver.find_element(By.ID, "WC_UserRegistrationAddForm_FormInput_email1_In_Register_1").click()
        self.driver.find_element(By.ID, "WC_UserRegistrationAddForm_FormInput_email1_In_Register_1").send_keys(
            "abam@hotmail.com")
        self.driver.find_element(By.ID, "WC_UserRegistrationAddForm_FormInput_logonPassword_In_Register_1").send_keys(
            "12345678aa")
        self.driver.find_element(By.ID,
                                 "WC_UserRegistrationAddForm_FormInput_logonPasswordVerify_In_Register_1").send_keys(
            "12345678aa")
        self.driver.find_element(By.ID, "WC_UserRegistrationAddForm_links_1").click()
        element = self.driver.find_element(By.ID, "WC_UserRegistrationAddForm_links_1")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
