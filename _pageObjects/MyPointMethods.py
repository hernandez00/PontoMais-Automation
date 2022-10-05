from _pageObjects.BaseMethods import Base
from _pageObjects._locators.MyPoint import MyPointLocators


class MyPoint(Base):
    
    def is_in_progress(self):
        is_in_progress = Base.find_text(
            self._driver, MyPointLocators.TEXT_STATUS_OFFICEHOUR)

        if is_in_progress == "Expediente em andamento":
            print("Expediente em andamento!")
            return True
        else:
            print("Expediente não está em andamento!")
            return False
