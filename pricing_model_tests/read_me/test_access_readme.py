from pricing_model_tests.read_me.readme_utility import ReadMeUtility


class AccessReadMe(ReadMeUtility):

    def test_access_readme(self):
        # Login and Access Read Me page
        self.login_action(self.env)
        self.select_sidebar_item(item="Read me")

        # Assert Read Me access via header label method
        self.assert_read_me_access()
