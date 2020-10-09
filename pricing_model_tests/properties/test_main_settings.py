from pricing_model_tests.properties.property_utility import PropUtils


class MainSettings(PropUtils):

    def test_main_settings(self):
        # Login and go to properties page
        self.login_action(self.env)
        self.select_sidebar_item(item="Properties")

        # Select property either thru external data or use the random property generator
        random_property = self.random_property_generator()
        self.select_property(random_property)

        # Assert property access
        try:
            if self.deferred_assert_text("Property information", self.property_details_header):
                print("\nProperty details page is accessed successfully")
        except Exception as e:
            self.save_screenshot("PropertyAccessFailed")
            print(e)
            print("Acutal text = " + self.find_element(self.property_details_header).text)

        # Select room type by random for now, since the property is selected randomly
        self.sleep(2)
        self.select_roomtype_settings()

        # Fill main settings form
        self.main_settings_form_random()
        self.sleep(2)

        # Assert success message after saving and excute teardown
        try:
            if self.deferred_assert_element(self.success_message):
                print("\nMain settings saved successfully")
        except Exception as e:
            self.save_screenshot("SaveSettingsFailed")
            print(e)
        finally:
            self.process_deferred_asserts()
            self.tearDown()
