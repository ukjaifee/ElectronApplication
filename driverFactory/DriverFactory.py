from selenium import webdriver


class DriverFactory:
    def get_driver(self, browserName):
        if browserName == 'Chrome':
            options = webdriver.ChromeOptions()
            options.binary_location = "C:\\Users\\Umesh_Kumar\\AppData\\Local\\atom\\atom.exe"
            driver = webdriver.Chrome(executable_path="C:\\driver\\chromedriver_win32\\chromedriver.exe",
                                      options=options)
        elif browserName == 'FireFox':
            pass
        return driver
