from selenium.webdriver.common.by import By

from abstractComponent.AbstractComponent import AbstractComponent
from utility.BaseClass import BaseClass
from selenium.webdriver.support import expected_conditions as EC


class SearchWidgetComponent(AbstractComponent, BaseClass):
    def __init__(self, driver):
        super().__init__(driver)

    # searchBox = (By.XPATH, "//input[@name='q']")
    userEmail = (By.CSS_SELECTOR, "input#signup_email")

    def is_Displayed(self):
        flag = self.is_visible(SearchWidgetComponent.searchBox)
        return flag
