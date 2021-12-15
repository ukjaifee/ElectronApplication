import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utility.Logging import Logging


@pytest.mark.usefixtures("setup")
class BaseClass(Logging):

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_all_elements_located(by_locator))
        return bool(element)

    def select_element_using_action_class(self, element):
        action = ActionChains(self.driver)
        action.click(element)

    def select_value_from_dropdown(self, ele, value):
        for element in ele:
            print(element.text)
            if element.text == value:
                element.click()
                break

