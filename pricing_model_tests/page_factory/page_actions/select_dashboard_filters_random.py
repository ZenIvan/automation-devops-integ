from pricing_model_tests.page_factory.page_actions.utility_class import UtilityClass


class SelectFilters(UtilityClass):

    def random_selection_dropdown(self, counter):
        # list of dropdown fields
        list_types = ["selected_hotel", "walks_in",
                      "group_by_date", "time_frame"]
        # list of items in the dropdown list by element
        list_elems = self.find_elements(f'div[aria-labelledby="{list_types[counter]}"] a')
        # list of items in the dropdown list by text
        item_list = []
        for item in list_elems:
            item_list.append(item.text)

        # random item generator
        item_count = len(item_list)
        value = self.random_number_generator(length=item_count)

        # click the random item
        self.click(f'//div[@aria-labelledby="{list_types[counter]}"]/a[contains(., "{item_list[value - 1]}")]')

    def select_filter_items(self):
        # list of all dropdown fields
        dropdown_fields = self.find_elements(self.dashboard_dropdowns)
        i = 0

        # click each filter dropdown field 1-by-1
        for field in dropdown_fields:
            self.sleep(5)
            field.click()
            self.random_selection_dropdown(counter=i)
            i += 1
