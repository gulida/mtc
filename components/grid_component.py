import time

from ..components.text_box import TextBox
from ..components.button import Button
from ..base.base import form_inputs


class GridComponent(TextBox, Button):

    def search_from_table(self, how, what, elements_how, elements_what, value, table_name):
        found_data_array = []
        if self.is_element_present(how, what):
            self.set_textbox_value(how, what, value, table_name)
            found_data = self.browser.find_elements(elements_how, elements_what)
            for data in found_data:
                found_data_array.append(data.text)
            return found_data_array
        else:
            print(f'Search field of {table_name} frame is not visible...')

    def get_table_name(self, how, what, table_name):
        if self.is_element_present(how, what):
            return self.browser.find_element(how, what).text
        else:
            print(f'Can not find name of {table_name} table')

    def get_table_column_titles(self, how, what):
        column_titles = []
        table_columns = self.browser.find_elements(how, what)
        for e in table_columns:
            column_titles.append(e.text)
        return column_titles

    def add_edit_catalog_data(self, how, what, data, element):
        keys = data.keys()
        for key in keys:
            self.set_textbox_value(*form_inputs(key), data[key], element + '_' + str(key))
        time.sleep(2)
        self.click_button(how, what, element)

    def get_column_data(self, how, what):
        data = []
        found_data = self.browser.find_elements(how, what)
        for e in found_data:
            data.append(e.text)
        return data

    def get_column_action_buttons(self, how, what):
        buttons = []
        found_buttons = self.browser.find_elements(how, what)
        for e in found_buttons:
            buttons.append(e)
        return buttons
