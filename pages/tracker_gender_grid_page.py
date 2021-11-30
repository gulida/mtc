import time


from ..locators.tracker_gender_grid_locators import TrackerGenderLocators
from ..locators.tracker_common_locators import TrackerCommonLocators
from ..variables.tracker_gender_grid_variables import TrackerGenderVariables

from ..components.grid_component import GridComponent


class TrackerGenderPage(GridComponent):
    table = 'OF SEX TABLE'
    table_name = 'NO NAME'

    gender_data = TrackerGenderVariables.gender_data

    def test_gender_table(self):
        # self.click_button(*TrackerGenderLocators.SEARCH_BUTTON, f'SEARCH BUTTON {self.table}')
        # time.sleep(2)
        # SEARCH IN TABLE
        data = self.search_from_table(*TrackerGenderLocators.SEARCH_BUTTON,
                                      *TrackerGenderLocators.SEARCH_INPUT,
                                      *TrackerGenderLocators.TABLE_DATA_NAME,
                                      self.gender_data['search_data'], 'GENDER')
        print('FOUND DATA IN NAME COLUMN: ', data)

        table_name = self.get_table_name(*TrackerGenderLocators.TABLE_NAME, 'GENDER')

        # Adding data to the table
        # self.add_table_entry(data, *TrackerGenderLocators.ADD_BUTTON, self.gender_data, *TrackerGenderLocators.SAVE_BUTTON, table_name)

        # Editing a table entry
        # self.edit_table_entry(data, *TrackerGenderLocators.EDIT_BUTTON, self.gender_data, *TrackerGenderLocators.SAVE_BUTTON, table_name)

        # Deleting a table entry
        # self.delete_table_entry(data, *TrackerGenderLocators.DELETE_BUTTON, '###', *TrackerCommonLocators.ACCEPT, table_name)

        # Get entry count
        # entry_count = self.get_count_of_entry(*TrackerGenderLocators.SEARCH_BUTTON,
        #                                       *TrackerGenderLocators.SEARCH_INPUT,
        #                                       # *TrackerGenderLocators.SEARCH_INPUT_CLOSE,
        #                                       *TrackerGenderLocators.TABLE_DATA_NAME, 'admin', table_name)
        # print('COUNT OF FOUND DATA:', entry_count)

        # data = self.get_column_data(*TrackerGenderLocators.TABLE_DATA_NAME)

        # next_arrow_flag = True
        # column_data = {}
        column_data = self.search_from_table_for_edit_delete(*TrackerGenderLocators.SEARCH_BUTTON,
                                                             *TrackerGenderLocators.SEARCH_INPUT,
                                                             *TrackerGenderLocators.TABLE_DATA_NAME,
                                                             *TrackerGenderLocators.EDIT_BUTTON,
                                                             *TrackerGenderLocators.DELETE_BUTTON,
                                                             self.gender_data['search_data'], table_name)
        # found_data = self.browser.find_elements(*TrackerGenderLocators.TABLE_DATA_NAME)
        # while next_arrow_flag:
        #     found_data_array = []
        #     found_data = self.browser.find_elements(*TrackerGenderLocators.TABLE_DATA_NAME)
        #     for data in found_data:
        #         found_data_array.append(data.text)
        #     full_string = self.browser.find_element(*TrackerCommonLocators.SHOWED_ITEM_COUNT).text
        #     dict_key = full_string.split('-')[0]
        #     column_data.update({dict_key: found_data_array})
        #     next_button = self.browser.find_element(*TrackerCommonLocators.PAGINATION_NEXT_BUTTON)
        #     disabled_props = next_button.get_property('disabled')
        #     if not disabled_props:
        #         next_button.click()
        #         time.sleep(3)
        #     else:
        #         next_arrow_flag = False

        self.edit_table_entry(data, column_data, self.gender_data,
                                *TrackerGenderLocators.SAVE_BUTTON, table_name)

        # print('COLUMN DATA: ', column_data)
        # print('COLUMN DATA: ', found_data)
        # self.delete_table_entry(data, column_data, 'admin', *TrackerCommonLocators.ACCEPT, table_name)

    def test_gender_form_validation(self):
        self.click_button(*TrackerGenderLocators.ADD_BUTTON, 'ADD')
        time.sleep(3)
        self.click_button(*TrackerGenderLocators.SAVE_BUTTON, 'SAVE')

