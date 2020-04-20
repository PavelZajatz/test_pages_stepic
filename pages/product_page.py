from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import BasketPageLocators
from selenium.webdriver.common.by import By


class BasketPage(BasePage):

    def should_add_item_to_basket(self):
        assert self.is_element_present(*BasketPageLocators.ADD_TO_BASKET), "Login url is not presented"
        add_btn = self.browser.find_element(*BasketPageLocators.ADD_TO_BASKET)
        add_btn.click()

    def should_be_book_price(self):
        book_price = self.browser.find_element(*BasketPageLocators.BOOK_PRICE).text
        basket_price = self.browser.find_element(*BasketPageLocators.BOOK_PRICE_BASKET).text
        assert  book_price == basket_price, "Price is not same"

    def should_be_book_name(self):
        book_name = self.browser.find_element(*BasketPageLocators.BOOK_NAME).text
        book_basket = self.browser.find_element(*BasketPageLocators.BOOK_NAME_BASKET).text
        assert book_name == book_basket, "Name is not same"



