import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import webbrowser
import select as something
from selenium.webdriver.common.action_chains import ActionChains



class TestElectron:
    aboutApp = (By.ID, "button-about")
    atomDoc = (By.XPATH,
               "//atom-workspace-axis[@class='vertical']/descendant::div[@class='welcome']/descendant::a[text()='Atom docs']")

    def get_driver(self):
        options = webdriver.ChromeOptions()
        options.binary_location = "C:\\Users\\Umesh_Kumar\\AppData\\Local\\atom\\atom.exe"
        driver = webdriver.Chrome(executable_path="C:\\driver\\chromedriver_win32\\chromedriver.exe", options=options)
        # driver.maximize_window()
        return driver

    def test_verify_check_box(self):
        driver = self.get_driver()
        time.sleep(4)
        flag = driver.find_element(By.XPATH,"//atom-workspace-axis[@class='vertical']/descendant::label/input").is_selected()
        print("The value of flag is", flag)
        assert flag == True
        self.get_change_theme(driver)

    def get_change_theme(self, driver):
        driver.find_element(By.XPATH, "//atom-workspace-axis[@class='vertical']/descendant::span[text()='Theme']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[text()='Open the theme picker']").click()
        dropDownElement = driver.find_element(By.XPATH, "//Select[1]")
        action = ActionChains(driver)
        action.click(dropDownElement)
        ele = driver.find_elements(By.XPATH, "//option")
        for element in ele:
            print(element.text)
            if element.text == "Atom Dark":
                element.click()
                break
