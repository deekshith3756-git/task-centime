import time

import pytest
from page_objects.cart_page import CartPage


@pytest.mark.usefixtures("driver")
class TestCart:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.cart_page = CartPage(driver)
        self.cart_page.open('https://practice.automationtesting.in/')

    @pytest.mark.smoke
    def test_add_product_to_cart(self):
        self.cart_page.navigate_to_shop()
        self.cart_page.add_product_to_cart('Android', 'Android Quick Start Guide')
        assert self.cart_page.verify_product_added('Android Quick Start Guide') is not None

    def test_delete_product_from_cart(self):
        self.cart_page.navigate_to_cart()
        self.cart_page.remove_product_from_cart('Android Quick Start Guide')
        assert self.cart_page.verify_product_removed('Android Quick Start Guide'), 'Android Quick Start Guide removed. '
