from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager  # use pip install webdriver-manager
from selenium.webdriver.chrome.service import Service

class DriverFactory:
    def get_driver(self, browserName):
        if browserName == 'Chrome':
            options = webdriver.ChromeOptions()
            options.binary_location = "C:\\Software\\ElectronAPIDemosSetup.exe"
            driver = webdriver.Chrome(ChromeDriverManager(options=options).install())
        elif browserName == 'FireFox':
            pass
        return driver

    def set_desire_Capabilities(self):
        #service = Service("/usr/local/bin/chromedriver")
        #service.start()

        options = webdriver.ChromeOptions()
        options.binary_location = "C:\\Software\\ElectronAPIDemosSetup.exe"
        driver = webdriver.Chrome(ChromeDriverManager(options=options).install())
        #driver = webdriver.Chrome(options=options)
        return driver
