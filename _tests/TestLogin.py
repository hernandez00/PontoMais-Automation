import unittest
from _webDriver.Driver import Driver
from _pageObjects.LoginMethods import Login
from _pageObjects.HomeMethods import Home


class TestClass(unittest.TestCase):
    def setUp(self):
        self.driver = Driver()

    def tearDown(self):
        self.driver.instance.quit()

    def test_login(self):
        launchLogin = Login(self.driver.instance)
        launchLogin.execute_login()
        home = Home(self.driver.instance)
        assert home.is_logged()
