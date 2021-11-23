import time

from ..locators.user_cabinet_locators import UserCabinetLocators

from ..components.buttons import Buttons
from ..components.text_box import TextBox
from ..components.check_box import CheckBox
from ..components.look_up import LookUp


class UserCabinetPage(Buttons, TextBox, CheckBox, LookUp):
    def test_open_user_cabinet(self):
        self.click_button(*UserCabinetLocators.TAB_MENU_CABINET, 'TAB MENU CABINET')
        time.sleep(5)
        self.click_button(*UserCabinetLocators.SIDE_MENU_USER_CABINET, 'SIDE MENU USER CABINET')

    def test_pin_check_color_of_text_box(self):
        self.check_textbox_color_of_element(*UserCabinetLocators.PIN_FIELD, 'PIN', '#f44336')

    def test_passport_terms(self):
        if self.check_checkbox_state(*UserCabinetLocators.PASSPORT_TERM_CHECKBOX, 'PASSPORT TERMS'):
            print('Do not consider passport terms!')
        else:
            print('Consider passport terms!')
        if self.check_checkbox_label(*UserCabinetLocators.PASSPORT_TERM_CHECKBOX_LABEL, 'PASSPORT TERMS',
                                     'Don\'t consider passport ter'):
            print('Correct!!!')
        else:
            print('INCORRECT!!!')

    def date_issue_click(self):
        self.click_button(*UserCabinetLocators.DATE_ISSUE, 'DATE ISSUE')

    def test_gender(self):
        if self.check_lookup_visibility(*UserCabinetLocators.GENDER):
            print('Visibility - OK')
        else:
            print('Visibility - NOT')
        time.sleep(1)
        if self.check_lookup_exists_value(*UserCabinetLocators.GENDER, 'Мужской', 'GENDER'):
            print('Value - OK')
        else:
            print('Value - NOT')
            time.sleep(1)
        time.sleep(1)
        self.open_close_look_up(*UserCabinetLocators.GENDER, 'GENDER')
        time.sleep(1)
        self.lookup_select_empty_element(*UserCabinetLocators.GENDER, '0', 'GENDER')
        time.sleep(1)
        if self.check_lookup_error_msg(*UserCabinetLocators.GENDER, '', 'GENDER'):
            print('Error msg - OK')
        else:
            print('Error msg - NOT')

        self.open_close_look_up(*UserCabinetLocators.GENDER, 'GENDER')

