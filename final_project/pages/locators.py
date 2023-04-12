from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    VIEW_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group > a:nth-child(1)")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
    BASKET_ITEMS = (By.CSS_SELECTOR, "#basket_formset")


class LoginPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, ".login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, ".register_form")
    EMAIL_ADDRESS_FIELD = (By.CSS_SELECTOR, "input#id_registration-email.form-control")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "input#id_registration-password1.form-control")
    CONFIRM_PASSWORD_FIELD = (By.CSS_SELECTOR, "input#id_registration-password2.form-control")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form > button")
    THANKS_FOR_REGISTERING_MESSAGE = (By.CSS_SELECTOR, "#messages > div > div")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".add-to-basket button")
    ITEM_ADDED_TO_BASKET_MESSAGE = (By.CSS_SELECTOR, "#messages>div:nth-child(1)>div")
    ITEM_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BASKET_PRICE = (By.CSS_SELECTOR, ".basket-mini")
    ITEM_NAME = (By.CSS_SELECTOR, "div.col-sm-6.product_main > h1")
