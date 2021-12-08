from selenium.webdriver.common.by import By
from abstractComponent.AbstractComponent import AbstractComponent
from utility.BaseClass import BaseClass


class HomePageComponent(AbstractComponent, BaseClass):
    def __init__(self, driver):
        super().__init__(driver)

    # searchBox = (By.XPATH, "//input[@name='q']")
    aboutApp = (By.ID, "button-about")
    button = (By.ID, "button - windows")


    def is_Displayed(self):
        flag = self.is_visible(HomePageComponent.aboutApp)
        return flag

    def click_About(self):
        self.driver.find_element(*HomePageComponent.button).click()
