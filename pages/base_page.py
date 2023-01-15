from browser import Browser
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class BasePage(Browser):

    def wait_for_elem(self, by, selector):
        WebDriverWait(self.driver,25).until(EC.presence_of_element_located((by,selector)))

    def wait_and_click_elem(self, by, selector):
        WebDriverWait(self.driver, 25).until(EC.presence_of_element_located((by, selector)))
        self.driver.find_element(by,selector).click()

    def wait_and_fill_elem_by_selector(self, by, selector, text):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((by, selector)))
        self.driver.find_element(by, selector).send_keys(text)

    def select_elem_by_select_by_value(self, by, selector, text):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((by, selector)))
        Select(self.driver.find_element(by, selector)).select_by_value(text)

    def select_elem_by_select_by_text(self, by, selector, text):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((by, selector)))
        Select(self.driver.find_element(by, selector)).select_by_visible_text(text)

    def verify_page_url(self, expected_url):
        actual_url = self.driver.current_url
        self.assertEqual(actual_url,expected_url, "The url is incorrect")

    def verify_text_visible(self, by, selector, expected_text):
        actual_text = self.driver.find_element(by, selector).text
        self.assertEqual(actual_text, expected_text, "Text is not visible")

    def wait_scroll_and_click_elem_by_selector(self, by, selector):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((by, selector)))
        elem = self.driver.find_element(by, selector)
        self.driver.execute_script("arguments[0].scrollIntoView();", elem)
        self.driver.execute_script("arguments[0].click();", elem)

