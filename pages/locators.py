from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    SEE_BASKET = (By.CSS_SELECTOR, "span.btn-group a.btn.btn-default")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REG_INPUT_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REG_INPUT_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_INPUT_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_BTN = (By.CSS_SELECTOR, "button[name='registration_submit']")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p.price_color")
    SUCSESS_MASSEGE_BOOKNAME = (By.CSS_SELECTOR, ".alertinner strong")
    SUCSESS_MASSEGE_PRICE = (By.CSS_SELECTOR, ".alertinner p strong")
    SUCCESS_MESSAGES = (By.CSS_SELECTOR, ".alertinner strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    SEE_BASKET = (By.CSS_SELECTOR, "span.btn-group a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, "#basket_formset")
    BASKET_INNER = (By.CSS_SELECTOR, "#content_inner p")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p a")
