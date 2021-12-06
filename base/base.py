import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ..locators.new_case_locators import NewCaseLocators


def is_element_equal(element, equal_to):
    if element == equal_to:
        return True
    else:
        return False


def form_inputs(input_name):
    return (By.ID, input_name)


def is_linking_element_present(linking_element, how, what):
    try:
        linking_element.find_element(how, what)
    except NoSuchElementException:
        return False
    return True


def linking_element(how, what, element):
    if is_linking_element_present(element, how, what):
        return element.find_element(how, what)
    else:
        print(f'{element} - linking element is not visible!')


class Base():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.wait = WebDriverWait(browser, timeout)
        # self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    # Forms
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
            time.sleep(5)

            gender = Select(self.browser.find_element(*NewCaseLocators.GENDER))
            options = gender.options
            for index in range(0, len(options)):
                print('ALL OPTIONS: ', options[index].text)
            # print('ALL OPTIONS: ', gender.options)
            # select by visible text
            gender.select_by_visible_text(person_info['MainInfo']['gender'])
            time.sleep(5)
            # gender = self.browser.find_element(*NewCaseLocators.GENDER)
            # time.sleep(3)
            # gender.send_keys(Keys.CONTROL, "a")
            # gender.send_keys(person_info['MainInfo']['gender'])
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
