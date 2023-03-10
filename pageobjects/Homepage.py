from  selenium import webdriver
from selenium.webdriver.common.by import By


class Homepage:

    def __init__(self,driver):
        self.driver = driver

    def get_my_account_option(self):
        return self.driver.find_element(By.XPATH,"//div[@class='profile-holder']/a[1]")

    def get_mobile_field(self):
        return self.driver.find_element(By.ID,"loginMobile")

    def get_login_submit_button(self):
        return self.driver.find_element(By.XPATH,"(//form[@id='validate-mobile']/div[2]/button)[2]")

    def get_otp_submit_button(self):
        return self.driver.find_element(By.XPATH,"//form[@id='validate-otp']//button[contains(@class,"
                                                 "'modal__variant-login--submit')][normalize-space()='SUBMIT']")

    def get_logged_in(self):
        return self.driver.find_element((By.XPATH, "//a[contains(@class,'iconLinks iconLinks__profile profile-js-handle "
                                                 "isLoggedIn')]//span[contains(@class,'spriteIcon-Firstfold "
                                                 "profileIcon-active')]"))

    def get_phone_number_is_invalid(self):
        return self.driver.find_element(By.XPATH,"//div[@role='status']")

    def get_name_field(self):
        return self.driver.find_element(By.ID,"registerName")

    def get_email_field(self):
        return self.driver.find_element(By.ID,"registerEmail")

    def get_submit_button_for_registering(self):
        return self.driver.find_element(By.XPATH,"//button[@class='ctaText reg_validate modal__variant-login--submit']")

    def get_email_id_already_registered(self):
        return self.driver.find_element(By.XPATH, "//div[@class='error-global step-3-error']")

    def get_invalid_otp(self):
        return self.driver.find_element(By.XPATH, "//div[@class='error-global step-3-error']")

    def click_on_my_account(self):
        self.get_my_account_option().click()

    def enter_mobile_number(self,mobile_number):
        self.get_mobile_field().send_keys(mobile_number)

    def click_on_login_submit_button(self):
        self.get_login_submit_button()

    def click_on_otp_submit_button(self):
        self.get_otp_submit_button().click()

    def display_status_of_logged_in(self):
        return self.get_logged_in().is_displayed

    def display_phone_number_is_invalid(self):
        return self.get_phone_number_is_invalid().text.__eq__("Phone number is invalid")

    def enter_name(self,name):
        self.get_name_field().send_keys(name)

    def enter_email(self,email_text):
        self.get_email_field().send_keys(email_text)

    def click_on_submit_button_for_registering_the_account(self):
        self.get_submit_button_for_registering()

    def display_email_id_is_already_registered(self):
        self.get_email_id_already_registered().text.__eq__("Email id already registered,please provide an alternate "
                                                           "email id.")

    def display_invalid_or_expired_otp(self):
        self.get_invalid_otp().text.__eq__("Invalid or expired OTP, please try again!")

