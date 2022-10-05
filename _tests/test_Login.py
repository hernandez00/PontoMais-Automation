import unittest
import pytest
from datetime import date
from _webDriver.Driver import Driver
from _pageObjects.LoginMethods import Login
from _pageObjects.HomeMethods import Home
from _pageObjects.MyPointMethods import MyPoint


class TestClass(unittest.TestCase):
    def setUp(self):
        self.driver = Driver()

    def tearDown(self):
        self.driver.instance.quit()

    @pytest.mark.skip(reason="No need test this.")
    def test_login(self):
        LoginScreen = Login(self.driver.instance)
        LoginScreen.execute_login()
        HomeScreen = Home(self.driver.instance)
        print(date.today())
        assert HomeScreen.is_logged()
    
    def test_officehour_ongoing(self):
        self.test_login()
        HomeScreen = Home(self.driver.instance)
        HomeScreen.open_pointments()
        MyPointScreen = MyPoint(self.driver.instance)
        assert MyPointScreen.is_in_progress()