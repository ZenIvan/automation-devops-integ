from pricing_model_tests.page_factory.page_actions.utility_class import UtilityClass


class AssertReadMe(UtilityClass):

    def verify_readme_content(self):
        # Verify read me content sections
        section_list = ["Terminology", "Notification system",
                        "Website pages", "How to price a property"]
        for section in section_list:
            try:
                if self.deferred_assert_text(section):
                    print(f"\nHeader label {section} is seen in Read Me")
            except Exception as e:
                print(f"\nHeader label {section} is NOT seen/visible in Read Me!!")
                self.save_screenshot("ReadMeHeaderLabelFail")
                print(e)

        # Verify read me section contents
        section_contents = ["Occupancy rate", "Lead day", "Current occupancy curve",
                            "Target curve", "Allotment", "(Global) ceiling price",
                            "(Global) floor price", "Normal price", "Maximum discount",
                            "Maximum markup", "Floor price by day:", "Floor price by date",
                            "Cluster", "Aggressiveness", "Autopilot"]
        for contents in section_contents:
            try:
                if self.deferred_assert_text(contents):
                    print(f"\n{contents} is visible under Terminology")
            except Exception as e:
                print(f"\n{contents} is not visible under Terminology")
                self.save_screenshot("TerminologyItemFail")
                print(e)
            finally:
                self.process_deferred_asserts()
