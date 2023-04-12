from .base_page import BasePage
from .product_page import ProductPage
from .locators import LoginPageLocators, BasePageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
        assert True

    def register_new_user(self, browser, email, password):
        # open register form
        link = "http://selenium1py.pythonanywhere.com"
        product_page = ProductPage(browser, link)
        product_page.open()
        page = product_page.go_to_login_page_one()

        # input email
        email_field = browser.find_element(*LoginPageLocators.EMAIL_ADDRESS_FIELD)
        email_field.send_keys(email)

        # input password
        password_field = browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        password_field.send_keys(password)

        # input confirm password
        confirm_password_field = browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_FIELD)
        confirm_password_field.send_keys(password)

        # click register button
        browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()

        # confirm that user registered
        assert self.is_element_present(*LoginPageLocators.THANKS_FOR_REGISTERING_MESSAGE), \
            "Register message is not present"
