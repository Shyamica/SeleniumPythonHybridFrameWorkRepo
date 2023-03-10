import time

import pytest
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageobjects.Homepage import Homepage


@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:

    @pytest.mark.parametrize("number", ["9498499445", "8304841101", "7994030029"])
    def test_login_with_valid_phone_number(self,number):
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
            home_page.enter_mobile_number("9498499445")
            time.sleep(5)
            home_page.click_on_login_submit_button()
            time.sleep(10)
            home_page.click_on_otp_submit_button()
            time.sleep(5)
            assert home_page.display_status_of_logged_in()
            time.sleep(5)

    def test_login_with_invalid_phone_number(self):
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
            home_page.enter_mobile_number("123456789")
            time.sleep(5)
            home_page.click_on_login_submit_button()
            time.sleep(5)
            assert home_page.display_phone_number_is_invalid()
            time.sleep(5)






