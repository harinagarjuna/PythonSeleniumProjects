import time

import pytest
from selenium.webdriver.common.by import By

from tests_parabank.pageObjects.loginpage import LoginPage
from tests_parabank.pageObjects.registerPage import RegisterPage
from tests_parabank.pageObjects.account_services import AccountServices
from selenium import webdriver

@pytest.fixture(autouse=True)
def setup():
    driver = webdriver.Chrome()
    driver.get("https://parabank.parasoft.com/parabank/index.html")
    driver.maximize_window()
    time.sleep(3)
    yield driver

def test_login_negative(setup):
    driver = setup
    LoginPageObject = LoginPage(driver)
    LoginPageObject.login(user="Hari",pwd="Test")
    err = LoginPageObject.get_errormessage()
    assert "error" in err.text
    tear_down(setup)

def test_login_positive(setup):
    driver = setup
    LoginPageObject = LoginPage(driver)
    LoginPageObject.login(user="HariOne",pwd="HariOne@123")
    accountservices = AccountServices(driver)
    #welcome_user_text = accountservices.get_welcome_text().text
    welcome_user_text = accountservices.text_welcome()

    assert welcome_user_text == "Welcome HariOne Test", "Wrong User"
    print(welcome_user_text)
    accountservices.get_logout().click()
    tear_down(setup)


def test_login_userBalance(setup):
    driver = setup
    LoginPageObject = LoginPage(driver)
    LoginPageObject.login(user="HariOne",pwd="HariOne@123")
    accountservices = AccountServices(driver)
    welcome_user_text = accountservices.text_welcome()
    user_balance = float((accountservices.get_balance().text).replace('$', ''))
    logout = accountservices.get_logout()
    assert welcome_user_text == "Welcome HariOne Test", "Wrong User"
    assert user_balance == 515.50, "Invalid Amount"
    print(user_balance)
    logout.click()
    tear_down(setup)


def test_login_userTotalAmount(setup):
    driver = setup
    LoginPageObject = LoginPage(driver)
    LoginPageObject.login(user="HariOne",pwd="HariOne@123")
    accountservices = AccountServices(driver)
    welcome_user_text = accountservices.get_welcome_text().text
    user_total = float((accountservices.get_balance().text).replace('$', ''))
    assert welcome_user_text == "Welcome HariOne Test", "Wrong User"
    logout = accountservices.get_logout()
    assert user_total == 515.50, "Incorrect Total"
    logout.click()
    tear_down(setup)

def test_register_positive(setup):
    driver = setup
    LoginpageObject = LoginPage(driver)
    register = LoginpageObject.get_register()
    register.click()
    RegisterPageObject = RegisterPage(driver)
    RegisterPageObject.register_page(fname='HariOne',lname='Test',Address='Test Address,Down Town,India',City='Chennai',State='Tamilnadu',Zip='60103',Phone='1234567890',Ssn='123',Confirm='HariOne@123',Username='HariOne',Password='HariOne@123')
    # err = LoginPageObject.get_errormessage()
    # assert "error" in err.text
    tear_down(setup)

# def test_parabank():
#   driver = webdriver.Chrome()
#   driver.get("https://parabank.parasoft.com/parabank/index.html")
#   register = driver.find_element(By.XPATH, "//*[@id='loginPanel']/p[2]/a")
#   register.click()
#   time.sleep(3)
#   rows = driver.find_elements(By.XPATH, "//table[@class='form2']/tbody/tr")
#   columns = driver.find_elements(By.XPATH, "//table[@class='form2']/tbody/tr[1]/td[1]")
#   first = "//table[@class='form2']/tbody/tr["
#   second = "]/td[1]"
#   td_second = "]/td[2]"
#   third = "/input"
#   for i in range(1,len(rows)):
#       first_path = f"{first}{i}{second}"
#       first_path_full = driver.find_element(By.XPATH, first_path).text
#       if i == 13:
#         # check_button = f"{first}{i}{td_second}{third}"
#         # check_button_full = driver.find_element(By.XPATH,check_button)
#         # register_value = check_button_full.get_attribute("Register")
#         firstname_path = f"{first}{i}{td_second}{third}"
#         register = driver.find_element(By.XPATH, firstname_path)
#         print(register)
#       if first_path_full == "First Name:":
#           firstname_path = f"{first}{i}{td_second}{third}"
#           print(firstname_path)
#           first_name = driver.find_element(By.XPATH, firstname_path)
#           print(first_name)
#       elif first_path_full == "Last Name:":
#           firstname_path = f"{first}{i}{td_second}{third}"
#           last_name = driver.find_element(By.XPATH, firstname_path)
#           print(last_name)
#       elif first_path_full == "Address:":
#           firstname_path = f"{first}{i}{td_second}{third}"
#           Address = driver.find_element(By.XPATH, firstname_path)
#           print(Address)
#       elif first_path_full == "City:":
#           firstname_path = f"{first}{i}{td_second}{third}"
#           City = driver.find_element(By.XPATH, firstname_path)
#           print(City)
#       elif first_path_full == "State:":
#           firstname_path = f"{first}{i}{td_second}{third}"
#           State = driver.find_element(By.XPATH, firstname_path)
#           print(State)
#       elif first_path_full == "Zip Code:":
#           firstname_path = f"{first}{i}{td_second}{third}"
#           Zip_Code = driver.find_element(By.XPATH, firstname_path)
#           print(Zip_Code)
#       elif first_path_full == "Phone #:":
#           firstname_path = f"{first}{i}{td_second}{third}"
#           Phone = driver.find_element(By.XPATH, firstname_path)
#           print(Phone)
#       elif first_path_full == "SSN:":
#           firstname_path = f"{first}{i}{td_second}{third}"
#           SSN = driver.find_element(By.XPATH, firstname_path)
#           print(SSN)
#       elif first_path_full == "Username:":
#           firstname_path = f"{first}{i}{td_second}{third}"
#           username = driver.find_element(By.XPATH, firstname_path)
#           print(username)
#       elif first_path_full == "Password:":
#           firstname_path = f"{first}{i}{td_second}{third}"
#           password = driver.find_element(By.XPATH, firstname_path)
#           print(password)
#       elif first_path_full == "Confirm:":
#           firstname_path = f"{first}{i}{td_second}{third}"
#           confirm = driver.find_element(By.XPATH, firstname_path)
#           print(confirm)
#       else:
#           print("Empty Row")


def test_parabank_Two():
  driver = webdriver.Chrome()
  driver.get("https://parabank.parasoft.com/parabank/index.html")
  register = driver.find_element(By.XPATH, "//*[@id='loginPanel']/p[2]/a")
  register.click()
  time.sleep(3)
  first_name = driver.find_element(By.ID, "customer.firstName")
  first_name.send_keys("Hari One")
  time.sleep(3)






def tear_down(setup):
    dr = setup
    dr.quit()