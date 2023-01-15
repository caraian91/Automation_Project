from pages.base_page import BasePage
from pages.register_user_page import RegisterUser

# it is run before each test
def before_all(context):
    context.base_page = BasePage()
    context.register_user_page = RegisterUser()

# is run after the test
def after_all(context):
    context.browser.close()