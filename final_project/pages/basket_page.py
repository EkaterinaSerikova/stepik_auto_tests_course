from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators, MainPageLocators
from .base_page import BasePage


class BasketPage(BasePage):
    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*MainPageLocators.BASKET_ITEMS), \
            "Items are in the basket, but should not be"

        # assert no items in basket message
        assert "Your basket is empty" in self.browser.find_element(*MainPageLocators.EMPTY_BASKET_MESSAGE).text
