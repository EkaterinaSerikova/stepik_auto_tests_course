import time
import math
import pytest

from selenium.common.exceptions import TimeoutException, NoSuchElementException, NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pytest import mark
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.base_page import BasePage
from .pages.basket_page import BasketPage
from .pages.locators import ProductPageLocators


class TestUserAddToBasketFromProductPage:
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = LoginPage(browser, browser.current_url)
        page.register_new_user(browser, str(time.time()) + "@fakemail.org", "randomrandom")

        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser, link)

        # open page
        page.open()

        # click on add to basket button
        browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

        # solve quiz
        page.solve_quiz_and_get_code()

        # verify message that product was added to basket
        page.product_added_to_basket_success_message(browser)

        # verify that the price of the cart is the same as the price of the product
        page.price_in_basket_is_the_same_as_products(browser)

    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser, link)

        # open page
        page.open()

        # click on add to basket button
        browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

        # solve quiz
        page.solve_quiz_and_get_code()

        # verify message that product was added to basket
        page.product_added_to_basket_success_message(browser)

        # verify that the price of the cart is the same as the price of the product
        page.price_in_basket_is_the_same_as_products(browser)

    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link_one()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page_one()

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser, link)

        # open page
        page.open()

        # open basket
        page.go_to_basket()

        # verify that there is no items in basket
        basket_page = BasketPage(browser, link)
        basket_page.should_not_be_items_in_basket()

