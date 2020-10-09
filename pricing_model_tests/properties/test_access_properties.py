from pricing_model_tests.properties.property_utility import PropUtils


class AccessProperties(PropUtils):

    def test_access_properties(self):
        # Login and access properties
        self.login_action(self.env)
        self.select_sidebar_item(item="Properties")

        # Verify if the properties page was accessed successfully
        self.assert_properties_page_access()
