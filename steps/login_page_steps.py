from behave import *

@given('Login Page: I am on the Form Authentication login page')
def step_impl(context):
    context.login_page_object.navigate_login_page()

@when('Login Page: I insert the username "tomsmith" and the password "SuperSecretPassword!"')
def step_impl(context):
    context.login_page_object.correct_user()
    context.login_page_object.correct_pass()

@when('Login Page: I click the login button')
def step_impl(context):
    context.login_page_object.click_login()

@when('Login Page: I insert username "<username>" and password "<password>"')
def step_impl(context, username, password):
    context.login_page_object.insert_username(username)
    context.login_page_object.insert_pass(password)

@then('Login Page: I am taken back to the login page')
def step_impl(context, expected_url):
    context.login_page_object.check_loginPage_url(expected_url)

@then('Login Page: I cannot login and I receive error message "<error_message>"')
def step_impl(context, error_message):
    context.login_page_object.check_login_error_message(error_message)