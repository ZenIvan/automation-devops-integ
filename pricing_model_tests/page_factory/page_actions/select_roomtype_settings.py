from pricing_model_tests.page_factory.page_actions.utility_class import UtilityClass


class SelectPropertySettings(UtilityClass):

    # Selection will be based on room type name for Data Driven Testing
    def select_roomtype_settings(self):
        # Lists all the roomtypes in the property details page
        rt_list = []
        rt_items = self.find_elements(self.room_type_list)
        for rt in rt_items:
            rt_list.append(rt.text)

        # Random room type generator
        rt_count = len(rt_list)
        value = self.random_number_generator(length=rt_count)

        # Select function on which room type settings button will be clicked
        for lst in rt_list:
            if rt_list[value - 1] == lst:
                split_string = lst.split('(')
                rt_name = split_string[0].rstrip()
                self.click(f'//table/tbody[contains(., "{rt_name}")]/tr/td[4]/a')
                try:
                    if self.assert_text("1. Main settings", self.main_settings):
                        print("\nSettings page of selected property accessed successfully")
                except Exception as e:
                    self.save_screenshot("SettingsAccessFailed")
                    print(e)
            else:
                continue
