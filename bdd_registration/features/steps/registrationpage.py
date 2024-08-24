import time

from behave import given,when,then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('User entered Login Page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.globalsqa.com/angularJs-protractor/registration-login-example/#/login")
    context.driver.maximize_window()
    time.sleep(5)

@when('User clicks on Register button')
def step_impl(context):
    register = context.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/form/div[3]/a")
    register.click()
    time.sleep(4)


@when('User Enter "{firstname}" "{lastname}" "{username}" "{password}"')
def step_impl(context,firstname,lastname,username,password):
    fname = context.driver.find_element(By.XPATH, "//*[@id='firstName']")
    lname = context.driver.find_element(By.XPATH, "//*[@id='Text1']")
    uname = context.driver.find_element(By.XPATH, "//*[@id='username']")
    pwd = context.driver.find_element(By.XPATH, "//*[@id='password']")
    fname.send_keys(firstname)
    lname.send_keys(lastname)
    uname.send_keys(username)
    pwd.send_keys(password)
    time.sleep(5)

@when('User Click on Register')
def step_impl(context):
    register_button = context.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/form/div[5]/button")
    register_button.click()
    time.sleep(4)



@then('User should see text "{success_text}"')
def step_impl(context,success_text):
    msg = context.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]")
    #print(error_msg.text)
    assert success_text in msg.text


