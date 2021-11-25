import time

from ..locators.tracker_gender_grid_locators import TrackerGenderLocators
from ..variables.tracker_gender_grid_variables import TrackerGenderVariables

from ..components.grid_component import GridComponent


class TrackerGenderPage(GridComponent):
    table = 'OF SEX TABLE'
    table_name = 'NO NAME'

    gender_data = TrackerGenderVariables.gender_data

    def test_gender_table(self):
        self.click_button(*TrackerGenderLocators.SEARCH_BUTTON, f'SEARCH BUTTON {self.table}')
        time.sleep(2)
        # SEARCH IN TABLE
        data = self.search_from_table(*TrackerGenderLocators.SEARCH_INPUT, *TrackerGenderLocators.TABLE_DATA_NAME,
                                      self.gender_data['search_data'], 'GENDER')
        print('FOUND DATA IN NAME COLUMN: ', data)

        table_name = self.get_table_name(*TrackerGenderLocators.TABLE_NAME, 'GENDER')

        # Adding data to the table
        if len(data):
            print('This value is already exists in the table!!!')
        else:
            self.click_button(*TrackerGenderLocators.ADD_BUTTON, 'GENDER ADD BUTTON')
            time.sleep(3)
            self.add_edit_catalog_data(*TrackerGenderLocators.SAVE_BUTTON, self.gender_data, table_name)
        time.sleep(2)

        # Editing a table entry
        if len(data):
            buttons = self.get_column_action_buttons(*TrackerGenderLocators.EDIT_BUTTON)
            for i in range(len(data)):
                if data[i] == self.gender_data['search_data']:
                    buttons[i].click()
                    time.sleep(3)
                    self.add_edit_catalog_data(*TrackerGenderLocators.SAVE_BUTTON, self.gender_data, table_name)
                    print('Entry was edited!')
                    time.sleep(4)
                    break
                else:
                    print('Nothing was edited!!!')
            time.sleep(2)
            print('BUTTONS LENGTH: ', len(buttons))
