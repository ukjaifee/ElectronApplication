from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class TestElectron:
    aboutApp = (By.ID, "button-about")

    def test_electron(self):
        #service = Service("C:\\Software\\chromedriver.exe")
        #service.start()
        options = webdriver.ChromeOptions()
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
        #options.binary_location = "C:\\Users\\Umesh_Kumar\\AppData\\Local\\electron-api-demos\\Electron API Demos.exe"
        options.binary_location = "C:\\Users\\Umesh_Kumar\\AppData\\Local\\slack\\slack.exe"
        driver = webdriver.Chrome(executable_path="C:\\Users\\Umesh_Kumar\\Documents\\driver\\chromedriver.exe",options=options)
        #driver = webdriver.Chrome(options=options)

        driver.find_element(By.ID, "button-about").click()
