from _pageObjects._locators.Home import HomeLocators
from _pageObjects.BaseMethods import Base


class Home(Base):

    def open_pointments(self):
        Base.find_button(self._driver, HomeLocators.BUTTON_MORE_INFO).click()
        Base.find_button(self._driver, HomeLocators.BUTTON_MY_POINT)

    def is_logged(self):
        is_logged = Base.find_text(self._driver, HomeLocators.LABEL_USER_NAME)

        if is_logged == "Leonardo Hernandez":
            print("Sucesso!")
            return True
        else:
            print("Deu ruim!")
            return False
