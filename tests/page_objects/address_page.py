from selenium.webdriver.common.by import By
from .base_page import BasePage


class AddressPage(BasePage):
    def navigate_to_my_account(self):
        self.find_element(By.LINK_TEXT, "My Account").click()

    def navigate_to_address(self):
        self.find_element(By.LINK_TEXT, "Addresses").click()

    def edit_billing_address(self):
        self.find_element(By.XPATH, '//*[@id="page-36"]/div/div[1]/div/div/div[1]/header/a').click()

    def enter_billing_address(self, first_name, last_name, address, city, state, postcode, country):
        self.find_element(By.ID, "billing_first_name").send_keys("kiran")
        self.find_element(By.ID, "billing_last_name").send_keys("reddy")
        self.find_element(By.ID,'billing_email').send_keys("kreddy@gmail.com")
        self.find_element(By.ID, 'billing_phone_field').send_keys("12345678")
        self.find_element(By.ID, "billing_address_1").send_keys("Hyderabad")
        self.find_element(By.ID, "billing_city").send_keys("Hyderabad")
        self.find_element(By.ID, "billing_state_field").send_keys("Telangana")
        self.find_element(By.ID, "billing_postcode").send_keys("512453")
        self.find_element(By.ID, "billing_country").send_keys("India")
        self.find_element(By.NAME, "save_address").click()

    def verify_address_change_success(self):
        return self.find_element(By.XPATH, "//*[contains(text(), 'Address changed successfully')]").text

    def get_billing_address(self):
        return self.find_element(By.CSS_SELECTOR, ".u-column1.addresses .address").text
