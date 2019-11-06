from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math


class ProductPage(BasePage):
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def add_product_to_basket(self):
        basket_link = self.browser.find_element(*ProductPageLocators.BASKET_LINK)
        basket_link.click()

    def check_status_of_basket(self):
        book_title = self.browser.find_element(*ProductPageLocators.BOOK_TITLE).text
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        product_in_basket_title = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_BASKET_TITLE).text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        assert book_title == product_in_basket_title, f"'{book_title}' not equal '{product_in_basket_title}'"
        assert book_price == basket_price, f"'{book_price}' not equal '{basket_price}'"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_dissapeared_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should be dissapeared"








