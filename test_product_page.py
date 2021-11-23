import time
import pytest
from .pages.product_page import ProductPage


@pytest.mark.parametrize('index', [0, 1, 2, 3, 4, 5, 6,
                                  pytest.param(7, marks=pytest.mark.xfail),
                                  8, 9])
def test_guest_can_add_product_to_basket(browser, index):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{index}"
    page = ProductPage(browser, link)
    page.open()
    # time.sleep(2)
    page.should_be_add_product_to_basket()
    page.solve_quiz_and_get_code()
    # time.sleep(2)
    page.should_be_check_product_name()
    page.should_be_check_product_price()
