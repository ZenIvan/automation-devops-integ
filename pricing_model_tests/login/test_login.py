from pricing_model_tests.login.login_utils import LoginUtility


class LoginSuccessfullyTest(LoginUtility):

    def test_login_successfully(self):
        # Login successfully page action
        self.login_action(env=self.env)

        # Assert method for both Staging V2 and Live V1
        self.sleep(2)
        self.assert_post_login(env=self.env)
