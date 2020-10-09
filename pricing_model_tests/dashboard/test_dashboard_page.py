from pricing_model_tests.dashboard.dashboard_utility import DashboardUtility


class DashboardPage(DashboardUtility):

    def test_dashboard_assert(self):
        # Login method
        self.login_action(self.env)

        # Assert dashboard access
        try:
            if self.assert_exact_text("Dashboard", self.dashboard_header):
                print("\nDashboard accessed successfully")
        except Exception as e:
            self.save_screenshot("DashboardAccessFail")
            print(e)
            print("Actual text = " + self.find_element(self.dashboard_header).text)

        # Function call for random selection of filter items
        self.select_filter_items()

        # Assert selected items in the filters and other page objects on Dashboard page
        self.sleep(2)
        self.assert_dashboard_post_test()
