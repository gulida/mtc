import time

from ..locators.tracker_person_grid_locators import TrackerPersonLocators
from ..variables.tracker_person_grid_variables import TrackerPersonVariables

from ..components.grid_component import GridComponent
from ..components.card import Card, press_card_edit_button
from ..components.date_type import DateType
from ..components.look_up import LookUp
from ..components.file_type import FileType


class TrackerPersonPage(GridComponent, Card, DateType, LookUp, FileType):
    table_name = 'PERSON'

    search_data = TrackerPersonVariables.person_data['search_data']

    def test_person_table(self):
        table_name = self.get_table_name(*TrackerPersonLocators.TABLE_NAME, self.table_name)
        data = self.search_from_table(*TrackerPersonLocators.SEARCH_BUTTON,
                                      *TrackerPersonLocators.SEARCH_INPUT,
                                      *TrackerPersonLocators.LAST_NAME,
                                      self.search_data, table_name)

        search_data = self.search_from_table_for_edit_delete(*TrackerPersonLocators.SEARCH_BUTTON,
                                                             *TrackerPersonLocators.SEARCH_INPUT,
                                                             *TrackerPersonLocators.LAST_NAME,
                                                             *TrackerPersonLocators.EDIT_BUTTON,
                                                             *TrackerPersonLocators.DELETE_BUTTON,
                                                             self.search_data, table_name)

        time.sleep(3)
        self.press_edit_button_of_table_entry(data, search_data, self.search_data, table_name)

        time.sleep(4)

        card_titles = self.get_all_card_titles(*TrackerPersonLocators.JOB_HISTORY_CARD_TITLE, 'JOB History')
        print('Titles: ', card_titles)

        collection = self.get_base_card_collection_with_title_edit_delete(*TrackerPersonLocators.JOB_HISTORY_CARD_NAME,
                                                                          *TrackerPersonLocators.JOB_HISTORY_CARD_TITLE,
                                                                          *TrackerPersonLocators.JOB_HISTORY_CARD_EDIT_BTN,
                                                                          *TrackerPersonLocators.JOB_HISTORY_CARD_DELETE_BTN,
                                                                          'Job history')
        print('COLLECTION: ', collection)
        press_card_edit_button(collection, 'Junior')
        time.sleep(3)
        # Job history form
        self.set_date_field_value(*TrackerPersonLocators.JOB_HISTORY_DATE_START,
                                  TrackerPersonVariables.job_history_data['dateStart'],
                                  'Start')

        self.set_date_field_value(*TrackerPersonLocators.JOB_HISTORY_DATE_FINISH,
                                  TrackerPersonVariables.job_history_data['dateFinish'],
                                  'Finish')

        self.open_close_look_up(*TrackerPersonLocators.JOB_HISTORY_POSITION, 'Position')
        self.select_lookup_element(*TrackerPersonLocators.JOB_HISTORY_POSITION, TrackerPersonVariables.job_history_data['idPost'], 'Position')
        self.open_close_look_up(*TrackerPersonLocators.JOB_HISTORY_POSITION, 'Position')

        self.set_file_type_value(*TrackerPersonLocators.JOB_HISTORY_DOCUMENT_FILE,
                                 TrackerPersonVariables.job_history_data['idDocumentNavigationName'],
                                 'file')

        self.set_textbox_value(*TrackerPersonLocators.JOB_HISTORY_DOCUMENT_DESCRIPTION,
                               TrackerPersonVariables.job_history_data['idDocumentNavdescription'],
                               'file description')

        self.open_close_look_up(*TrackerPersonLocators.JOB_HISTORY_DOCUMENT_FILE_TYPE,
                                  TrackerPersonVariables.job_history_data['idDocumentNavidFileType'])
        self.select_lookup_element(*TrackerPersonLocators.JOB_HISTORY_DOCUMENT_FILE_TYPE,
                                  TrackerPersonVariables.job_history_data['idDocumentNavidFileType'],
                                  'file type')
        self.open_close_look_up(*TrackerPersonLocators.JOB_HISTORY_DOCUMENT_FILE_TYPE,
                                TrackerPersonVariables.job_history_data['idDocumentNavidFileType'])

        time.sleep(2)
        self.click_button(*TrackerPersonLocators.JOB_HISTORY_SAVE_BUTTON, 'Job history save')
        time.sleep(5)
