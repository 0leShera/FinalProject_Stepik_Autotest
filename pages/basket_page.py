from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def is_not_full_basket(self):
        self.basket_not_present()
        self.basket_content_inner()

    def basket_not_present(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Invalid success message"

    def basket_content_inner(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_INNER), "Invalid basket section"

    def text_in_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "Message 'Empte basket' is not presented"
