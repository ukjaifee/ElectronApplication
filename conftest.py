import pytest
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

from data.StaticWorkStationData import StaticWorkStationData
from driverFactory.DriverFactory import DriverFactory

driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", "--item_name",action="store", default="type1",
    )

@pytest.fixture(scope="class")
def setup(request):
    global driver
    options = Options()
    #capabilities = DesiredCapabilities();
    #chromeOptions.setBinary("C:\\Software\\chromedriver.exe")
    options.binary_location="C:\\Users\\Umesh_Kumar\\AppData\\Local\\slack\\slack.exe"
    #options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
    options.add_argument('--no-sandbox')
    options.add_argument('--window-size=1420,1080')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-software-rasterizer')
    options.add_argument('--disable-gpu')
    options.add_argument("--disable-gpu-compositing")
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-cache')
    #options.add_argument("--remote-debugging-port=9222")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.maximize_window()
    yield
    driver.close()






