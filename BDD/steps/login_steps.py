from behave import *

@given('I am on the Jules login page')
def step_impl(context):
    context.login_page_object.navigate_to_login_page()

@when('I insert the correct email and correct password')
def step_impl(context):
    context.login_page_object.insert_correct_email()
    context.login_page_object.insert_correct_password()

@when('I click the login button')
def step_impl(context):
    context.login_page_object.click_login_button()

@then('I can login into the application')
def step_impl(context):
    context.search_page_object.check_url()
