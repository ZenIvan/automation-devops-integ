from pricing_model_tests.properties.property_utility import PropUtils


class TestCsvExport(PropUtils):
    """
    Test Case
    ------------------------------------------------------------------
    1. Access PM V2, Login, Access Properties, and Select a Property
    2. Verify Export CSV button in one of the room type/s
    3. Click Export CSV button
    4. Verify downloaded file/s
    5. Verify the extension of a downloaded file (.csv)
    """
    def test_csv_export(self):
        # Login, go to properties page, assert properties page access
        self.login_action(self.env)
        self.select_sidebar_item(item="Properties")
        self.assert_properties_page_access()

        # Select property either thru external data or use the random property generator
        test_property = "8 Doors"
        self.select_property(test_property)
        self.assert_property_details_access()

        # Export CSV download action ang assertion
        self.export_csv_action_assert()
