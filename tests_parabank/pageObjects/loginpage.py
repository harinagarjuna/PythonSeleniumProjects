import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self,driver):
        self.driver = driver


    #page locators
    username = (By.NAME, "username")
    password = (By.NAME, "password")
    login_button = (By.XPATH,"//input[@value='Log In']")
    err_msg = (By.XPATH, "//div[@id='rightPanel']/p")
    forgot_login = (By.XPATH, "//*[@id='loginPanel']/p[1]/a")
    register = (By.XPATH, "//*[@id='loginPanel']/p[2]/a")


    def get_username(self):
        return self.driver.find_element(*LoginPage.username)

    def get_password(self):
        return self.driver.find_element(*LoginPage.password)

    def get_submitbutton(self):
        return self.driver.find_element(*LoginPage.login_button)

    def get_errormessage(self):
        return self.driver.find_element(*LoginPage.err_msg)

    def get_forgotlogin(self):
        return self.driver.find_element(*LoginPage.forgot_login)

    def get_register(self):
        return self.driver.find_element(*LoginPage.register)

    def login(self,user,pwd):
        usrname = self.get_username()
        usrname.send_keys(user)
        pswd = self.get_password()
        pswd.send_keys(pwd)
        submit = self.get_submitbutton()
        submit.click()
        time.sleep(5)