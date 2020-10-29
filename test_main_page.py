from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.go_to_login_page()  # выполняем метод страницы - переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url)  # инициализируем страницу
    login_page.should_be_login_page()  # проверка url,формы логина и регистрации


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.should_be_login_link()  # проверка что есть логин линк


def test_guest_should_see_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = LoginPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.should_be_login_page()  # проверка url, формы логина и регистрации

# def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     page = BasketPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
#     page.open()                      # открываем страницу
#     page.should_open_basket()        # открытие корзины
#     page.is_items_not_in_the_basket()# товар не должен быть в корзине
#     page.is_basket_empty()           # корзина пуста
