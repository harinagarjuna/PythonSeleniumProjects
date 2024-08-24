from selenium import  webdriver
import time
from selenium.webdriver import Keys,ActionChains
from selenium.webdriver.support.select import Select


class CompletePage():
    def __init__(self,driver):
        self.driver = driver


    def get_thanks_title(self):
        return self.driver.execute_script("return document.querySelector('body > shop-app').shadowRoot.querySelector('iron-pages > shop-checkout').shadowRoot.querySelector('#pages > header.iron-selected > h1')")

    def get_confirmation(self):
        return self.driver.execute_script("return document.querySelector('body > shop-app').shadowRoot.querySelector('iron-pages > shop-checkout').shadowRoot.querySelector('#pages > header.iron-selected > p')")

    def get_finish_button(self):
        return self.driver.execute_script("return document.querySelector(‘body > shop-app’).shadowRoot.querySelector(‘iron-pages > shop-checkout’).shadowRoot.querySelector(‘#pages > header.iron-selected > shop-button > a’)")