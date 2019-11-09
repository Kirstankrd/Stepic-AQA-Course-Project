from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_message_about_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
            "Success message is presented, but should not be"
        empty_message = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text
        assert empty_message == "Your basket is empty. Continue shopping",\
            f"'{empty_message}', but Expected 'Your basket is empty. Continue shopping'"

    def should_not_be_list_of_products(self):
        assert self.is_not_element_present(*BasketPageLocators.LIST_OF_ITEM), \
            "List of products in basket is presented, but should not be"
