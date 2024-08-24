import pytest
from selenium.webdriver.common.by import By
from selenium import  webdriver
import time
from selenium.webdriver import Keys,ActionChains

class MenswearPage:
    def __init__(self,driver):
        self.driver = driver


    #Locators
    allproducts = "return document.querySelector('shop-app').shadowRoot.querySelector('iron-pages').querySelector('shop-list').shadowRoot.querySelector('ul').querySelectorAll('li')"

    allproducts_price = "return document.querySelector('body > shop-app').shadowRoot.querySelector('iron-pages > shop-list').shadowRoot.querySelector('ul > li > a >shop-list-item').shadowRoot.querySelector('span')"

    lowest_product_price = None


    #getElementFunctions
    def get_allproducts(self):
        return self.driver.execute_script(*MenswearPage.allproducts)

    def get_allproducts_price(self):
        return self.driver.execute_script(*MenswearPage.allproducts_price)

    def get_lowest_price_product(self):
        return self.driver.execute_script(*MenswearPage.lowest_product_price)

    def get_youtube_hooded_shirt(self):
        time.sleep(4)
        yhs = self.driver.execute_script("return document.querySelector('body > shop-app').shadowRoot.querySelector('iron-pages > shop-list').shadowRoot.querySelector('ul > li:nth-child(5) > a > shop-list-item').shadowRoot.querySelector('shop-image').shadowRoot.querySelector('#img')")
        print(yhs)
        return yhs



    #functions
    def set_lowest_price(self):
        l_price = []
        allprodcts_price = self.get_allproducts_price()
        for price in allprodcts_price:
            prod_price = float((price.text).replace('$', ''))
            l_price.append(prod_price)

        sorted_price = sorted(l_price)
        for lowest_price in allprodcts_price:
            if str(sorted_price[0]) in lowest_price.text:
                MenswearPage.lowest_product_price = lowest_price
                break

    def click_lowest_price_product(self):
        self.set_lowest_price()
        self.get_lowest_price_product().click()
        time.sleep(4)

    def click_youtube_shirt(self):
        yshirt = self.get_youtube_hooded_shirt()
        actionchains = ActionChains(self.driver)
        actionchains.scroll_to_element(yshirt).click(yshirt).perform()
        time.sleep(8)