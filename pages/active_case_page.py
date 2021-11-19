import time

from .base_page import BasePage
from ..locators.active_case_locators import ActiveCaseLocators
from ..variables.active_case_variables import ActiveCaseVariables


class ActiveCasePage(BasePage):

    def edit_plaintiff_person_form(self):
        self.click_button(*ActiveCaseLocators.PLAINTIFF_BLOCK, 'PLAINTIFF BLOCK OPEN')
        time.sleep(3)
        self.click_button(*ActiveCaseLocators.PLAINTIFF_EDIT_BUTTON, 'PLAINTIFF PERSON EDIT')
        self.fill_in_edit_person_form(ActiveCaseVariables.plaintiff_person)
        self.click_button(*ActiveCaseLocators.SAVE_BUTTON, 'PLAINTIFF SAVE BUTTON')