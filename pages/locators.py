from selenium.webdriver.common.by import By


class MainPageLocators(): #локаторы главной страницы
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators(): #локаторы страницы логина
    LOGIN_URL = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_LOGIN = (By.CSS_SELECTOR, 'input#id_registration-email')
    REGISTER_PASSWORD1 = (By.ID, 'id_registration-password1')
    REGISTER_PASSWORD2 = (By.ID, 'id_registration-password2')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[name^="registration_submit"]')

class ProductPageLocators(): #локаторы страницы товара
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BOOK_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
    BOOK_NAME_BASKET = (By.CSS_SELECTOR, "#messages>div:nth-child(1) strong")
    BOOK_PRICE_BASKET = (By.CSS_SELECTOR, "#messages>div:nth-child(3) strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages>div:nth-child(1)")
    BASKET_BUTTON = (By.XPATH, "//span[@class='btn-group']/a[@href='/en-gb/basket/']")
    EMPTY_BASKET = (By.CSS_SELECTOR, ".basket-items")
    BASKET_EMPTY_MESSAGE = (By.XPATH, "//p[contains(text(),'Your basket is empty.')]")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

