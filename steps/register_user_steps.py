from behave import *
from time import sleep

@given('registeruser: I am a user on Automation Exercise page')
def step_impl(context):
    context.register_user_page.navigate_to_home_page()

@when('registeruser: Verify that home page is visible successfully')
def step_impl(context):
    context.register_user_page.visible_btn_home_page()

@when('registeruser: Click on Signup / Login button')
def step_impl(context):
    context.register_user_page.click_signup_login_button()

@when('registeruser: Verify New User Signup! is visible')
def step_impl(context):
    context.register_user_page.text_visible_new_user_singup()

@when('registeruser: Enter name "{name}"')
def step_impl(context, name):
    context.register_user_page.set_name(name)

@when('registeruser: Enter email adress "{email_adress}"')
def step_impl(context, email_adress):
    context.register_user_page.set_email(email_adress)

@when('registeruser: Click Signup button')
def step_impl(context):
    context.register_user_page.click_signup_button()

@when('registeruser: Verify that ENTER ACCOUNT INFORMATION is visible')
def step_impl(context):
    context.register_user_page.text_visible_enter_account()

@when ('registeruser: Fill details: Title, Name, Email, "{password}", Date of birth "{day}","{months}","{years}"')
def step_impl(context, password, day, months, years):
    context.register_user_page.fill_details_1(password,day,months,years)
    sleep(3)

@when ('registeruser: Select checkbox Sign up for our newsletter!')
def step_impl(context):
    context.register_user_page.checkbox_newsletter_and_receive()

@when ('registeruser: Fill details: First name "{first_name}", Last name "{last_name}", Company "{company}", Address "{adress1}", Address2 "{adress2}", Country "{country}", State "{state}", City "{city}", Zipcode "{zipcode}", Mobile Number "{mobile_number}"')
def step_impl(context,first_name,last_name,company,adress1,adress2,country,state,city,zipcode,mobile_number):
    context.register_user_page.fill_details_2(first_name,last_name,company,adress1,adress2,country,state,city,zipcode,mobile_number)
    sleep(3)

@when ('registeruser: I click on Create Account button')
def step_impl(context):
    context.register_user_page.click_create_account()

@when ('registeruser: Verify that ACCOUNT CREATED! is visible')
def step_impl(context):
    context.register_user_page.text_visible_account_created()

@when ('registeruser: Click on the Continue button')
def step_impl(context):
    context.register_user_page.click_contiune_btn()

@when ('registeruser: Verify that Logged in as username is visible')
def step_impl(context):
    context.register_user_page.visible_btn_logout()

@when ('registeruser: Click on the Delete Account button')
def step_impl(context):
    context.register_user_page.click_delete_account()
    sleep(3)

@then ('registeruser: Verify that ACCOUNT DELETED! is visible and click Continue button')
def step_impl(context):
    context.register_user_page.click_contiune_btn()
