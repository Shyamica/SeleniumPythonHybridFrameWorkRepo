import time

import pytest
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageobjects.Homepage import Homepage


@pytest.mark.usefixtures("setup_and_teardown")
class TestRegister:
    def test_register_with_mandatory_fields(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            frame1 = wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//div["
                                                                                             "@id='__st_fancy_popup"
                                                                                             "']/iframe")))
            self.driver.switch_to.frame(frame1)
            self.driver.find_element(By.ID, "__st_bpn_no")
        except TimeoutException:
            print("TimeoutException got handled here")
            self.driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
            home_page = Homepage(self.driver)
            home_page.click_on_my_account()
            time.sleep(5)
            home_page.enter_mobile_number("9498499445")
            time.sleep(5)
            home_page.click_on_login_submit_button()
            time.sleep(5)
            home_page.enter_name("shyamica")
            time.sleep(5)
            home_page.enter_email("gangishyamica@gmail.com")
            time.sleep(15)
            home_page.click_on_submit_button_for_registering_the_account()
            time.sleep(5)

    def test_register_with_existing_email_id(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            frame1 = wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//div["
                                                                                             "@id='__st_fancy_popup"
                                                                                             "']/iframe")))
            self.driver.switch_to.frame(frame1)
            self.driver.find_element(By.ID, "__st_bpn_no")
        except TimeoutException:
            print("TimeoutException got handled here")
            self.driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
            home_page = Homepage(self.driver)
            home_page.click_on_my_account()
            time.sleep(5)
            home_page.enter_mobile_number("7722021267")
            time.sleep(5)
            home_page.click_on_login_submit_button()
            home_page.enter_name("aarti")
            time.sleep(5)
            home_page.enter_email("gangishyamica@gmail.com")
            time.sleep(15)
            home_page.click_on_submit_button_for_registering_the_account()
            time.sleep(5)
            assert home_page.display_email_id_is_already_registered()
            time.sleep(5)

    def test_register_with_invalid_otp(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            frame1 = wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//div["
                                                                                             "@id='__st_fancy_popup"
                                                                                             "']/iframe")))
            self.driver.switch_to.frame(frame1)
            self.driver.find_element(By.ID, "__st_bpn_no")
        except TimeoutException:
            print("TimeoutException got handled here")
            self.driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
            home_page = Homepage(self.driver)
            home_page.click_on_my_account()
            time.sleep(5)
            home_page.enter_mobile_number("772202167")
            time.sleep(5)
            home_page.click_on_login_submit_button()
            time.sleep(5)
            home_page.enter_name("aarti")
            time.sleep(5)
            home_page.enter_email("gangishyamica@gmail.com")
            time.sleep(15)
            home_page.click_on_submit_button_for_registering_the_account()
            assert home_page.display_invalid_or_expired_otp()
            time.sleep(5)

