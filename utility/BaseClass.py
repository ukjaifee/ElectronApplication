import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utility.Logging import Logging


@pytest.mark.usefixtures("setup")
class BaseClass(Logging):

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_all_elements_located(by_locator))
        return bool(element)