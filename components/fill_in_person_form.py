import time

from ..base.base import Base
from ..locators.new_case_locators import NewCaseLocators
from selenium.common.exceptions import NoSuchElementException


class FillInPersonForm(Base):

    def fill_in_person_form(self, person_info):
        try:
            # Main info fields
            surname = self.browser.find_element(*NewCaseLocators.SURNAME)
            time.sleep(3)
            surname.send_keys(person_info['MainInfo']['surname'])
            firstname = self.browser.find_element(*NewCaseLocators.FIRSTNAME)
            time.sleep(3)
            firstname.send_keys(person_info['MainInfo']['firstname'])
            dob = self.browser.find_element(*NewCaseLocators.DATE_OF_BIRTH)
            time.sleep(3)
            dob.send_keys(person_info['MainInfo']['dob'])
            gender = self.browser.find_element(*NewCaseLocators.GENDER)
            time.sleep(3)
            gender.send_keys(person_info['MainInfo']['gender'])
            pin = self.browser.find_element(*NewCaseLocators.PIN)
            time.sleep(3)
            pin.send_keys(person_info['MainInfo']['pin'])

            # Passport info fields
            p_numbers = self.browser.find_element(*NewCaseLocators.PASSPORT_NUMBER)
            p_numbers.send_keys(person_info['PassportInfo']['number'])
            p_issue = self.browser.find_element(*NewCaseLocators.PASSPORT_DATE_ISSUE)
            p_issue.send_keys(person_info['PassportInfo']['issue'])
            p_expire = self.browser.find_element(*NewCaseLocators.PASSPORT_EXPIRE_DATE)
            p_expire.send_keys(person_info['Passport']['expire'])
            p_authority = self.browser.find_element(*NewCaseLocators.PASSPORT_AUTHORITY)
            p_authority.send_keys(person_info['PassportInfo']['authority'])
        except NoSuchElementException:
            print('Some elements are not visible!!!')