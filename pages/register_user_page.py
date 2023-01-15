from time import sleep
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common import  NoSuchElementException
from selenium.webdriver.support.ui import Select

class RegisterUser(BasePage):
    # Atributs
    HOME_PAGE_VISIBLE = (By.XPATH,"//a[contains(text(),'Home')]")
    SIGNUP_LOGIN_BTN = (By.XPATH, "//a[contains(text(),'Signup / Login')]")
    NEW_USER_SINGUP_TEXT = (By.XPATH, "//h2[text()='New User Signup!']")
    NAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='Name']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[data-qa='signup-email']")
    SIGNUP_BTN = (By.XPATH, "//button[text()='Signup']")
    ENTER_ACCOUNT_INFORMATION_TEXT = (By.XPATH, "//*[text()='Enter Account Information']")
    TITLE_RATIO_SELECTION = (By.XPATH, "(//input[@name='title'])[1]")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[type='password']")
    DATE_OF_BIRTH_DAY_SELECTION = (By.CSS_SELECTOR, "#days")
    DATE_OF_BIRTH_MONTH_SELECTION = (By.CSS_SELECTOR, "#months")
    DATE_OF_BIRTH_YEAR_SELECTION = (By.CSS_SELECTOR, "#years")
    NEWSLETTER_RATIO_SELECTION = (By.CSS_SELECTOR, "#newsletter")
    RECEIVE_SPECIAL_RATIO_SELECTION = (By.CSS_SELECTOR, "#optin")
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "#first_name")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "#last_name")
    COMPANY_INPUT = (By.CSS_SELECTOR, "#company")
    ADRESS1_INPUT = (By.CSS_SELECTOR, "#address1")
    ADRESS2_INPUT = (By.CSS_SELECTOR, "#address2")
    COUNTRY_INPUT = (By.CSS_SELECTOR, "#country")
    STATE_INPUT = (By.CSS_SELECTOR, "#state")
    CITY_INPUT = (By.CSS_SELECTOR, "#city")
    ZIPCODE_INPUT = (By.CSS_SELECTOR, "#zipcode")
    MOBILE_NUMBER_INPUT = (By.CSS_SELECTOR, "#mobile_number")
    CREATE_ACCOUNT_BTN = (By.XPATH, "//button[text()='Create Account']")
    ACCOUNT_CREATED_TEXT = (By.XPATH, "//b[text()='Account Created!']")
    CONTINUE_BTN = (By.XPATH, "//a[@class='btn btn-primary']")
    LOGOUT_BTN = (By.XPATH, "//a[contains(text(),'Logout')]")
    DELETE_ACCOUNT = (By.XPATH, "//a[contains(text(),'Delete Account')]")

    # Methods
    def navigate_to_home_page(self):
        self.driver.get("https://automationexercise.com/")
        sleep(3)

    def visible_btn_home_page(self):
        elem_home = self.driver.find_element(*self.HOME_PAGE_VISIBLE)
        self.assertTrue(elem_home.is_displayed(), "The home page is not visible")

    def click_signup_login_button(self):
        self.wait_and_click_elem(*self.SIGNUP_LOGIN_BTN)

    def text_visible_new_user_singup(self):
        self.verify_text_visible(*self.NEW_USER_SINGUP_TEXT,"New User Signup!")

    def set_name(self, name):
        self.wait_and_fill_elem_by_selector(*self.NAME_INPUT, name)

    def set_email(self, email):
        self.wait_and_fill_elem_by_selector(*self.EMAIL_INPUT, email)

    def click_signup_button(self):
        self.wait_and_click_elem(*self.SIGNUP_BTN)

    def text_visible_enter_account(self):
        self.verify_text_visible(*self.ENTER_ACCOUNT_INFORMATION_TEXT,"ENTER ACCOUNT INFORMATION")

    def fill_details_1(self, password, day, months, years):
        # select Title Mr./Mrs.
        self.wait_and_click_elem(*self.TITLE_RATIO_SELECTION)
        # fill the PASSWORD
        self.wait_and_fill_elem_by_selector(*self.PASSWORD_INPUT, password)
        # select the DATE OF BIRTH
        # we use here the Select function
        self.select_elem_by_select_by_value(*self.DATE_OF_BIRTH_DAY_SELECTION, day)
        self.select_elem_by_select_by_text(*self.DATE_OF_BIRTH_MONTH_SELECTION, months)
        self.select_elem_by_select_by_value(*self.DATE_OF_BIRTH_YEAR_SELECTION, years)

    def checkbox_newsletter_and_receive(self):
        self.wait_and_click_elem(*self.NEWSLETTER_RATIO_SELECTION)
        self.wait_and_click_elem(*self.RECEIVE_SPECIAL_RATIO_SELECTION)

    def fill_details_2(self, first_name, last_name, company, adress1, adress2, country, state, city, zipcode, mobile_number):
        self.wait_and_fill_elem_by_selector(*self.FIRST_NAME_INPUT, first_name)
        self.wait_and_fill_elem_by_selector(*self.LAST_NAME_INPUT, last_name)
        self.wait_and_fill_elem_by_selector(*self.COMPANY_INPUT, company)
        self.wait_and_fill_elem_by_selector(*self.ADRESS1_INPUT, adress1)
        self.wait_and_fill_elem_by_selector(*self.ADRESS2_INPUT, adress2)
        self.select_elem_by_select_by_text(*self.COUNTRY_INPUT, country)
        self.wait_and_fill_elem_by_selector(*self.STATE_INPUT, state)
        self.wait_and_fill_elem_by_selector(*self.CITY_INPUT, city)
        self.wait_and_fill_elem_by_selector(*self.ZIPCODE_INPUT, zipcode)
        self.wait_and_fill_elem_by_selector(*self.MOBILE_NUMBER_INPUT, mobile_number)

    def click_create_account(self):
        self.wait_scroll_and_click_elem_by_selector(*self.CREATE_ACCOUNT_BTN)

    def text_visible_account_created(self):
        self.verify_text_visible(*self.ACCOUNT_CREATED_TEXT,"ACCOUNT CREATED!")

    def click_contiune_btn(self):
        self.wait_and_click_elem(*self.CONTINUE_BTN)

    def visible_btn_logout(self):
        elem = self.driver.find_element(*self.LOGOUT_BTN)
        self.assertTrue(elem.is_displayed(), "The logout button is not visible")

    def click_delete_account(self):
        self.wait_and_click_elem(*self.DELETE_ACCOUNT)


