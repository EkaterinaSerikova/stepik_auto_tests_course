import time
import math
import pytest

from selenium.common.exceptions import TimeoutException, NoSuchElementException, NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pytest import mark

from .pages.base_page import BasePage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

from .pages.locators import MainPageLocators, BasePageLocators, LoginPageLocators


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = BasePage(browser, link)
        page.open()
        page.go_to_login_page_one()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = BasePage(browser, link)
        page.open()
        page.should_be_login_link_one()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        # open main page
        link = "http://selenium1py.pythonanywhere.com/"
        page = BasePage(browser, link)
        page.open()

        # click on view basket
        page.go_to_basket()

        # verify that there is no items in basket
        basket_page = BasketPage(browser, link)
        basket_page.should_not_be_items_in_basket()
