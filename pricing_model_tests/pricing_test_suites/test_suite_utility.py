from pricing_model_tests.login.test_login import LoginSuccessfullyTest
from pricing_model_tests.login.test_logout import LogoutTest


class TestSuiteUtils(LoginSuccessfullyTest, LogoutTest):
    pass
