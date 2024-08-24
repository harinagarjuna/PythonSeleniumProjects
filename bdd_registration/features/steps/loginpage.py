import time

from behave import given,when,then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('User on a Login Page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.globalsqa.com/angularJs-protractor/registration-login-example/#/login")
    context.driver.maximize_window()
    time.sleep(5)

@when('User Enters invalid "{username}" and invalid "{password}"')
def step_impl(context,username,password):
    uname = context.driver.find_element(By.XPATH, "//*[@id='username']")
    pwd = context.driver.find_element(By.XPATH, "//*[@id='password']")
    login_button = context.driver.find_element(By.XPATH, "//button[@class='btn btn-primary']")
    uname.send_keys(username)
    pwd.send_keys(password)
    login_button.click()
    time.sleep(5)

@then('User should see the "{error_message}"')
def step_impl(context,error_message):
    time.sleep(4)
    error_msg = context.driver.find_element(By.XPATH, "//div[@class='ng-binding ng-scope alert alert-danger']")
    print(error_msg.text)
    assert error_message in error_msg.text

# @given('User on a Login Page')
# def step_impl(context):
#         context.driver = webdriver.Chrome()
#         context.driver.get("https://www.globalsqa.com/angularJs-protractor/registration-login-example/#/login")
#         context.driver.maximize_window()
#         time.sleep(5)
#
# @when('User Enters valid "{username}" and valid "{password}"')
# def step_impl(context, username, password):
#         uname = context.driver.find_element(By.XPATH, "//*[@id='username']")
#         pwd = context.driver.find_element(By.XPATH, "//*[@id='password']")
#         login_button = context.driver.find_element(By.XPATH, "//button[@class='btn btn-primary']")
#         uname.send_keys(username)
#         pwd.send_keys(password)
#         print(password)
#         login_button.click()
#         time.sleep(5)
#
# @then('User should able to see login and url should be "{url}"')
# def step_impl(context, url):
#         time.sleep(4)
#         dashboard_url = "https://www.globalsqa.com/angularJs-protractor/registration-login-example/#/"
#         assert context.driver.current_url == dashboard_url
#
# @then('User should see "{name}" and text "{dashboard_text}" on the page on the page')
# def step_impl(context, name, dashboard_text):
#     username = context.driver.find_element(By.XPATH, "//div[@class='ng-scope']/h1")
#     d_text = context.driver.find_element(By.XPATH, "//div[@class='ng-scope']/p[1]")
#     assert name in username.text
#     assert d_text == dashboard_text
#


