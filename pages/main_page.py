from ..locators.main_page_locators import MainPageLocators
from ..variables.main_page_variables import MainPageVariables

from ..components.button import Button
from ..components.text_box import TextBox


class MainPage(Button, TextBox):
    def test_log_in_system(self):
        username = self.browser.find_element(*MainPageLocators.USERNAME)
        username.send_keys(*MainPageVariables.username)
        password = self.browser.find_element(*MainPageLocators.PASSWORD)
        password.send_keys(*MainPageVariables.password)
        self.click_button(*MainPageLocators.LOGIN_BUTTON, 'LOGIN BUTTON')

    def test_login_button_visibility(self):
        self.check_button_visibility(*MainPageLocators.LOGIN_BUTTON)

    def test_login_button_caption(self):
        self.check_button_caption(*MainPageLocators.LOGIN_BUTTON, 'LOGIN BUTTON', 'SIGN IN')

    def test_login_button_color(self):
        self.check_button_color(*MainPageLocators.LOGIN_BUTTON, 'LOGIN BUTTON', '#3f51b5')

    def test_username_field_visibility(self):
        self.check_textbox_visibility(*MainPageLocators.USERNAME)

    def test_username_sent_text(self):
        self.set_textbox_value(*MainPageLocators.USERNAME, '', 'USERNAME')
        # self.send_text(*MainPageLocators.USERNAME, 'altynbekova@arbitricaccikr.com', 'USERNAME')
        self.set_textbox_value(*MainPageLocators.PASSWORD, '1111', 'PASSWORD')

    def test_username_check_text(self):
        self.check_textbox_value(*MainPageLocators.USERNAME, 'altynbekova', 'USERNAME')

    def test_username_check_text_box_color(self):
        self.check_textbox_color_of_element(*MainPageLocators.USERNAME_FIELD, 'USERNAME', ' ')

    def test_username_check_error_msg(self):
        self.check_textbox_error_msg(*MainPageLocators.USERNAME_ERROR_MSG, 'USERNAME', 'E-mail address is required')