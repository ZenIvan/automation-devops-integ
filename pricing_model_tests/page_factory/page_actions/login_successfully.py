from pricing_model_tests.page_factory.page_actions.utility_class import UtilityClass
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


class LoginSuccess(UtilityClass):

    def tearDown(self):
        self.save_teardown_screenshot()
        self.delete_saved_cookies()
        super(LoginSuccess, self).tearDown()

    def login_action(self, env):
        self.set_window_size(1920, 1080)
        self.maximize_window()
        staging = os.getenv('STAGING_V2')
        live = os.getenv('LIVE_V1')

        # Always remember to add --env=staging or production on the test run CLI
        if env == "staging":
            self.open(staging)
        if env == "production":
            self.open(live)
        super_user = os.getenv('SUPER_USER_PMV2')
        su_password = os.getenv('SU_PMV2_PASSWORD')
        self.type(self.username, super_user)
        self.type(self.password, su_password+"\n")
git