from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import time
import random
import pytest


# проверка что гость может видить сообщение о успешном добавлении товара в корзину
@pytest.mark.xfail(reason="should not be present")
def test_guest_can_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    # product_page.solve_quiz_and_get_code()
    # time.sleep(5)
    product_page.should_not_be_success_message()


# проверка что гость не может видить сообщение о успешном добавлении товара в корзину
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_not_be_success_message()


# проверка что гость может видить как сообщение о успешном добавлении товара в корзину пропадает
@pytest.mark.xfail(reason="not disappiring")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    time.sleep(1)
    product_page.should_disappeared()


# проверка что гость может добавить продукт в корзину
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.should_be_book_name()
    product_page.should_be_book_price()


# проверка что гость может видить ссылку логина на странице товара
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


# проверка что гость может перейти на страницу логина со страницы товара
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)  # инициализируем страницу
    login_page.should_be_login_page()


# проверка что гость не может видеть товар в корзине после ее открытия
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link)
    page.open()
    page.should_open_basket()
    page.is_items_not_in_the_basket()
    page.is_basket_empty()


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, browser):  # подготовка пользователя
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        self.login_page = LoginPage(browser, link)
        self.login_page.open()
        count = random.randint(1, 100)
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time() + count)
        self.login_page.register_new_user(email, password)
        self.login_page.should_be_authorized_user()

    # проверка что пользователь не может видить сообщение об успешном бобавлении товара в корзину на странице товара
    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        self.product_page = ProductPage(browser, link)
        self.product_page.open()
        self.product_page.should_not_be_success_message()

    # проверка что пользователь может добавить товар в корзину
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        self.product_page = ProductPage(browser, link)
        self.product_page.open()
        self.product_page.add_to_basket()
        self.product_page.should_be_book_name()
        self.product_page.should_be_book_price()
