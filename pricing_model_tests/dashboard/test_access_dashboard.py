from pricing_model_tests.dashboard.dashboard_utility import DashboardUtility


class AccessDashboard(DashboardUtility):

    def test_access_dashboard(self):
        # Login, go to properties, click dashboard in the sidebar
        self.login_action(self.env)
        self.select_sidebar_item(item="Properties")
        self.select_sidebar_item(item="Dashboard")

        # Assert dashboard page access
        self.assert_dashboard_access_text()
