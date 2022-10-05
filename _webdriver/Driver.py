from appium import webdriver


class Driver:
    def __init__(self):
        caps = {
            "platformName": "Android",
            "appium:deviceName": "192.168.100.130:5555",
            "deviceId": "192.168.100.130:5554",
            "appium:appPackage": "br.com.pontomais.v2",
            "appium:appActivity": "br.com.pontomais.v2.MainActivity"
        }
        self.instance = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
