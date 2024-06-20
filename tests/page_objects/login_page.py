from selenium.webdriver.common.by import By
from .base_page import BasePage


class LoginPage(BasePage):
    def navigate_to_my_account(self):
        self.find_element(By.XPATH, "//a[text()='My Account']").click()

    def login(self, email, password):
        self.find_element(By.ID, "username").send_keys(email)
        self.find_element(By.ID, "password").send_keys(password)
        self.find_element(By.NAME, "login").click()

    def verify_login(self):
        return self.find_element(By.XPATH, "//*[contains(text(), 'Hello')]").text

    def sign_out(self):
        self.find_element(By.LINK_TEXT, 'Sign out')
