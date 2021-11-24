import time

from ..locators.tracker_gender_grid_locators import TrackerGenderLocators

from ..components.button import Button
from ..components.text_box import TextBox


class TrackerGenderPage(Button, TextBox):
    table = 'OF SEX TABLE'

    def test_gender_table(self, value):
        self.click_button(*TrackerGenderLocators.SEARCH_BUTTON, f'SEARCH BUTTON {self.table}')
        time.sleep(2)
        self.set_textbox_value(*TrackerGenderLocators.SEARCH_INPUT, value, f'SEARCH INPUT {self.table}')
        time.sleep(2)

        columns = []

        # TABLE NAME
        if self.is_element_present(*TrackerGenderLocators.TABLE_NAME):
            table_name = self.browser.find_element(*TrackerGenderLocators.TABLE_NAME).text
            print('Table name: ', table_name)
        else:
            print('Can not find table name')

        # TABLE COLUMN TITLES
        table_columns = self.browser.find_elements(*TrackerGenderLocators.TABLE_HEAD_TITLES)
        column_count = len(table_columns)

        for e in table_columns:
            columns.append(e.text)

        print('Column count: ', column_count)
        print('Columns: ', columns)

        # TABLE DATA
        names_data = []
        table_data_name = self.browser.find_elements(*TrackerGenderLocators.TABLE_DATA_NAME)
        data_count = len(table_data_name)

        for data in table_data_name:
            names_data.append(data.text)

        print('NAMES: ', names_data)
        print('NAMES COUNT: ', data_count)

        if data_count:
            print('This value already exists!!!')
        else:
            print('You can add this value in the table!!!')

        # if names_data.count(value) == 0:
        #     print('You can add this value in the table!!!')
        # else:
        #     print('This value already exists!!!')