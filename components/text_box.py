import time

from ..pages.base_page import BasePage
from ..pages.base_page import is_element_equal
from selenium.webdriver.support.color import Color


class TextBox(BasePage):
    def check_textbox_visibility(self, how, what):
        if self.is_element_present(how, what):
            return True
        else:
            return False

    def set_textbox_value(self, how, what, text, element):
        if self.is_element_present(how, what):
            text_field = self.browser.find_element(how, what)
            time.sleep(3)
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

    def check_textbox_error_msg(self, how, what, msg, element):
        if self.is_element_present(how, what):
            text_element = self.browser.find_element(how, what).text
            return is_element_equal(text_element, msg)
        else:
            print(f'{element} - field is not visible...')

    def check_textbox_color_of_element(self, how, what, color, element):
        if self.is_element_present(how, what):
            text_field_color = self.browser.find_element(how, what).value_of_css_property('color')
            color_hex = Color.from_string(text_field_color).hex
            return is_element_equal(color_hex, color)
        else:
            print(f'{element} - field is not visible...')