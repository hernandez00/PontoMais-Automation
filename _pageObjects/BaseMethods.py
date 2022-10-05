from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException


class Base(object):
    def __init__(self, driver):
        self._driver = driver

    def find_textfield(self, element_value):
        try:
            element = WebDriverWait(self, 15).until(EC.visibility_of_element_located((
                element_value)))

            element = WebDriverWait(self, 15).until(EC.element_to_be_clickable((
                element_value)))

        except TimeoutException:
            return False
        return element

    def find_button(self, element_value):
        try:
            element = WebDriverWait(self, 15).until(EC.visibility_of_element_located((
                element_value)))

            element = WebDriverWait(self, 15).until(EC.element_to_be_clickable((
                element_value)))

        except TimeoutException:
            return False
        return element

    def find_text(self, element_value):
        try:
            element = WebDriverWait(self, 15).until(EC.presence_of_element_located((
                element_value)))

        except TimeoutException:
            return False
        print(element.text)
        return element.text
