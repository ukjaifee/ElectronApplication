from Components.SearchWidgetComponent import SearchWidgetComponent


class GooglePage:

    def __init__(self, driver):
        self.driver = driver

    def get_Search_Component(self):

        return SearchWidgetComponent(self.driver)
