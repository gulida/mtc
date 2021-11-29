import time


from ..locators.tracker_gender_grid_locators import TrackerGenderLocators
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
                                      # *TrackerGenderLocators.SEARCH_INPUT_CLOSE,
                                      *TrackerGenderLocators.TABLE_DATA_NAME,
                                      self.gender_data['search_data'], 'GENDER')
        print('FOUND DATA IN NAME COLUMN: ', data)

        table_name = self.get_table_name(*TrackerGenderLocators.TABLE_NAME, 'GENDER')

        # Adding data to the table
        self.add_table_entry(data, *TrackerGenderLocators.ADD_BUTTON, self.gender_data, *TrackerGenderLocators.SAVE_BUTTON, table_name)

        # Editing a table entry
        # self.edit_table_entry(data, *TrackerGenderLocators.EDIT_BUTTON, self.gender_data, *TrackerGenderLocators.SAVE_BUTTON, table_name)

        # Deleting a table entry
        # self.delete_table_entry(data, *TrackerGenderLocators.DELETE_BUTTON, '###', *TrackerCommonLocators.ACCEPT, table_name)

        # Get entry count
        entry_count = self.get_count_of_entry(*TrackerGenderLocators.SEARCH_BUTTON,
                                              *TrackerGenderLocators.SEARCH_INPUT,
                                              # *TrackerGenderLocators.SEARCH_INPUT_CLOSE,
                                              *TrackerGenderLocators.TABLE_DATA_NAME, 'admin', table_name)
        print('COUNT OF FOUND DATA:', entry_count)

    def test_gender_form_validation(self):
        self.click_button(*TrackerGenderLocators.ADD_BUTTON, 'ADD')
        time.sleep(3)
        self.click_button(*TrackerGenderLocators.SAVE_BUTTON, 'SAVE')

