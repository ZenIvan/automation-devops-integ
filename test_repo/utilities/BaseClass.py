import os
from test_repo.utilities.utils import UtilityClass
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


class BaseClass(UtilityClass):
    def setUp(self, **kwargs):
        super(BaseClass, self).setUp()
        self.delete_saved_cookies()
        self.set_window_size(1920, 1080)
        self.maximize_window()

    def tearDown(self):
        self.save_teardown_screenshot()
        super(BaseClass, self).tearDown()

    def login_action(self, env='staging'):
        # Environment values on .env file
        staging = os.getenv('STAGING_V2')
        live = os.getenv('LIVE_V1')

        # Always remember to add --env=staging or production on the test run CLI
        if env == "staging":
            self.open(staging)
        elif env == "production":
            self.open(live)
        else:
            self.open(staging)
        super_user = os.getenv('SUPER_USER_PMV2')
        su_password = os.getenv('SU_PMV2_PASSWORD')
        self.type(self.username, super_user)
        self.type(self.password, su_password+"\n")