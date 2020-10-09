from pricing_model_tests.page_factory.page_actions.login_successfully import LoginSuccess
from pricing_model_tests.page_factory.page_actions.utility_class import UtilityClass
import os
from os.path import join, dirname
from dotenv import load_dotenv
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


class ForgotPass(LoginSuccess, UtilityClass):

    def forgot_password_action(self, env):
        if env == "staging":
            self.open(os.getenv('STAGING_V2'))
        if env == "production":
            self.open(os.getenv('LIVE_V1'))
        self.click(self.forgot_password)
        self.type(self.forgot_email, os.getenv('SU_PMV2_EMAIL'))
        self.click(self.forgot_submit)
