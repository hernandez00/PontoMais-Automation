from _pageObjects._locators.Login import LoginLocators
from _pageObjects.BaseMethods import Base

class Login(Base):

    def execute_login(self):
        Base.find_textfield(self.driver, LoginLocators.TEXTFIELD_LOGIN).send_keys('leonardo.hernandez@fmxsolucoes.com.br')
        Base.find_textfield(self.driver, LoginLocators.TEXTFIELD_PASSWORD).send_keys('HernandeZ!#%5')
        Base.find_button(self.driver, LoginLocators.BUTTON_LOGIN).click()