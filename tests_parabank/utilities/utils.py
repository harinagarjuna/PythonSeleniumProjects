import time

import pytest
from selenium.webdriver.common.by import By
from selenium import  webdriver


class BasicUtils:
    def __init__(self,driver):
        self.driver = driver

    def get_cart(self):
        return self.driver.execute_script \
        ("return document.querySelector('body > shop-app').shadowRoot.querySelector('#header > app-toolbar > div.cart-btn-container > a > paper-icon-button')")


    def click_cart(self):
        self.get_cart().click()

        time.sleep(4)