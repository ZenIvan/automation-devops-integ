from pricing_model_tests.page_factory.page_actions.utility_class import UtilityClass


class PropertyRand(UtilityClass):

    def random_property_generator(self):
        # List all property names and append them in a list variable
        property_name_list = self.find_elements(self.property_list)
        property_names = []
        for property_name in property_name_list:
            property_names.append(property_name.text)

        # Random room type generator
        property_count = len(property_names)
        value = self.random_number_generator(length=property_count)

        # Return the randomly selected property name
        return property_names[value - 1]
