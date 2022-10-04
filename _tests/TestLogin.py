import unittest
from _webdriver.Driver import Driver
from _pageObjects.LoginMethods import Login


class TestClass(unittest.TestCase):
    def setUp(self):
        self.driver = Driver()

    def tearDown(self):
        self.driver.instance.quit()

    def test_login(self):
        launchLogin = Login(self.driver.instance)
        launchLogin.execute_login()
        assert True