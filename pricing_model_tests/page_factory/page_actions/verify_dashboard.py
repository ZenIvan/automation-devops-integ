from pricing_model_tests.page_factory.page_actions.utility_class import UtilityClass


class CheckSelectedItems(UtilityClass):

    def gather_selected_items(self):
        # List of dashboard dropdowns
        dropdown_elems = self.find_elements(self.dashboard_dropdowns)

        # Fetches dashboard items and places them on selected_item_list[]
        selected_item_list = []
        for item in dropdown_elems:
            selected_item_list.append(item.text)
        return selected_item_list

    def verify_dashboard_items(self):
        # Method call for dropdown filter fields's selected item fetch texts function
        sel_items = CheckSelectedItems.gather_selected_items(self)
        i = 0
        for items in sel_items:
            try:
                if self.deferred_assert_text(items):
                    print("\nSelected filters are correct! Item = " + items)
            except Exception as e:
                self.save_screenshot("DropdownItemFails")
                print(e)
            i += 1

        # Verifying the room nights and net revenue bar graph
        try:
            if self.deferred_assert_element(self.dashboard_chart):
                print("\nBar graph for room nights and revenue")
        except Exception as e:
            self.save_screenshot("GraphMissing")
            print(e)

        # Verify recent properties visited table
        try:
            if self.deferred_assert_element(self.dashboard_properties_table):
                print("\nRecent properties visited is visible")
        except Exception as e:
            self.save_screenshot("RecentPropertiesTableMissing")
            print(e)
        finally:
            self.process_deferred_asserts()
