from Components.HomePageComponent import HomePageComponent


class AtomMainPage:
    def __init__(self, driver):
        self.driver=driver

    def home_Component(self):
        return HomePageComponent(self.driver)
