from selenium.webdriver.common.by import By
from .base_page import BasePage


class RegistrationPage(BasePage):
    def navigate_to_my_account(self):
        self.find_element(By.LINK_TEXT, "My Account").click()

    def register(self, email, password):
        self.find_element(By.ID, "reg_email").send_keys(email)
        self.find_element(By.ID, "reg_password").send_keys(password)
        self.find_element(By.NAME, "register").click()

    def verify_registration(self):
        return self.find_element(By.XPATH, "//*[contains(text(), 'Hello')]").text