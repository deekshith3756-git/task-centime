import pytest
from page_objects.address_page import AddressPage
from page_objects.login_page import LoginPage


@pytest.mark.usefixtures("driver")
class TestAddressPage:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.address_page = AddressPage(driver)
        self.login_page = LoginPage(driver)
        self.address_page.open('https://practice.automationtesting.in/')

    def test_add_address(self):
        if 'Hello' not in self.login_page.verify_login():
            self.login_page.login('xyz123@gmail.com', '12345678')
        self.address_page.navigate_to_my_account()
        self.address_page.navigate_to_address()
        self.address_page.edit_billing_address()
        self.address_page.enter_billing_address()
        assert self.address_page.verify_address_change_success(), 'Address changed successfully'
