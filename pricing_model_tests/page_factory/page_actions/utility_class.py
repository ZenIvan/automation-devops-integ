from random import randint

from seleniumbase import BaseCase

from pricing_model_tests.page_factory.page_objects.dashboard_page_objects import Dashboard
from pricing_model_tests.page_factory.page_objects.login_page_object import LoginPage
from pricing_model_tests.page_factory.page_objects.properties_page_objects import Properties
from pricing_model_tests.page_factory.page_objects.readme_page_object import ReadMe


class UtilityClass (BaseCase, Dashboard, LoginPage,
                    Properties, ReadMe):

    # RNG function based on dynamic lenghts
    @staticmethod
    def random_number_generator(length):
        value = randint(1, length)
        return value

    # Generates a random normal price from 500 - 800
    @staticmethod
    def random_normal_price():
        normal_price = randint(500, 800)
        return normal_price
