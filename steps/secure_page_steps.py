from behave import *

@then('Secure Page: I can login and see the secure page')
def step_impl(context):
    context.secure_page.object.check_success_message()

@when('Secure Page: I can login and see the secure page')
def step_impl(context):
    context.secure_page.object.check_success_message()

@when('Secure Page: I click the logout button')
def step_impl(context):
    context.secure_page_object.click_logout()