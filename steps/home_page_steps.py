from behave import *

@given('Home Page: I am on the home page')
def step_impl(context):
    context.home_page_object.navigate_home_page()

@when('Home Page: I click on the link "<link>"')
def step_impl(context):
    context.home_page_object.click_link()

@then('Home Page: I am taken to the page "<expected_url>"')
def step_impl(context, expected_url):
    context.home_page_object.check_link_url(expected_url)