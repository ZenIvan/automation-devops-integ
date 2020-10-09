from pricing_model_tests.login.login_utils import LoginUtility


class LogoutTest (LoginUtility):
    """
    Test Case:
    -----------------------------------------------------------------------
    1. Login on Pricing V2 Staging (Invoke argument --env=staging on CLI)
    2. Assert post-login page
    3. Click Logout/Sign-out button
    4. Assert post-logout page
    5. Click return to login link
    6. Assert login page
    """
    def test_logout_successfully(self):
        # Login action script
        self.login_action(self.env)

        # Assert post-login page
        self.assert_post_login(self.env)

        # Click Logout button
        self.click(self.sign_out)

        # Assert post-logout page
        self.assert_post_logout()

        # Click login page link
        self.click(self.login_link)

        # Assert login page
        try:
            self.assert_element_present(self.username, timeout=10)
            print("\nLogin page is present")
        except Exception as e:
            self.save_screenshot("LoginPagePostLogoutFail")
            print(e)
