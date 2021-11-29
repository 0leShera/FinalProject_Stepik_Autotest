from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def should_be_add_product_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket.click()

    def should_be_check_product_name_and_price(self):
        def should_be_check_product_name():
            book_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
            book_massage = self.browser.find_element(*ProductPageLocators.SUCSESS_MASSEGE_BOOKNAME).text
            assert book_name == book_massage, \
                f"The book_name is not correct: '{book_name}' instead of '{book_massage}'"

        def should_be_check_product_price(self):
            book_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
            price_massage = self.browser.find_element(*ProductPageLocators.SUCSESS_MASSEGE_PRICE).text
            assert book_price == price_massage, \
                f"The price is not correct: '{book_price}' instead of '{price_massage}'"

    def is_not_success_massage_present(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGES), "Wrong show success message"

    def should_be_disappeared_message_after_adding_product(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGES), "Wrong show success message"
