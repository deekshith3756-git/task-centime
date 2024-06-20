import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

from .base_page import BasePage


class CartPage(BasePage):
    def navigate_to_shop(self):
        self.find_element(By.LINK_TEXT, "Shop").click()

    def add_product_to_cart(self, category, product_name):
        self.find_element(By.XPATH, f"//a[text()='{category}']").click()
        self.find_element(By.XPATH, "//a[text()='Add to basket']").click()
        self.find_element(By.XPATH, "//a[@title='View Basket']").click()


    def verify_product_added(self, product_name):
        elem = None
        try:
            elem = self.find_element(By.XPATH, f"//a[text()='{product_name}']")
        except Exception as e:
            print("Product not found in basket")
        return elem


    def navigate_to_cart(self):
        #self.find_element(By.LINK_TEXT, "Cart").click()
        self.find_element(By.XPATH, '//*[@id="wpmenucartli"]/a/i').click()

    def remove_product_from_cart(self, product_name):
        elem = self.find_element(By.XPATH, f"//td/a[text()='{product_name}']")
        if elem:
            self.find_element(By.XPATH, "//a[@title='Remove this item']").click()

    def verify_product_removed(self, product_name):
        return self.find_element(By.XPATH, f"//div[contains(text(), '{product_name} removed')]").text

