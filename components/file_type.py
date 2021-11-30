import os
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from ..base.base import Base, linking_element
from ..base.base import is_element_equal
from ..base.base import is_linking_element_present
from selenium.webdriver.support.color import Color


class FileType(Base):

    def check_file_type_visibility(self, how, what):
        return self.is_element_present(how, what)

    def set_file_type_value(self, how, what, file_path, element):
        file = os.path.join(file_path)
        if self.is_element_present(how, what):
            file_field = self.browser.find_element(how, what)
            time.sleep(1)
            file_field.send_keys(file)
        else:
            print(f'{element} - field is not visible...')

    # Error message functions
    def file_field(self, how, what, element):
        if self.is_element_present(how, what):
            return self.browser.find_element(how, what)
        else:
            print(f'{element} - is not visible')

    def check_file_error_msg(self, how, what, msg, element):
        if self.is_element_present(how, what):
            file_element = self.file_field(how, what, element)
            print('FILE ELEMENT: ', file_element)
            parent_element = linking_element(By.XPATH, '../..', file_element)
            print('PARENT ELEMENT: ', parent_element)
            if is_linking_element_present(parent_element, By.TAG_NAME, 'p'):
                error_msg = self.browser.find_element(By.TAG_NAME, 'p').text
                return is_element_equal(error_msg, msg)
        else:
            print(f'{element} - field is not visible...')

    def get_file_error_msg(self, how, what, element):
        if self.is_element_present(how, what):
            file_element = self.file_field(how, what, element)
            parent_element = linking_element(By.XPATH, '../..', file_element)
            if is_linking_element_present(parent_element, By.TAG_NAME, 'p'):
                return parent_element.find_element(By.TAG_NAME, 'p').text
            else:
                print('Could not find ERROR MSG!!!')
        else:
            print(f'{element} - field is not visible...')

