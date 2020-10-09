from pricing_model_tests.page_factory.page_actions.forgot_password_actions import ForgotPass


class LoginUtility(ForgotPass):

    # Forgot pasword page assert mehtod
    def assert_forgotpass_page(self, text, element):
        try:
            if self.assert_exact_text(text, element, timeout=10):
                print("\nForgot password process is working fine")
        except Exception as e:
            self.save_screenshot("ForgotPasswordFail")
            print(e)
        finally:
            self.tearDown()

    # Post login assertion method
    def assert_post_login(self, env):
        if env == "staging":
            # Assert Dashboard page after logging in on Staging V2
            try:
                if self.assert_text("Dashboard", timeout=10):
                    print("\nLogin function works")
            except Exception as e:
                self.save_screenshot("LoginFailV2Staging")
                print(e)
        if env == "production":
            # Assert properties list page after logging in on Live V1
            try:
                if self.assert_text("Please select the property you want to price"):
                    print("\nLogin function works")
            except Exception as e:
                self.save_screenshot("LoginFailV1Live")
                print(e)

    def assert_post_logout(self):
        try:
            self.assert_element_present(self.login_link, timeout=10)
            print("\nLogout function works")
        except Exception as e:
            self.save_screenshot("LoginLinkMissing")
            print(e)
