from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), "Button is not presented"
        add_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_btn.click()

    def should_be_book_price(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_BASKET).text
        assert book_price == basket_price, "Price is not same"

    def should_be_book_name(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        book_basket = self.browser.find_element(*ProductPageLocators.BOOK_NAME_BASKET).text
        assert book_name == book_basket, "Name is not same"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented"

    def should_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"



