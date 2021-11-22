import time

from ..pages.base_page import BasePage
from ..pages.base_page import is_element_equal
from selenium.webdriver.support.color import Color


class TextBox(BasePage):
    def check_text_box_visibility(self, how, what, text_field_name):
        if self.is_element_present(how, what):
            print(f'{text_field_name} - field is visible!!!')
        else:
            print(f'{text_field_name} field is not visible!!!')

    def send_text(self, how, what, text, text_field_name):
        if self.is_element_present(how, what):
            text_field = self.browser.find_element(how, what)
            time.sleep(3)
            text_field.send_keys(text)
            print(f'{text_field_name} - field has got --- {text} --- as a value...')
        else:
            print(f'{text_field_name} - field is not visible...')

    def check_text(self, how, what, text_field_name):
        if self.is_element_present(how, what):
            text_field = self.browser.find_element(how, what)
            time.sleep(3)
            text_field_value = text_field.get_attribute('value')
            if len(text_field_value):
                print(f'{text_field_name} - field contains --- {text_field_value} --- ...')
            else:
                print(f'{text_field_name} - field is empty...')
        else:
            print(f'{text_field_name} - field is not visible...')

    def check_error_msg(self, how, what, text_name, msg):
        if self.is_element_present(how, what):
            text_field = self.browser.find_element(how, what).text
            print(f'{text_name} - field\'s error message - {text_field}')
            if is_element_equal(text_field, msg):
                print(f'{text_name} - field\'s error message is CORRECT!')
            else:
                print(f'{text_name} - field\'s error message is INCORRECT!')

    def check_color_of_text_box(self, how, what, textbox_name, color):
        if self.is_element_present(how, what):
            text_field_color = self.browser.find_element(how, what).value_of_css_property('color')
            color_hex = Color.from_string(text_field_color).hex
            print(f'{textbox_name} - text box\'s color is - {color_hex}...')
            if is_element_equal(color_hex, color):
                print(f'Color of {textbox_name} text field is CORRECT.')
            else:
                print(f'!!!!! Color of {textbox_name} text field is INCORRECT.')