import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

from ..locators.new_case_locators import NewCaseLocators


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def click_button(self, how, what, btn):
        if self.is_element_present(how, what):
            button = self.browser.find_element(how, what)
            button.click()
            print(f'{btn} - button was pressed...')
        else:
            print(f'{btn} button is not visible!!!')

    def fill_in_edit_person_form(self, person_info):
        try:
            # Main info fields
            surname = self.browser.find_element(*NewCaseLocators.SURNAME)
            time.sleep(3)
            surname.send_keys(Keys.CONTROL, "a")
            surname.send_keys(person_info['MainInfo']['surname'])
            firstname = self.browser.find_element(*NewCaseLocators.FIRSTNAME)
            time.sleep(3)
            firstname.send_keys(Keys.CONTROL, "a")
            firstname.send_keys(person_info['MainInfo']['firstname'])
            dob = self.browser.find_element(*NewCaseLocators.DATE_OF_BIRTH)
            time.sleep(3)
            dob.send_keys(Keys.CONTROL, "a")
            dob.send_keys(person_info['MainInfo']['dob'])
            gender = self.browser.find_element(*NewCaseLocators.GENDER)
            time.sleep(3)
            gender.send_keys(Keys.CONTROL, "a")
            gender.send_keys(person_info['MainInfo']['gender'])
            pin = self.browser.find_element(*NewCaseLocators.PIN)
            time.sleep(3)
            pin.send_keys(Keys.CONTROL, "a")
            pin.send_keys(person_info['MainInfo']['pin'])

            # Passport info fields
            p_number = self.browser.find_element(*NewCaseLocators.PASSPORT_NUMBER)
            time.sleep(1)
            p_number.send_keys(Keys.CONTROL, "a")
            p_number.send_keys(person_info['PassportInfo']['number'])
            p_issue = self.browser.find_element(*NewCaseLocators.PASSPORT_DATE_ISSUE)
            time.sleep(1)
            p_issue.send_keys(Keys.CONTROL, "a")
            p_issue.send_keys(person_info['PassportInfo']['issue'])
            p_expire = self.browser.find_element(*NewCaseLocators.PASSPORT_EXPIRE_DATE)
            time.sleep(1)
            p_expire.send_keys(Keys.CONTROL, "a")
            p_expire.send_keys(person_info['PassportInfo']['expire'])
            p_authority = self.browser.find_element(*NewCaseLocators.PASSPORT_AUTHORITY)
            time.sleep(1)
            p_authority.send_keys(Keys.CONTROL, "a")
            p_authority.send_keys(person_info['PassportInfo']['authority'])
        except NoSuchElementException:
            print('Some elements are not visible!!!')
