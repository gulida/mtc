import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from ..base.base import Base, linking_element
from ..base.base import is_element_equal
from ..base.base import is_linking_element_present
from selenium.webdriver.support.color import Color


# def linking_element(how, what, element):
#     if is_linking_element_present(element, how, what):
#         return element.find_element(how, what)
#     else:
#         print(f'{element} - linking element is not visible!')


class TextBox(Base):
    def check_textbox_visibility(self, how, what):
        return self.is_element_present(how, what)

    def set_textbox_value(self, how, what, text, element):
        if self.is_element_present(how, what):
            text_field = self.browser.find_element(how, what)
            time.sleep(2)
            text_field.send_keys(Keys.CONTROL, "a")
            time.sleep(1)
            text_field.send_keys(text)
        else:
            print(f'{element} - field is not visible...')

    def check_textbox_value(self, how, what, value, element):
        if self.is_element_present(how, what):
            text_field = self.browser.find_element(how, what)
            time.sleep(3)
            text_field_value = text_field.get_attribute('value')
            return is_element_equal(text_field_value, value)
        else:
            print(f'{element} - field is not visible...')

    def check_textbox_color_of_element(self, how, what, color, element):
        if self.is_element_present(how, what):
            text_field_color = self.browser.find_element(how, what).value_of_css_property('color')
            color_hex = Color.from_string(text_field_color).hex
            return is_element_equal(color_hex, color)
        else:
            print(f'{element} - field is not visible...')

    # Error message functions
    def textbox_field(self, how, what, element):
        if self.is_element_present(how, what):
            return self.browser.find_element(how, what)
        else:
            print(f'{element} - is not visible')

    def check_textbox_error_msg(self, how, what, msg, element):
        if self.is_element_present(how, what):
            text_element = self.textbox_field(how, what, element)
            print('TEXT_ELEMENT: ', text_element)
            parent_element = linking_element(By.XPATH, '../..', text_element)
            print('PARENT_ELEMENT: ', parent_element)
            if is_linking_element_present(parent_element, By.TAG_NAME, 'p'):
                error_msg = self.browser.find_element(By.TAG_NAME, 'p').text
                return is_element_equal(error_msg, msg)
        else:
            print(f'{element} - field is not visible...')

    def get_textbox_error_msg(self, how, what, element):
        if self.is_element_present(how, what):
            text_element = self.textbox_field(how, what, element)
            parent_element = linking_element(By.XPATH, '../..', text_element)
            if is_linking_element_present(parent_element, By.TAG_NAME, 'p'):
                return parent_element.find_element(By.TAG_NAME, 'p').text
            else:
                print('Could not find ERROR MSG!!!')
        else:
            print(f'{element} - field is not visible...')
