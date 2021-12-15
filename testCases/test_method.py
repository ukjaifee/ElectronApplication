import pytest

from data.StaticWorkStationData import StaticWorkStationData
from pageObjects.GooglePage import GooglePage
from utility.BaseClass import BaseClass


class TestMethod(BaseClass):

    def testMethod1_Atom(self, getData, getDataFromTuple):
        log = self.get_log()
        #print(getData["fn"])
        print(getDataFromTuple[0])
        self.driver.get("https://www.google.com/")
        google = GooglePage(self.driver)
        flag = google.get_Search_Component().is_Displayed()
        print("The value of flage is", flag)
        log.info("I am running the test cases")
        log.warning("Its warning")
        log.debug("I am debugging")
        assert flag == True

    @pytest.fixture(params=StaticWorkStationData.staticWS)
    def getData(self, request):
        return request.param

    @pytest.fixture(params=StaticWorkStationData.staticWSTuple)
    def getDataFromTuple(self, request):
        return request.param

