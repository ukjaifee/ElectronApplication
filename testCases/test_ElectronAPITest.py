from pageObjects.EelectronAPIAPPMainPage import ElectronAPIAPPMainPage
from utility.BaseClass import BaseClass


class TestElectronAPIAPP(BaseClass):

    def test_electron_Api_APP(self):
        electronsAppPage=ElectronAPIAPPMainPage(self.driver)
        electronsAppPage.home_Component().is_Displayed()
        electronsAppPage.home_Component().click_About()

