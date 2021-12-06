import time
from time import process_time

from ..locators.tracker_common_locators import TrackerCommonLocators
from ..locators.tracker_file_type_grid_locators import TrackerFileTypeLocators
from ..variables.tracker_file_type_variables import TrackerFileTypeVariables
from ..components.grid_component import GridComponent
from ..components.time_counter import running_time_counter
from ..components.bcolors import BColors


class TrackerFileTypePage(GridComponent):
    table_name = 'FILE TYPE'

    search_data = TrackerFileTypeVariables.file_type_data['search_data']

    def test_file_type_add_entry(self):
        start = process_time()
        table_name = self.get_table_name(*TrackerFileTypeLocators.TABLE_NAME, self.table_name)

        # found_data = self.search_from_table(*TrackerFileTypeLocators.SEARCH_BUTTON,
        #                                     *TrackerFileTypeLocators.SEARCH_INPUT,
        #                                     *TrackerFileTypeLocators.COLUMN_DATA_NAME,
        #                                     self.search_data, table_name)
        # # found_data = self.wait.until(self.search_from_table(*TrackerFileTypeLocators.SEARCH_BUTTON,
        # #                                                     *TrackerFileTypeLocators.SEARCH_INPUT,
        # #                                                     *TrackerFileTypeLocators.COLUMN_DATA_NAME,
        # #                                                     self.search_data, table_name))
        # time.sleep(1)
        # self.add_catalog_table_entry(found_data, *TrackerFileTypeLocators.ADD_BUTTON,
        #                              TrackerFileTypeVariables.file_type_data,
        #                              *TrackerFileTypeLocators.SAVE_BUTTON, table_name)
        #
        # time.sleep(2)
        # # Checking if the new entry was added
        # check_data = self.search_from_table(*TrackerFileTypeLocators.SEARCH_BUTTON,
        #                                     *TrackerFileTypeLocators.SEARCH_INPUT,
        #                                     *TrackerFileTypeLocators.COLUMN_DATA_NAME,
        #                                     self.search_data, table_name)
        # check_flag = True
        # if len(check_data):
        #     for i in range(len(check_data)):
        #         if check_data[i] == self.search_data:
        #             print(f'{BColors.OK} \nNew entry was added to {table_name} table!')
        #             check_flag = False
        #             break
        # if check_flag:
        #     print(f'{BColors.FAIL} \nNew entry was not added to {table_name} table!')
        self.add_new_entry_to_catalog_table(*TrackerFileTypeLocators.SEARCH_BUTTON,
                                            *TrackerFileTypeLocators.SEARCH_INPUT,
                                            *TrackerFileTypeLocators.COLUMN_DATA_NAME,
                                            self.search_data, *TrackerFileTypeLocators.ADD_BUTTON,
                                            TrackerFileTypeVariables.file_type_data,
                                            *TrackerFileTypeLocators.SAVE_BUTTON, table_name)
        end = process_time()
        running_time_counter(start, end, f'ADD ENTRY TO {table_name}')

    def test_file_type_edit_entry(self):
        start = process_time()
        table_name = self.get_table_name(*TrackerFileTypeLocators.TABLE_NAME, self.table_name)

        # found_data = self.search_from_table(*TrackerFileTypeLocators.SEARCH_BUTTON,
        #                                     *TrackerFileTypeLocators.SEARCH_INPUT,
        #                                     *TrackerFileTypeLocators.COLUMN_DATA_NAME,
        #                                     self.search_data, table_name)
        # found_data = self.wait.until(self.search_from_table(*TrackerFileTypeLocators.SEARCH_BUTTON,
        #                                                     *TrackerFileTypeLocators.SEARCH_INPUT,
        #                                                     *TrackerFileTypeLocators.COLUMN_DATA_NAME,
        #                                                     self.search_data, table_name))

        search_data = self.search_from_table_for_edit_delete(*TrackerFileTypeLocators.SEARCH_BUTTON,
                                                             *TrackerFileTypeLocators.SEARCH_INPUT,
                                                             *TrackerFileTypeLocators.COLUMN_DATA_NAME,
                                                             *TrackerFileTypeLocators.EDIT_BUTTON,
                                                             *TrackerFileTypeLocators.DELETE_BUTTON,
                                                             self.search_data, table_name)
        # search_data = self.wait.until(self.search_from_table_for_edit_delete(*TrackerFileTypeLocators.SEARCH_BUTTON,
        #                                                                      *TrackerFileTypeLocators.SEARCH_INPUT,
        #                                                                      *TrackerFileTypeLocators.COLUMN_DATA_NAME,
        #                                                                      *TrackerFileTypeLocators.EDIT_BUTTON,
        #                                                                      *TrackerFileTypeLocators.DELETE_BUTTON,
        #                                                                      self.search_data, table_name))
        # time.sleep(3)
        self.edit_catalog_table_entry(search_data, TrackerFileTypeVariables.file_type_data,
                                      *TrackerFileTypeLocators.SAVE_BUTTON, table_name)
        time.sleep(2)
        end = process_time()
        running_time_counter(start, end, f'EDIT ENTRY OF {table_name} TABLE')

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
