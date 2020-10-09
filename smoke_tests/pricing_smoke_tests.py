from pricing_model_tests.pricing_test_suites.smoke_test_suite import SmokeTestSuite

"""
This will be the placeholder for all smoke tests on pricing model.New tests will be seeded on the SmokeTestSuite class,
and be inheritted in this file. So when pytest ./smoke_tests/ is invoked on the CI, or the terminal, it will run the 
inheritted tests from SmokeTestSuite.
"""


def pricing_smoke_list():
    SmokeTestSuite.smoke_test_list()
