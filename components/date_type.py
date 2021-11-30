import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color

from ..base.base import Base, is_element_equal, linking_element, is_linking_element_present


class DateType(Base):

    def check_visibility(self, how, what):
        return self.is_element_present(how, what)

    def set_date_field_value(self, how, what, date_data, element):
        if self.is_element_present(how, what):
            date_field = self.browser.find_element(how, what)
            time.sleep(2)
            date_field.send_keys(date_data) # date_data format: 'mm-dd-yyyy'
        else:
            print(f'{element} - field is not visible...')

    def check_date_field_value(self, how, what, value, element):
        if self.is_element_present(how, what):
            date_field = self.browser.find_element(how, what)
            time.sleep(2)
            date_field_value = date_field.get_attribute('value') # value format yyyy-mm-dd
            return is_element_equal(date_field_value, value)
        else:
            print(f'{element} - field is not visible...')

    def check_date_type_color_of_element(self, how, what, color, element):
        if self.is_element_present(how, what):
            date_field_color = self.browser.find_element(how, what).value_of_css_property('color')
            color_hex = Color.from_string(date_field_color).hex
            return is_element_equal(color_hex, color)
        else:
            print(f'{element} - field is not visible...')

    # Error message functions
    def date_type_field(self, how, what, element):
        if self.is_element_present(how, what):
            return self.browser.find_element(how, what)
        else:
            print(f'{element} - is not visible')

    def check_date_type_error_msg(self, how, what, msg, element):
        if self.is_element_present(how, what):
            date_element = self.date_type_field(how, what, element)
            print('TEXT_ELEMENT: ', date_element)
            parent_element = linking_element(By.XPATH, '../..', date_element)
            print('PARENT_ELEMENT: ', parent_element)
            if is_linking_element_present(parent_element, By.TAG_NAME, 'p'):
                error_msg = self.browser.find_element(By.TAG_NAME, 'p').text
                return is_element_equal(error_msg, msg)
        else:
            print(f'{element} - field is not visible...')

    def get_date_type_error_msg(self, how, what, element):
        if self.is_element_present(how, what):
            date_element = self.date_type_field(how, what, element)
            parent_element = linking_element(By.XPATH, '../..', date_element)
            if is_linking_element_present(parent_element, By.TAG_NAME, 'p'):
                return parent_element.find_element(By.TAG_NAME, 'p').text
            else:
                print('Could not find ERROR MSG!!!')
        else:
            print(f'{element} - field is not visible...')