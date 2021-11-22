import time

from ..locators.user_cabinet_locators import UserCabinetLocators

from ..components.buttons import Buttons
from ..components.text_box import TextBox
from ..components.check_box import CheckBox


class UserCabinetPage(Buttons, TextBox, CheckBox):
    def test_open_user_cabinet(self):
        self.click_button(*UserCabinetLocators.TAB_MENU_CABINET, 'TAB MENU CABINET')
        time.sleep(5)
        self.click_button(*UserCabinetLocators.SIDE_MENU_USER_CABINET, 'SIDE MENU USER CABINET')

    def test_pin_check_color_of_text_box(self):
        self.check_color_of_text_box(*UserCabinetLocators.PIN_FIELD, 'PIN', '#f44336')

    def test_passport_terms(self):
        if self.check_checkbox_state(*UserCabinetLocators.PASSPORT_TERM_CHECKBOX, 'PASSPORT TERMS'):
            print('Do not consider passport terms!')
        else:
            print('Consider passport terms!')
        if self.check_checkbox_label(*UserCabinetLocators.PASSPORT_TERM_CHECKBOX_LABEL, 'PASSPORT TERMS', 'Don\'t consider passport ter'):
            print('Correct!!!')
        else:
            print('INCORRECT!!!')

    def date_issue_click(self):
        self.click_button(*UserCabinetLocators.DATE_ISSUE, 'DATE ISSUE')