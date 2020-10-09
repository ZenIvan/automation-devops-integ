from pricing_model_tests.page_factory.page_actions.verify_readme_content import AssertReadMe
from pricing_model_tests.page_factory.page_actions.login_successfully import LoginSuccess
from pricing_model_tests.page_factory.page_actions.sidebar_menu_selection import SidebarAction


class ReadMeUtility(AssertReadMe, LoginSuccess, SidebarAction):

    # Asser read me access actions
    def assert_read_me_access(self):
        try:
            if self.assert_text("Guidelines", self.readme_header):
                print("\n\nRead me access is successful")
        except Exception as e:
            self.save_screenshot("ReadMeAccessFail")
            print(e)
            print("Actual header label = "+self.find_element(self.readme_header).text)
        finally:
            self.tearDown()

    # Assert read me contents actions
    def assert_read_me_contents(self):
        try:
            self.verify_readme_content()
        except Exception as e:
            self.save_screenshot("ReadMeContentFail")
            print(e)
            print("Read me content has an issue")
        finally:
            self.tearDown()
