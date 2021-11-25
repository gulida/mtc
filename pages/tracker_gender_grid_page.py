import time

from ..base.base import form_inputs
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

        self.click_button(*TrackerGenderLocators.ADD_BUTTON, 'GENDER ADD BUTTON')
        time.sleep(3)

        self.add_edit_catalog_data(*TrackerGenderLocators.SAVE_BUTTON, self.gender_data, table_name)

        time.sleep(5)
