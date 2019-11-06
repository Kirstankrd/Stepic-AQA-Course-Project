from pages.product_page import ProductPage
import pytest
import time
from pages.locators import ProductPageLocators

'''
@pytest.mark.parametrize('offer', ["?promo=offer0",
                                  "?promo=offer1",
                                  "?promo=offer2",
                                  "?promo=offer3",
                                  "?promo=offer4",
                                  "?promo=offer5",
                                  "?promo=offer6",
                                  pytest.param("?promo=offer7",
                                               marks=pytest.mark.xfail(reason="Little bug in offer")),
                                  "?promo=offer8",
                                  "?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, offer):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/" + offer
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.check_status_of_basket()
'''

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE)


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE)


def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    time.sleep(1)
    page.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE)
