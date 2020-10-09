from pricing_model_tests.page_factory.page_actions.utility_class import UtilityClass
import os
from os.path import join
from dotenv import load_dotenv, find_dotenv


class ExportCsv(UtilityClass):
    """
    Page Actions
    ----------------------------
    1. Assert Export CSV button
    2. Clicks the export csv
    3. Assert if files were downloaded
    4. Assert the extensions of the files (.csv)
    """
    @property
    def trim_room_type_name(self):
        """
        Room type name is being fetched as "Family Room (Common)",
        this function splits the text from '(', then it removes
        white spaces on the right most side of the string by .rstrip()
        """
        rt_name_raw = self.get_text(self.room_type_family_room)
        rt_name_split = rt_name_raw.split("(")
        rt_name_final = rt_name_split[0].rstrip()
        return rt_name_final

    @property
    def trim_property_name(self):
        """
        Property name is being fetched as "> 8 Doors Inn Langkawi",
        this functions removes "> " by using .split(">")on the property name,
        and using .lstrip() for the white space on left side
        """
        prop_name_raw = self.get_text(self.property_details_name)
        prop_name_split = prop_name_raw.split(">")
        prop_name_final = prop_name_split[1].lstrip()
        return prop_name_final

    def assert_downloaded_csv(self, prop_name, rt_name):
        """
        Asserts the downloaded file by using seleniumbase's built-in assert
        method for dowloaded files .assert_downloaded_file, then deletes the
        file after asserting successfully in a try/catch's finally: statement
        """
        # dotenv setup for reading variables on .env file
        load_dotenv(find_dotenv())

        # Set file name format
        pkg_name = str(prop_name) + "-" + str(rt_name) + "-" + "PART1.csv"

        # Assert the downloaded file and delete it after test
        try:
            self.assert_downloaded_file(pkg_name, timeout=20)
            print("\nDownloaded file verified!!")
        except Exception as e:
            self.save_screenshot("DownloadedFileFail")
            print(e)
        finally:
            os.chdir(os.getenv("DOWNLOADED_FILES_PATH"))
            dl_file_path = os.getcwd()
            dl_file = join(dl_file_path, pkg_name)
            os.remove(dl_file)
            print(f"\nDownloaded file {pkg_name} has been deleted")

    def export_csv_action_assert(self):
        # Main method that's used on the test_csv_export.py
        # Assert if export csv button is present
        try:
            self.assert_element_present(self.export_csv_button)
        except Exception as e:
            self.save_screenshot("CSVExportButtonMissing")
            print(e)

        # Click the Export CSV on Family Room
        self.click(self.export_csv_button)
        print("\nExport CSV clicked")

        # Assert the downloaded file
        print("\nAsserting downloaded files...")
        rt_family_room = self.trim_room_type_name
        property_name = self.trim_property_name
        self.assert_downloaded_csv(prop_name=property_name, rt_name=rt_family_room)
