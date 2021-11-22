from ..locators.main_page_locators import MainPageLocators
from ..variables.main_page_variables import MainPageVariables

from ..components.buttons import Buttons
from ..components.text_box import TextBox


class MainPage(Buttons, TextBox):
    def test_log_in_system(self):
        username = self.browser.find_element(*MainPageLocators.USERNAME)
        username.send_keys(*MainPageVariables.username)
        password = self.browser.find_element(*MainPageLocators.PASSWORD)
        password.send_keys(*MainPageVariables.password)
        self.click_button(*MainPageLocators.LOGIN_BUTTON, 'LOGIN BUTTON')

    def test_login_button_visibility(self):
        self.check_button_visibility(*MainPageLocators.LOGIN_BUTTON, 'LOGIN BUTTON')

    def test_login_button_caption(self):
        self.check_button_caption(*MainPageLocators.LOGIN_BUTTON, 'LOGIN BUTTON', 'SIGN IN')

    def test_login_button_color(self):
        self.check_button_color(*MainPageLocators.LOGIN_BUTTON, 'LOGIN BUTTON')

    def test_username_field_visibility(self):
        self.check_text_box_visibility(*MainPageLocators.USERNAME, 'USERNAME FIELD')

    def test_username_sent_text(self):
        self.send_text(*MainPageLocators.USERNAME, '', 'USERNAME')
        # self.send_text(*MainPageLocators.USERNAME, 'altynbekova@arbitricaccikr.com', 'USERNAME')
        self.send_text(*MainPageLocators.PASSWORD, '1111', 'PASSWORD')

    def test_username_check_text(self):
        self.check_text(*MainPageLocators.USERNAME, 'USERNAME')

    def test_username_check_text_box_color(self):
        self.check_color_of_text_box(*MainPageLocators.USERNAME_FIELD, 'USERNAME', ' ')

    def test_username_check_error_msg(self):
        self.check_error_msg(*MainPageLocators.USERNAME_ERROR_MSG, 'USERNAME', 'E-mail addess is required')