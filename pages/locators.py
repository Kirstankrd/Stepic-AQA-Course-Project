from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    LIST_OF_ITEM = (By.CSS_SELECTOR, "#content_inner .col-sm-6.h3")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, ".login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, ".register_form")
    REGISTER_FORM_EMAIL = (By.CSS_SELECTOR, "[name = 'registration-email']")
    REGISTER_FORM_PASSWORD = (By.CSS_SELECTOR, "[name = 'registration-password1']")
    REGISTER_FORM_PASSWORD_CONFIRM = (By.CSS_SELECTOR, "[name = 'registration-password2']")
    REGISTER_FORM_SUBMIT = (By.CSS_SELECTOR, "[name = 'registration_submit']")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class ProductPageLocators():
    ADD_TO_BASKET_LINK = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_TITLE = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_IN_BASKET_TITLE = (By.CSS_SELECTOR, "#messages div:first-child .alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div:first-child .alertinner")
    BOOK_PRICE = (By.CSS_SELECTOR, "p.price_color")
    BASKET_PRICE = (By.CSS_SELECTOR, "#messages div:nth-child(3) div p:first-child strong")
