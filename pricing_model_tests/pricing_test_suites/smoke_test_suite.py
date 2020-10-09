from pricing_model_tests.pricing_test_suites.test_suite_utility import TestSuiteUtils


class SmokeTestSuite(TestSuiteUtils):
    """
    place all smoke test scripts under this method,
    export the class on any package for recycling
    """
    def smoke_test_list(self):
        self.test_login_successfully(self.env)
        self.test_logout_successfully(self.env)
