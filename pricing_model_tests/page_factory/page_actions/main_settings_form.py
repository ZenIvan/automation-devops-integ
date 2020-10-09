from pricing_model_tests.page_factory.page_actions.utility_class import UtilityClass


class MainSettingsActions(UtilityClass):

    # Select items randomly function
    def select_dropdown_values(self):
        # List of all required dropdown fields in main settings
        dropdown_list = [self.quality_level, self.gender, self.main_settings_cluster]
        item_list = []

        # Select random items on each dropdown field
        for d_list in dropdown_list:
            dropdown_items = self.find_elements(f'//select[@id="{d_list}"]/option')
            for dd_items in dropdown_items:
                item_list.append(dd_items.text)
            item_count = len(item_list)
            rand_index = self.random_number_generator(length=item_count)
            self.sleep(1)
            self.select_option_by_index(f'//select[@id="{d_list}"]', rand_index - 1)
            item_list.clear()

    def input_prices(self):
        # List all required price fields
        price_fields = [self.normal_price, self.floor_price, self.ceiling_price]

        # Generate a random normal price from 500 - 800
        rand_normal_price = self.random_normal_price()

        # Fill each price fields
        for p_fields in price_fields:
            self.clear(p_fields)
            if p_fields == self.normal_price:
                self.input(p_fields, str(rand_normal_price))
            else:
                if p_fields == self.floor_price:
                    self.input(p_fields, str(rand_normal_price - 300))
                else:
                    if p_fields == self.ceiling_price:
                        self.input(p_fields, str(rand_normal_price + 500))
                    else:
                        continue

    def main_settings_form_random(self):
        # Open main settings form
        self.sleep(2)
        self.click(self.main_settings)

        # Select random data on the dropdown fields function
        self.sleep(2)
        self.select_dropdown_values()

        # Input prices on normal, floor, and ceiling price fields and click save
        self.sleep(1)
        self.input_prices()
        self.click(self.save_settings)
