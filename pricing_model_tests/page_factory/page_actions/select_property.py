from seleniumbase import BaseCase


class SelectProperty(BaseCase):

    def select_property(self, selected_prop_name="Casamara"):
        # Selecting a property by name in the properties table
        self.click(f'//tbody/tr/td[1]/a[contains(., "{selected_prop_name}")]')
