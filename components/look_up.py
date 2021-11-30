import time

from selenium.webdriver.support.color import Color
from selenium.webdriver.support.select import Select

from ..base.base import Base
from ..base.base import is_element_equal


class LookUp(Base):
    def check_lookup_visibility(self, how, what):
        return self.is_element_present(how, what)

    def open_close_look_up(self, how, what, element):
        if self.is_element_present(how, what):
            look_up = self.browser.find_element(how, what)
            look_up.click()
            time.sleep(1)
            print(f'{element} - look up element was pressed...')
        else:
            print(f'{element} look up element is not visible!!!')

    def check_lookup_exists_value(self, how, what, value, element):
        if self.is_element_present(how, what):
            select = Select(self.browser.find_element(how, what))
            options = select.options
            for index in range(0, len(options)):
                if options[index].text == value:
                    return True
            return False
        else:
            print(f'{element} look up element is not visible!!!')

    def select_lookup_element(self, how, what, value, element):
        if self.is_element_present(how, what):
            select = Select(self.browser.find_element(how, what))
            time.sleep(2)
            select.select_by_visible_text(value)
            time.sleep(1)
        else:
            print(f'{element} look up element is not visible!!!')

    def lookup_select_empty_element(self, how, what, value, element):
        if self.is_element_present(how, what):
            select = Select(self.browser.find_element(how, what))
            time.sleep(2)
            select.select_by_value(value)
            time.sleep(1)
        else:
            print(f'{element} look up element is not visible!!!')

    def check_lookup_error_msg(self, how, what, msg, element):
        if self.is_element_present(how, what):
            error_text = self.browser.find_element(how, what).text
            return is_element_equal(error_text, msg)
        else:
            print(f'{element} look up error message is not visible!!!')

    def check_lookup_color_of_element(self, how, what, color, element):
        if self.is_element_present(how, what):
            lookup_color = self.browser.find_element(how, what).value_of_css_property('color')
            color_hex = Color.from_string(lookup_color).hex
            return is_element_equal(color_hex, color)
        else:
            print(f'{element} look up element is not visible!!!')

    def clear_lookup_selected_value(self, how, what, value, element):
        if self.is_element_present(how, what):
            select = self.browser.find_element(how, what)
            select.send_keys(value)
        else:
            print(f'{element} look up element is not visible!!!')