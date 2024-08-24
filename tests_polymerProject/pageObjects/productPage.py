import pytest
from selenium.webdriver.common.by import By
from selenium import  webdriver
import time
from selenium.webdriver import Keys,ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class ProductPage:

    def __init__(self,driver):
        self.driver = driver

    #Locators
    def get_product_title(self):
       return self.driver.execute_script("return document.querySelector('body > shop-app').shadowRoot.querySelector('iron-pages > shop-detail').shadowRoot.querySelector('#content > div > h1')")

    def get_product_price(self):
        return self.driver.execute_script("return document.querySelector('body > shop-app').shadowRoot.querySelector('iron-pages > shop-detail').shadowRoot.querySelector('#content > div > div.price')")


    def select_size_of_product(self):
        return self.driver.execute_script("return document.querySelector('body > shop-app').shadowRoot.querySelector('iron-pages > shop-detail').shadowRoot.querySelector('#sizeSelect')")

    def add_cart_button(self):
       return self.driver.execute_script("return document.querySelector('body > shop-app').shadowRoot.querySelector('iron-pages > shop-detail').shadowRoot.querySelector('#content > div > shop-button > button')")

    def added_cart_box(self):
       return self.driver.execute_script("return document.querySelector('body > shop-app').shadowRoot.querySelector('shop-cart-modal').shadowRoot.querySelector('div:nth-child(2) > div')")

    def viewcart_button(self):
        return self.driver.execute_script("return document.querySelector('body > shop-app').shadowRoot.querySelector('shop-cart-modal').shadowRoot.querySelector('#viewCartAnchor')")

    def checkout_button(self):
        return self.driver.execute_script("return document.querySelector('body > shop-app').shadowRoot.querySelector('shop-cart-modal').shadowRoot.querySelector('div:nth-child(3) > shop-button:nth-child(2) > a')")

    def select_quantity_box_of_product(self):
        return self.driver.execute_script(
            "return document.querySelector('body > shop-app').shadowRoot.querySelector('iron-pages > shop-detail').shadowRoot.querySelector('#quantitySelect')")

    def added_confirmation_box(self):
        return self.driver.execute_script("return document.querySelector('body > shop-app').shadowRoot.querySelector('shop-cart-modal')")
    def select_product_size(self,size):
        size_element = self.select_size_of_product()
        select_size = Select(size_element)
        select_size.select_by_visible_text(size)

    def select_quantity(self,quantity):
        qty_element = self.select_quantity_box_of_product()
        qty = Select(qty_element)
        qty.select_by_value(quantity)

    def check_if_item_added(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(lambda driver : self.added_cart_box())
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element(self.added_cart_box()).click(self.viewcart_button()).perform()
        self.driver.save_screenshot("tests_polymerProject/screenshots/select_a_product/click-on-product.png")
        #print(self.added_cart_box().text)
        #assert "Added" in self.added_cart_box().text

    def click_on_viewcart(self):
        wait = WebDriverWait(self.driver,10)
        wait.until(lambda driver : self.viewcart_button()).click()

        time.sleep(5)


