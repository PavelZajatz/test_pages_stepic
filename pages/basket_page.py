from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By


class BasketPage(BasePage):
    def should_add_to_basket(self):
        self.should_open_page()
        self.should_add_item_to_basket()
        self.should_solve_quize()

    def should_open_page(self):

    def should_add_item_to_basket(self):

    def should_solve_quize(self):
