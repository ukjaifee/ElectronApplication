from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from abstractComponent.AbstractComponent import AbstractComponent
from utility.BaseClass import BaseClass


class HomePageComponent(AbstractComponent, BaseClass):

    def __init__(self, driver):
        super().__init__(driver)

    # searchBox = (By.XPATH, "//input[@name='q']")
    aboutApp = (By.ID, "button-about")
    button = (By.ID, "button - windows")
    # aboutButton = (By.XPATH, "//button[text()='Add folders']")
    welcomeCheckBox = (By.XPATH, "//atom-workspace-axis[@class='vertical']/descendant::label/input")
    chooseTheme = (By.XPATH, "//atom-workspace-axis[@class='vertical']/descendant::span[text()='Theme']")
    openThemePicker = (By.XPATH, "//button[text()='Open the theme picker']")
    themeDropDown = (By.XPATH, "//Select[1]")
    dropDownOptions = (By.XPATH, "//option")

    def is_Displayed(self):
        flag = self.is_visible(HomePageComponent.welcomeCheckBox)
        return flag

    def check_welcome_checkbox(self):
        log = self.get_log()
        log.info("Verifying the welcome checkbox is selected")
        flag = self.driver.find_element(*HomePageComponent.welcomeCheckBox).is_selected()
        return flag

    def change_atom_theme(self, theme):
        try:
            log = self.get_log()
            log.info("Clicking the choose theme button")
            self.driver.find_element(*HomePageComponent.chooseTheme).click()
            self.driver.find_element(*HomePageComponent.openThemePicker).click()
            log.info("Clicking the open theme picker button")
            dropDownElement = self.driver.find_element(*HomePageComponent.themeDropDown)
            self.select_element_using_action_class(dropDownElement)
            log.info("Click the select theme dropdown")
            ele = self.driver.find_elements(*HomePageComponent.dropDownOptions)
            self.select_value_from_dropdown(ele, theme)
            log.info("Select a theme")
        except:
            log.error("The element not found", ele)
