from ..locators.tracker_user_locators import TrackerUserPageLocators

from ..components.button import Button


class TrackerUserPage(Button):
    def test_open_file_type_table(self):
        self.click_button(*TrackerUserPageLocators.FILE_TYPE, 'MENU FILE TYPE')