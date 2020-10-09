from zenrooms_tests.page_actions import PageActions

class ZenroomsWebsite(PageActions):

    def test_zenrooms_home_page(self):
        self.visit_zenrooms_home_page()
        self.is_element_visible("#currency_switch")
        self.is_element_visible("language_switch")
        self.is_element_visible("#searchText")