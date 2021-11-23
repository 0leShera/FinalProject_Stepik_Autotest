from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    # добавить товар в корзину
    def should_be_add_product_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket.click()

        # сверить название книни в корзине
    def should_be_check_product_name(self):
        book_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        book_massage = self.browser.find_element(*ProductPageLocators.SUCSESS_MASSEGE_NAME).text
        assert book_name == book_massage, \
            f"The book_name is not correct: '{book_name}' instead of '{book_massage}'"

        # сверить цену в корзине
    def should_be_check_product_price(self):
        book_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        price_massage = self.browser.find_element(*ProductPageLocators.SUCSESS_MASSEGE_PRICE).text
        assert book_price == price_massage, \
            f"The price is not correct: '{book_price}' instead of '{price_massage}'"
