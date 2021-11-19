from ..locators.main_page_locators import MainPageLocators
from ..variables.main_page_variables import MainPageVariables

from .base_page import BasePage


class MainPage(BasePage):
    def test_log_in_system(self):
        username = self.browser.find_element(*MainPageLocators.USERNAME)
        username.send_keys(*MainPageVariables.username)
        password = self.browser.find_element(*MainPageLocators.PASSWORD)
        password.send_keys(*MainPageVariables.password)
        self.click_button(*MainPageLocators.LOGIN_BUTTON, 'LOGIN BUTTON')