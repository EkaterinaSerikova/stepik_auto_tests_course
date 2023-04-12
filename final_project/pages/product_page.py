from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators, ProductPageLocators


class ProductPage(BasePage):
    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        alert = self.browser.switch_to.alert
        alert.accept()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ITEM_ADDED_TO_BASKET_MESSAGE), \
           "Success message is presented, but should not be"

    def product_added_to_basket_success_message(self, browser):
        assert self.browser.find_element(
            *ProductPageLocators.ITEM_NAME).text + " has been added to your basket." in browser.find_element(
            *ProductPageLocators.ITEM_ADDED_TO_BASKET_MESSAGE).text

    def price_in_basket_is_the_same_as_products(self, browser):
        assert self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text in browser.find_element(
            *ProductPageLocators.BASKET_PRICE).text
