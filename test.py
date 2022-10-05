import unittest
from _webDriver.Driver import Driver
from _pageObjects.LoginMethods import Login
from _pageObjects.HomeMethods import Home

driver = Driver()
launch = Login(driver.instance)
launch.execute_login()
home = Home(driver.instance)
assert home.is_logged()
driver.instance.quit()