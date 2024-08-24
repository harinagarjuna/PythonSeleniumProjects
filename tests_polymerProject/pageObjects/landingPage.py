import pytest
from selenium.webdriver.common.by import By
from selenium import  webdriver
import time


class LandingPage():

    def __init__(self,driver):
        self.driver = driver

    def get_menswear_link(self):
        menswear_link = self.driver.execute_script("return document.querySelector('body > shop-app').shadowRoot.querySelector('#tabContainer > shop-tabs > shop-tab:nth-child(1) > a');")
        return menswear_link




    def click_on_menswear_link(self):
        self.get_menswear_link().click()
        self.driver.save_screenshot("C:/Users/harin/PycharmProjects/pythonProject1/tests_polymerProject/screenshots/LandingPage/landingpage.jpg")
        time.sleep(4)





