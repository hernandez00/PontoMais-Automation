import unittest
from _webDriver.Driver import Driver
from _pageObjects.LoginMethods import Login
from _pageObjects.HomeMethods import Home
from _pageObjects.MyPointMethods import MyPoint

driver = Driver()
LoginScreen = Login(driver.instance)
LoginScreen.execute_login()
HomeScreen = Home(driver.instance)
assert HomeScreen.is_logged()

MyPointScreen = MyPoint(driver.instance)
MyPointScreen.is_in_progress()

driver.instance.quit()



    def test_login(self):
        LoginScreen = Login(self.driver.instance)
        LoginScreen.execute_login()
        HomeScreen = Home(self.driver.instance)
        print(date.today())
        assert HomeScreen.is_logged()
    
    def test_officehour_ongoing(self):
        self.test_login()
        MyPointScreen = MyPoint(self.driver.instance)
        assert MyPointScreen.is_in_progress()