import pytest
from selenium.webdriver.common.by import By
from selenium import  webdriver
import time
from selenium.webdriver import Keys,ActionChains
from selenium.webdriver.support.select import Select


class CheckOutPage():
    def __init__(self,driver):
        self.driver = driver

    def get_CheckoutPageTitle(self):
        return self.driver.execute_script("return document.querySelector('body > shop-app').shadowRoot.querySelector('iron-pages > shop-checkout').shadowRoot.querySelector('#checkoutForm > form > header > h1')")

    def get_acc_info_Email(self):
        return self.driver.execute_script("return document.querySelector('body > shop-app').shadowRoot.querySelector('iron-pages > shop-checkout').shadowRoot.querySelector('#accountEmail')")

    def get_acc_info_Phone(self):
        return self.driver.execute_script("return document.querySelector('body > shop-app').shadowRoot.querySelector('iron-pages > shop-checkout').shadowRoot.querySelector('#accountPhone')")

    def get_shippingAdd_Add(self):
        return self.driver.execute_script("return document.querySelector('body > shop-app').shadowRoot.querySelector('iron-pages > shop-checkout').shadowRoot.querySelector('#shipAddress')")

    def get_shippingAdd_City(self):
        return self.driver.execute_script("return document.querySelector('body > shop-app').shadowRoot.querySelector('iron-pages > shop-checkout').shadowRoot.querySelector('#shipCity')")

    def get_shippingAddz_State(self):
        return self.driver.execute_script("return document.querySelector('body > shop-app').shadowRoot.querySelector('iron-pages > shop-checkout').shadowRoot.querySelector('#shipState')")

    def get_shippingAddz_Post(self):
        return self.driver.execute_script("return document.querySelector('body > shop-app').shadowRoot.querySelector('iron-pages > shop-checkout').shadowRoot.querySelector('#shipZip')")

    def get_shippingAdd_Country(self):
        return self.driver.execute_script("return document.querySelector('body > shop-app').shadowRoot.querySelector('iron-pages > shop-checkout').shadowRoot.querySelector('#shipCountry')")

    def get_Billing_Address_Checkbox(self):
        return self.driver.execute_script("return document.querySelector('body > shop-app').shadowRoot.querySelector('iron-pages > shop-checkout').shadowRoot.querySelector('#setBilling')")

    def get_Billing_Address_Address(self):
        return self.driver.execute_script("return document.querySelector('body > shop-app').shadowRoot.querySelector('iron-pages > shop-checkout').shadowRoot.querySelector('#billAddress')")

    def get_Billing_Address_City(self):
        return self.driver.execute_script("return document.querySelector('body > shop-app').shadowRoot.querySelector('iron-pages > shop-checkout').shadowRoot.querySelector('#billCity')")

    def get_Billing_Address_State(self):
        return self.driver.execute_script("return document.querySelector('body > shop-app').shadowRoot.querySelector('iron-pages > shop-checkout').shadowRoot.querySelector('#billState')")

    def get_Billing_Address_Zip(self):
        return self.driver.execute_script("return document.querySelector('body > shop-app').shadowRoot.querySelector('iron-pages > shop-checkout').shadowRoot.querySelector('#billZip')")

    def get_Billing_Address_Country(self):
        return self.driver.execute_script("return document.querySelector('body > shop-app').shadowRoot.querySelector('iron-pages > shop-checkout').shadowRoot.querySelector('#billCountry')")


    def get_Payment_CardHolderName(self):
        return self.driver.execute_script("return document.querySelector('body > shop-app').shadowRoot.querySelector('iron-pages > shop-checkout').shadowRoot.querySelector('#ccName')")

    def get_Payment_CardNumber(self):
        return self.driver.execute_script("return document.querySelector('body > shop-app').shadowRoot.querySelector('iron-pages > shop-checkout').shadowRoot.querySelector('#ccNumber')")


    def get_Payment_Expiry(self):
        return self.driver.execute_script("return document.querySelector('body > shop-app').shadowRoot.querySelector('iron-pages > shop-checkout').shadowRoot.querySelector('#ccExpMonth')")

    def get_Payment_Year(self):
        return self.driver.execute_script("return document.querySelector('body > shop-app').shadowRoot.querySelector('iron-pages > shop-checkout').shadowRoot.querySelector('#ccExpYear')")

    def get_Payment_CVV(self):
        return self.driver.execute_script("return document.querySelector('body > shop-app').shadowRoot.querySelector('iron-pages > shop-checkout').shadowRoot.querySelector('#ccCVV')")


    def get_OrderSummary_ItemPrice(self):
        return self.driver.execute_script("return document.querySelector('body > shop-app').shadowRoot.querySelector('iron-pages > shop-checkout').shadowRoot.querySelector('#checkoutForm > form > div.subsection.grid > section:nth-child(2) > div.row.order-summary-row > div:nth-child(2)')")


    def get_OrderSummary_TotalPrice(self):
        return self.driver.execute_script("return document.querySelector('body > shop-app').shadowRoot.querySelector('iron-pages > shop-checkout').shadowRoot.querySelector('#checkoutForm > form > div.subsection.grid > section:nth-child(2) > div.row.total-row > div:nth-child(2)')")

    def get_place_order_button(self):
        return self.driver.execute_script("return document.querySelector('body > shop-app').shadowRoot.querySelector('iron-pages > shop-checkout').shadowRoot.querySelector('#submitBox > input[type=button]')")

    def select_shipping_country(self,s_country):
        country_box = Select(self.get_shippingAdd_Country())
        country_box.select_by_value(s_country)


    def select_billing_country(self,b_country):
        country_box = Select(self.get_Billing_Address_Country())
        country_box.select_by_value(b_country)

    def select_payment_expirydate(self,edate):
        expiry_box = Select(self.get_Payment_Expiry())
        expiry_box.select_by_value(edate)

    def select_payment_year(self,year):
        year_box = Select(self.get_Payment_Year())
        year_box.select_by_value(year)


    def enter_account_details(self,email,phone):
        self.get_acc_info_Email().send_keys(email)
        self.get_acc_info_Phone().send_keys(phone)



    def enter_shipping_details(self,address,city,state,zip,shipping_country):
        self.get_shippingAdd_Add().send_keys(address)
        self.get_shippingAdd_City().send_keys(city)
        self.get_shippingAddz_State().send_keys(state)
        self.get_shippingAddz_Post().send_keys(zip)
        self.select_shipping_country(s_country=shipping_country)
        self.driver.save_screenshot("C:/Users/harin/PycharmProjects/pythonProject1/tests_polymerProject/screenshots/checkoutpage/shippingdetails.png")

    def enter_billing_details(self, address, city, state, zip, billing_country):
        self.get_Billing_Address_Address().send_keys(address)
        self.get_Billing_Address_City().send_keys(city)
        self.get_Billing_Address_State().send_keys(state)
        self.get_Billing_Address_Zip().send_keys(zip)
        self.select_billing_country(b_country=billing_country)
        self.driver.save_screenshot("C:/Users/harin/PycharmProjects/pythonProject1/tests_polymerProject/screenshots/checkoutpage/billing.png")

    def click_use_different_billing_checkbox(self):
        self.get_Billing_Address_Checkbox().click()

    def enter_payment_details(self,name,cnumber,expdate,expyear,cvv):
        self.get_Payment_CardHolderName().send_keys(name)
        self.get_Payment_CardNumber().send_keys(cnumber)
        self.select_payment_expirydate(edate=expdate)
        self.select_payment_year(year=expyear)
        self.get_Payment_CVV().send_keys(cvv)
        self.driver.save_screenshot("tests_polymerProject/screenshots/checkoutpage/payment.png")















