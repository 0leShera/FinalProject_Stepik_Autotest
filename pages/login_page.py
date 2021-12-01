import time
from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "Wrong url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        assert self.is_element_present(*LoginPageLocators.REG_INPUT_EMAIL), "Email form not found"
        self.browser.find_element(*LoginPageLocators.REG_INPUT_EMAIL).send_keys(str(email))
        assert self.is_element_present(*LoginPageLocators.REG_INPUT_PASSWORD1), "Password1 form not found"
        self.browser.find_element(*LoginPageLocators.REG_INPUT_PASSWORD1).send_keys(str(password))
        assert self.is_element_present(*LoginPageLocators.REG_INPUT_PASSWORD2), "Password2 form not found"
        self.browser.find_element(*LoginPageLocators.REG_INPUT_PASSWORD2).send_keys(str(password))
        assert self.is_element_present(*LoginPageLocators.REG_BTN), "Password2 form not found"
        self.browser.find_element(*LoginPageLocators.REG_BTN).click()
