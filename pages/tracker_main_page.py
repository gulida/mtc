from ..locators.tracker_main_page_locators import TrackerMainPageLocators
from ..variables.tracker_auth_page_variables import TrackerAuthPageVariables

from ..components.authorization import AuthReg


class TrackerMainPage(AuthReg):

    def test_authorization(self):
        self.fill_in_auth_form(TrackerAuthPageVariables.auth_info)

    def test_open_user_page(self):
        self.click_button(*TrackerMainPageLocators.LOGO, 'LOGO')