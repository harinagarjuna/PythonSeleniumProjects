import pytest
from selenium.webdriver.common.by import By
from selenium import  webdriver
import time
from selenium.webdriver import Keys,ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage():
    def __init__(self,driver):
        self.driver = driver


    def get_checkout_button(self):
        return self.driver.execute_script("return document.querySelector('body > shop-app').shadowRoot.querySelector('iron-pages > shop-cart').shadowRoot.querySelector('div > div:nth-child(2) > div.checkout-box > shop-button > a')")

    def click_checkout(self):
        self.get_checkout_button().click()