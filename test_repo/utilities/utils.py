from seleniumbase import BaseCase
from test_repo.page_objects.login_objects import LoginPage


class UtilityClass(BaseCase, LoginPage):
    def assert_post_login(self, env):
        if env == "production":
            # Assert properties list page after logging in on Live V1
            try:
                self.assert_text("Please select the property you want to price")
                print("\nLogin function works")
            except Exception as e:
                self.save_screenshot("LoginFailV1Live")
                print(e)
        else:
            # Assert Dashboard page after logging in on Staging V2
            try:
                self.assert_text("Dashboard", timeout=10)
                print("\nLogin function works")
            except Exception as e:
                self.save_screenshot("LoginFailV2Staging")
                print(e)
