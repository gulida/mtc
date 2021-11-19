import time

from .base_page import BasePage
from ..locators.new_case_locators import NewCaseLocators
from ..variables.new_case_variables import NewCaseVariables


class NewCasePage(BasePage):

    def fill_in_plaintiff_person_form(self):
        self.click_button(*NewCaseLocators.PLAINTIFF_ADD_PERSON, 'ADD PERSON')
        time.sleep(10)
        self.fill_in_edit_person_form(NewCaseVariables.plaintiff_person)
        self.click_button(*NewCaseLocators.SAVE_BUTTON, 'PLAINTIFF SAVE BUTTON')