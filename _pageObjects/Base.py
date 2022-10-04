from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Base(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)

    def find_element(self, element):
