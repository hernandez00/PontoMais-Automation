from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException


class Base(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 11)

    def find_textfield(self, element_value):
        try:
            element = self.wait.until(EC.visibility_of_element_located((
                element_value
            )))

            element = self.wait.until(EC.element_to_be_clickable)

        except TimeoutException:
            pass
        return element
    
    def find_button(self, element_value):
        try:
            element = self.wait.until(EC.visibility_of_element_located((
                element_value
            )))

            element = self.wait.until(EC.element_to_be_clickable((
                element_value
            )))
        except TimeoutException:
            pass
        return element