import pytest
from page_objects.login_page import LoginPage
from page_objects.registration_page import RegistrationPage


@pytest.mark.usefixtures("driver")
class TestLoginRegistration:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.registration_page = RegistrationPage(driver)
        self.login_page = LoginPage(driver)
        self.registration_page.open('https://practice.automationtesting.in/')

    def test_registration(self):
        self.registration_page.navigate_to_my_account()
        self.registration_page.register('pyrza1c2t3gice412@gmail.com', 'Practice*1234#')
        assert 'Hello' in self.registration_page.verify_registration()

    def test_login(self):
        self.registration_page.navigate_to_my_account()
        try:
            if self.login_page.verify_login() is not None:
                self.login_page.sign_out()
        except Exception as e:
            print("User is not logged in")

        self.login_page.login('pyrza1c2t3gice412@gmail.com', 'Practice*1234#')
        assert 'Hello' in self.login_page.verify_login()