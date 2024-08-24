import time

import selenium
from selenium.webdriver.common.by import By

# f_name_value = None
# l_name_value = None
# add_value = None
# city_value = None
# state_value = None
# zip_value = None
# ph_value = None
# ssn_value = None
# username_value = None
# password_value = None
# confirm_value = None
# submit_button_value = None
class RegisterPage:

    def __init__(self,driver):
        self.driver = driver

    # def set_values(self):
    #     rows = self.driver.find_elements(By.XPATH, "//table[@class='form2']/tbody/tr")
    #     columns = self.driver.find_elements(By.XPATH, "//table[@class='form2']/tbody/tr[1]/td[1]")
    #     first = "//table[@class='form2']/tbody/tr["
    #     second = "]/td[1]"
    #     td_second = "]/td[2]"
    #     third = "/input"
    #     for i in range(1, len(rows)):
    #         first_path = f"{first}{i}{second}"
    #         first_path_full = self.driver.find_element(By.XPATH, first_path).text
    #         if i == 13:
    #             # check_button = f"{first}{i}{td_second}{third}"
    #             # check_button_full = driver.find_element(By.XPATH,check_button)
    #             # register_value = check_button_full.get_attribute("Register")
    #             RegisterPage.submit_button_value = f"{first}{i}{td_second}{third}"
    #         if first_path_full == "First Name:":
    #             RegisterPage.fname_value = f"{first}{i}{td_second}{third}"
    #         elif first_path_full == "Last Name:":
    #             RegisterPage.l_name_value = f"{first}{i}{td_second}{third}"
    #         elif first_path_full == "Address:":
    #             RegisterPage.add_value = f"{first}{i}{td_second}{third}"
    #         elif first_path_full == "City:":
    #             RegisterPage.city_value = f"{first}{i}{td_second}{third}"
    #         elif first_path_full == "State:":
    #             RegisterPage.state_value = f"{first}{i}{td_second}{third}"
    #         elif first_path_full == "Zip Code:":
    #             RegisterPage.zip_value = f"{first}{i}{td_second}{third}"
    #         elif first_path_full == "Phone #:":
    #             RegisterPage.zip_value = f"{first}{i}{td_second}{third}"
    #         elif first_path_full == "SSN:":
    #             RegisterPage.ssn_value = f"{first}{i}{td_second}{third}"
    #         elif first_path_full == "Username:":
    #             RegisterPage.username_value = f"{first}{i}{td_second}{third}"
    #         elif first_path_full == "Password:":
    #             RegisterPage.password_value = f"{first}{i}{td_second}{third}"
    #         elif first_path_full == "Confirm:":
    #             RegisterPage.confirm_value = f"{first}{i}{td_second}{third}"
    #         else:
    #             print("Empty Row")

    #locator value



    #page locators
    first_name = (By.ID, "customer.firstName")
    last_name = (By.ID, "customer.lastName")
    address = (By.ID, "customer.address.street")
    city = (By.ID, "customer.address.city")
    state = (By.ID, "customer.address.state")
    zipcode = (By.ID, "customer.address.zipCode")
    phone = (By.ID, "customer.phoneNumber")
    ssn = (By.ID, "customer.ssn")
    username = (By.ID, "customer.username")
    password = (By.ID, "customer.password")
    confirm = (By.ID, "repeatedPassword")
    submit_button = (By.XPATH, "//input[@value='Register']")

    #get all the webElements on the register page form

    def get_username(self):
        return self.driver.find_element(*RegisterPage.username)

    def get_password(self):
        return self.driver.find_element(*RegisterPage.password)

    def get_firstname(self):
        return self.driver.find_element(*RegisterPage.first_name)

    def get_lastname(self):
        return self.driver.find_element(*RegisterPage.last_name)

    def get_address(self):
        return self.driver.find_element(*RegisterPage.address)

    def get_city(self):
        return self.driver.find_element(*RegisterPage.city)

    def get_state(self):
        return self.driver.find_element(*RegisterPage.state)

    def get_zip(self):
        return self.driver.find_element(*RegisterPage.zipcode)

    def get_phone(self):
        return self.driver.find_element(*RegisterPage.phone)

    def get_ssn(self):
        return self.driver.find_element(*RegisterPage.ssn)

    def get_confirm(self):
        return self.driver.find_element(*RegisterPage.confirm)

    def get_register(self):
        return self.driver.find_element(*RegisterPage.submit_button)




    def register_page(self,fname,lname,Address,City,State,Zip,Phone,Ssn,Confirm,Username,Password):
       self.get_firstname().send_keys(fname)
       self.get_lastname().send_keys(lname)
       self.get_address().send_keys(Address)
       self.get_city().send_keys(City)
       self.get_state().send_keys(State)
       self.get_zip().send_keys(Zip)
       self.get_phone().send_keys(Phone)
       self.get_ssn().send_keys(Ssn)
       self.get_confirm().send_keys(Confirm)
       self.get_username().send_keys(Username)
       self.get_password().send_keys(Password)
       self.get_register().click()
       time.sleep(6)





