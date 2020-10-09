from pricing_model_tests.page_factory.page_actions.verify_dashboard import CheckSelectedItems
from pricing_model_tests.page_factory.page_actions.login_successfully import LoginSuccess
from pricing_model_tests.page_factory.page_actions.select_dashboard_filters_random import SelectFilters
from pricing_model_tests.page_factory.page_actions.sidebar_menu_selection import SidebarAction


class DashboardUtility(CheckSelectedItems, LoginSuccess,
                       SelectFilters, SidebarAction):

    # Dashboard access assert method
    def assert_dashboard_access_text(self):
        try:
            if self.assert_exact_text("Dashboard", self.dashboard_header):
                print("\nDashboard accessed successfully")
        except Exception as e:
            self.save_screenshot("DashboardAccessFail")
            print(e)
            print("Actual text = " + self.find_element(self.dashboard_header).text)

    # Assert selected filters and other dashboard objects
    def assert_dashboard_post_test(self):
        try:
            if self.verify_dashboard_items():
                print("\nDashboard items are validated as correct and complete")
        except Exception as e:
            self.save_screenshot("DashboardData&ObjectValidationFail")
            print(e)
