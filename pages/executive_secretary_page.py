from selenium.webdriver.common.by import By

from ..locators.executive_secretary_locators import ExecutiveSecretaryLocators
from .base_page import BasePage


class ExecutiveSecretaryPage(BasePage):
    def open_new_case_add_steps(self):
        if self.is_element_present(*ExecutiveSecretaryLocators.MENU_CLAIM):
            menu_link = self.browser.find_element(*ExecutiveSecretaryLocators.MENU_CLAIM)
            menu_link.click()
            if self.is_element_present(*ExecutiveSecretaryLocators.NEW_CLAIM_LINK):
                new_claim_link = self.browser.find_element(*ExecutiveSecretaryLocators.NEW_CLAIM_LINK)
                new_claim_link.click()
                print('You can continue your test..')
            else:
                print('There is no NEW CLAIM LINK ...')
        else:
            print('You can not continue your test...')

    def open_active_cases_list(self):
        if self.is_element_present(*ExecutiveSecretaryLocators.MENU_CASES):
            cases_link = self.browser.find_element(*ExecutiveSecretaryLocators.MENU_CASES)
            cases_link.click()
            if self.is_element_present(*ExecutiveSecretaryLocators.ACTIVE_CASES_LINK):
                active_cases = self.browser.find_element(*ExecutiveSecretaryLocators.ACTIVE_CASES_LINK)
                active_cases.click()
                print('You can continue your test with active cases...')
            else:
                print('There is NO ACTIVE CASES link...')
        else:
            print('You can not continue your test... You do not have access to active cases!')

    def open_active_case(self):
        self.click_button(*ExecutiveSecretaryLocators.FIRST_CASE_EDIT_BTN, 'FIRST ACTIVE CASE EDIT')