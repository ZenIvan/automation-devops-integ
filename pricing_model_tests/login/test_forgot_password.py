from pricing_model_tests.login.login_utils import LoginUtility


class ForgotPasswordTest(LoginUtility):

    def test_forgot_password(self):
        # Forgot password page actions
        self.forgot_password_action(env=self.env)

        # Assert the success of forgot password
        self.sleep(2)
        self.assert_forgotpass_page(text="Check your inbox!", element=self.forgot_success_header)
