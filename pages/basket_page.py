from .product_page import ProductPage
from .locators import ProductPageLocators


class BasketPage(ProductPage):

    def is_items_not_in_the_basket(self): #проверка что в корзине нет товара
        assert self.is_not_element_present(*ProductPageLocators.EMPTY_BASKET), \
            "Items should not be present in the Basket"


    def is_basket_empty(self): #проверка что корзина пустая
        assert self.is_element_present(*ProductPageLocators.BASKET_EMPTY_MESSAGE), \
            'Basket is not empty.'