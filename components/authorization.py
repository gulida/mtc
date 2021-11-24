from .button import Button
from .text_box import TextBox

from ..locators.tracker_auth_page_locators import TrackerAuthPageLocators


class AuthReg(Button, TextBox):

    def fill_in_auth_form(self, auth_info):
        self.set_textbox_value(*TrackerAuthPageLocators.EMAIL, auth_info['email'], 'EMAIL')
        self.set_textbox_value(*TrackerAuthPageLocators.PASSWORD, auth_info['password'], 'PASSWORD')
        self.click_button(*TrackerAuthPageLocators.SIGN_IN_BUTTON, 'SIGN IN')
