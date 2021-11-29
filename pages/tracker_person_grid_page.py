import time

from ..locators.tracker_person_grid_locators import TrackerPersonLocators
from ..variables.tracker_person_grid_variables import TrackerPersonVariables

from ..components.grid_component import GridComponent
from ..components.card import Card
from ..components.date_type import DateType


class TrackerPersonPage(GridComponent, Card, DateType):
    table = 'OF Person TABLE'
    table_name = 'NO NAME'

    search_data = TrackerPersonVariables.person_data['search_data']

    def test_person_table(self):
        self.click_button(*TrackerPersonLocators.SEARCH_BUTTON, f'SEARCH BUTTON {self.table}')
        time.sleep(2)

        data = self.search_from_table(*TrackerPersonLocators.SEARCH_INPUT, *TrackerPersonLocators.TABLE_DATA_NAME,
                                      self.search_data, 'PERSON')
        print('FOUND DATA IN NAME COLUMN: ', data)

        table_name = self.get_table_name(*TrackerPersonLocators.TABLE_NAME, 'PERSON')
        if len(data):
            buttons = self.get_column_action_buttons(*TrackerPersonLocators.EDIT_BUTTON)
            for i in range(len(data)):
                print('IN FOR')
                if data[i] == self.search_data:
                    print('IN IF')
                    buttons[i].click()
                    time.sleep(3)
                    break
        print('TABLE NAME: ', table_name)

        cards = self.get_all_cards_in_container(*TrackerPersonLocators.JOB_HISTORY_CARD_NAME, 'JOB HISTORY')
        card_titles = self.get_all_card_titles(*TrackerPersonLocators.JOB_HISTORY_CARD_TITLE, 'JOB HISTORY')
        print('CARDS: ', cards)
        print('CARD TITLES: ', card_titles)

        self.click_button(*TrackerPersonLocators.JOB_HISTORY_CARD_EDIT_BTN, 'CARD EDIT')
        time.sleep(2)

        # Job history form
        # print('CHECK: ',self.check_date_field_value(*TrackerPersonLocators.JOB_HISTORY_DATE_START, '2021-11-21', 'DATE START'))
        self.set_date_field_value(*TrackerPersonLocators.JOB_HISTORY_DATE_START, '00-00-0000', 'DATE START')
        time.sleep(2)
        print('DATE START: ', self.get_date_type_error_msg(*TrackerPersonLocators.JOB_HISTORY_DATE_START, 'DATE START'))
        time.sleep(2)
        self.click_button(*TrackerPersonLocators.JOB_HISTORY_CANCEL_BUTTON, 'JOB HISTORY CANCEL')
        # self.click_button(*TrackerPersonLocators.JOB_HISTORY_SAVE_BUTTON, 'JOB HISTORY SAVE')
        time.sleep(4)