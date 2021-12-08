from abc import ABC, abstractmethod

from selenium.webdriver.support.wait import WebDriverWait


class AbstractComponent(ABC):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    @abstractmethod
    def is_Displayed(self):
        pass
