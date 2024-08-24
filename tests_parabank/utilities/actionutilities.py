import time
import pytest
from selenium.webdriver.common.by import By
from selenium import  webdriver
from tests_parabank.utilities.utils import BasicUtils
from tests_polymerProject.constants.basiconstants import BaseConstants
from tests_polymerProject.pageObjects.cartPage import CartPage
from tests_polymerProject.pageObjects.landingPage import LandingPage
from tests_polymerProject.pageObjects.menswear import MenswearPage
from selenium.webdriver.support.ui import Select

from tests_polymerProject.pageObjects.productPage import ProductPage


class ActionUtilities():


    @pytest.mark.usefixtures('ch_driver')
    def click_on_a_product(self,ch_driver):
        dr = ch_driver
        BSObject = BaseConstants()
        dr.get(BSObject.base_url)
        time.sleep(5)
        landing_page = LandingPage(dr)
        landing_page.click_on_menswear_link()
        dr.save_screenshot("C:/Users/harin/PycharmProjects/pythonProject1/tests_polymerProject/screenshots/select_a_product/click-on-menswear.png")
        menswear = MenswearPage(dr)
        menswear.click_youtube_shirt()
        time.sleep(4)

    @pytest.mark.usefixtures('ch_driver')
    def select_a_product(self,ch_driver,size,qnty):
        dr = ch_driver
        #action_utils = ActionUtilities()
        self.click_on_a_product(dr)
        product_page = ProductPage(dr)
        product_page.select_product_size(size)
        product_page.select_quantity(qnty)
        dr.save_screenshot("C:/Users/harin/PycharmProjects/pythonProject1/tests_polymerProject/screenshots/select_a_product/select-product.png")
        product_page.add_cart_button().click()
        time.sleep(5)
