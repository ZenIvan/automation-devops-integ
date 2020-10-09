from pricing_model_tests.page_factory.page_actions.login_successfully import LoginSuccess
from pricing_model_tests.page_factory.page_actions.main_settings_form import MainSettingsActions
from pricing_model_tests.page_factory.page_actions.select_property import SelectProperty
from pricing_model_tests.page_factory.page_actions.select_roomtype_settings import SelectPropertySettings
from pricing_model_tests.page_factory.page_actions.sidebar_menu_selection import SidebarAction
from pricing_model_tests.page_factory.page_actions.random_property_selector import PropertyRand
from pricing_model_tests.page_factory.page_actions.verify_export_csv import ExportCsv


class PropUtils(LoginSuccess, MainSettingsActions, SelectProperty,
                SelectPropertySettings, SidebarAction, PropertyRand,
                ExportCsv):

    # Assert post access to properties page
    def assert_properties_page_access(self):
        try:
            if self.assert_exact_text("Properties", self.properties_header):
                print("\n\nProperties is accessed successfully")
        except Exception as e:
            self.save_screenshot("AccessPropertiesFailed")
            print(e)
            print("Actual header text = " + self.find_element(self.properties_header).text)

    # Assert post access to a property details page
    def assert_property_details_access(self):
        try:
            if self.assert_text("Property information", self.property_details_header):
                print("\nProperty details page is accessed successfully")
        except Exception as e:
            self.save_screenshot("PropertyAccessFailed")
            print(e)
            print("Acutal text = "+self.find_element(self.property_details_header).text)
