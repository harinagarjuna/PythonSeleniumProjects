from selenium import webdriver
from selenium.webdriver.common.by import By


class AccountServices:
    def __init__(self,driver):
        self.driver = driver
#Locators
    welcome = (By.XPATH, "//div[@id='leftPanel']/p")
    logout = (By.XPATH, "//div[@id='leftPanel']/ul/li[8]/a")
    Balance = (By.XPATH,"//table[@id='accountTable']/tbody/tr[1]/td[2]")
    Total = (By.XPATH, "//table[@id='accountTable']/tbody/tr[2]/td[2]")


    def get_welcome_text(self):
        return self.driver.find_element(*AccountServices.welcome)

    def get_balance(self):
        return self.driver.find_element(*AccountServices.Balance)

    def get_total(self):
        return self.driver.find_element(*AccountServices.Total)

    def get_logout(self):
        return self.driver.find_element(*AccountServices.logout)

    def text_welcome(self):
        return self.get_welcome_text().text



