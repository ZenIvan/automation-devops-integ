from pricing_model_tests.properties.property_utility import PropUtils


class TestSelectProp(PropUtils):

    def test_select_property(self):
        # Pre-conditions: Login, Go to Properties page, Select Property
        self.login_action(self.env)
        self.select_sidebar_item(item="Properties")
        self.select_property()

        # Assert property access and do post test clean-up
        self.assert_property_details_access()
