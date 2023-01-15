from selenium import webdriver
import unittest

class Browser(unittest.TestCase):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.set_page_load_timeout(10)
    driver.delete_all_cookies()

    def close(self):
        self.driver.close()
        self.driver.delete_all_cookies()