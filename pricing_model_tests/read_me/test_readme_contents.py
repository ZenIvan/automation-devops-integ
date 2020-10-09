from pricing_model_tests.read_me.readme_utility import ReadMeUtility


class VerifyReadMe(ReadMeUtility):

    def test_content_readme(self):
        # Login and Access Read Me page
        self.login_action(self.env)
        self.select_sidebar_item(item="Read me")

        # Assert read me content method
        self.assert_read_me_contents()
