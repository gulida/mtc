import time

from ..locators.tracker_common_locators import TrackerCommonLocators
from ..locators.tracker_file_type_grid_locators import TrackerFileTypeLocators
from ..variables.tracker_file_type_variables import TrackerFileTypeVariables
from ..components.grid_component import GridComponent


class TrackerFileTypePage(GridComponent):
    table_name = 'FILE TYPE'

    search_data = TrackerFileTypeVariables.file_type_data['search_data']

    def test_file_type_add_entry(self):
        table_name = self.get_table_name(*TrackerFileTypeLocators.TABLE_NAME, self.table_name)

        found_data = self.search_from_table(*TrackerFileTypeLocators.SEARCH_BUTTON,
                                            *TrackerFileTypeLocators.SEARCH_INPUT,
                                            *TrackerFileTypeLocators.COLUMN_DATA_NAME,
                                            self.search_data, table_name)
        time.sleep(1)
        self.add_catalog_table_entry(found_data, *TrackerFileTypeLocators.ADD_BUTTON,
                                     TrackerFileTypeVariables.file_type_data,
                                     *TrackerFileTypeLocators.SAVE_BUTTON, table_name)
        # self.click_button(*TrackerFileTypeLocators.ADD_BUTTON, 'ADD')
        # time.sleep(2)
        # self.set_textbox_value(*TrackerFileTypeLocators.NAME, 'test', 'NAME FIELD')
        # self.set_textbox_value(*TrackerFileTypeLocators.DESCRIPTION, 'test', 'DESCRIPTION FIELD')
        # self.set_textbox_value(*TrackerFileTypeLocators.CODE, 'test', 'CODE FIELD')
        # time.sleep(3)
        # self.click_button(*TrackerFileTypeLocators.SAVE_BUTTON, 'SAVE')
        # time.sleep(3)

    def test_file_type_edit_entry(self):
        table_name = self.get_table_name(*TrackerFileTypeLocators.TABLE_NAME, self.table_name)

        found_data = self.search_from_table(*TrackerFileTypeLocators.SEARCH_BUTTON,
                                            *TrackerFileTypeLocators.SEARCH_INPUT,
                                            *TrackerFileTypeLocators.COLUMN_DATA_NAME,
                                            self.search_data, table_name)
        time.sleep(3)

        search_data = self.search_from_table_for_edit_delete(*TrackerFileTypeLocators.SEARCH_BUTTON,
                                                             *TrackerFileTypeLocators.SEARCH_INPUT,
                                                             *TrackerFileTypeLocators.COLUMN_DATA_NAME,
                                                             *TrackerFileTypeLocators.EDIT_BUTTON,
                                                             *TrackerFileTypeLocators.DELETE_BUTTON,
                                                             self.search_data, table_name)
        time.sleep(3)
        self.edit_catalog_table_entry(found_data, search_data, TrackerFileTypeVariables.file_type_data,
                                      *TrackerFileTypeLocators.SAVE_BUTTON, table_name)

    def test_file_type_delete_entry(self):
        table_name = self.get_table_name(*TrackerFileTypeLocators.TABLE_NAME, self.table_name)
        found_data = self.search_from_table(*TrackerFileTypeLocators.SEARCH_BUTTON,
                                            *TrackerFileTypeLocators.SEARCH_INPUT,
                                            *TrackerFileTypeLocators.COLUMN_DATA_NAME,
                                            self.search_data, table_name)

        search_data = self.search_from_table_for_edit_delete(*TrackerFileTypeLocators.SEARCH_BUTTON,
                                                             *TrackerFileTypeLocators.SEARCH_INPUT,
                                                             *TrackerFileTypeLocators.COLUMN_DATA_NAME,
                                                             *TrackerFileTypeLocators.EDIT_BUTTON,
                                                             *TrackerFileTypeLocators.DELETE_BUTTON,
                                                             self.search_data, table_name)
        time.sleep(3)
        self.delete_table_entry(found_data, search_data, self.search_data, *TrackerCommonLocators.ACCEPT, table_name)
        time.sleep(3)