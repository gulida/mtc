import time

from ..components.text_box import TextBox
from ..components.button import Button
from ..base.base import form_inputs
from ..locators.tracker_common_locators import TrackerCommonLocators


class GridComponent(TextBox, Button):

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

    def search_from_table(self, how_search_btn, what_search_btn,
                          how_search_input, what_search_input,
                          # how_input_close, what_input_close,
                          search_area_how, search_area_what,
                          search_data, table_name):
        found_data_array = []
        # Checking if search input field is available
        if self.is_element_present(how_search_input, what_search_input):
            # self.click_button(how_input_close, what_input_close, 'SEARCH INPUT CLOSE')
            self.set_textbox_value(how_search_input, what_search_input, search_data, table_name)
            next_arrow_flag = True
            time.sleep(3)
            while next_arrow_flag:
                found_data = self.browser.find_elements(search_area_how, search_area_what)
                for data in found_data:
                    found_data_array.append(data.text)
                next_button = self.browser.find_element(*TrackerCommonLocators.PAGINATION_NEXT_BUTTON)
                disabled_props = next_button.get_property('disabled')
                if not disabled_props:
                    next_button.click()
                    time.sleep(3)
                else:
                    next_arrow_flag = False
                print('IF NEXT BUTTON PROPS1: ', disabled_props)
            return found_data_array
        elif self.is_element_present(how_search_btn, what_search_btn):
            self.click_button(how_search_btn, what_search_btn, 'SEARCH BUTTON')
            time.sleep(2)
            if self.is_element_present(how_search_input, what_search_input):
                self.set_textbox_value(how_search_input, what_search_input, search_data, table_name)
                next_arrow_flag = True
                time.sleep(3)
                while next_arrow_flag:
                    found_data = self.browser.find_elements(search_area_how, search_area_what)
                    for data in found_data:
                        found_data_array.append(data.text)
                    next_button = self.browser.find_element(*TrackerCommonLocators.PAGINATION_NEXT_BUTTON)
                    disabled_props = next_button.get_property('disabled')
                    if not disabled_props:
                        next_button.click()
                        time.sleep(3)
                    else:
                        next_arrow_flag = False
                    print('ELIF NEXT BUTTON PROPS1: ', disabled_props)
                return found_data_array
            else:
                print(f'{table_name} table does not have SEARCH FIELD...')
        else:
            print(f'{table_name} table does not have SEARCH BUTTON...')

    # ADD & EDIT
    def add_edit_catalog_data(self, how, what, data, element):
        keys = data.keys()
        for key in keys:
            self.set_textbox_value(*form_inputs(key), data[key], element + '_' + str(key))
        time.sleep(2)
        self.click_button(how, what, element)

    def add_table_entry(self, column_data, how_add_btn, what_add_btn, new_entry_data, how_save_btn, what_save_btn,
                        table_name):
        add_flag = True
        if len(column_data):
            print('++++++++++')
            for i in range(len(column_data)):
                if column_data[i] == new_entry_data['search_data']:
                    print('This value is already exists in the table!!!')
                    add_flag = False
                    break
        if add_flag:
            print('$$$$$$$$$$$$$$$')
            self.click_button(how_add_btn, what_add_btn, f'{table_name} ADD BUTTON')
            time.sleep(3)
            self.add_edit_catalog_data(how_save_btn, what_save_btn, new_entry_data, table_name)
        print('OK')

    def edit_table_entry(self, column_data, how_edit_btn, what_edit_btn, correct_data, how_save_btn, what_save_btn,
                         table_name):
        if len(column_data):
            buttons = self.get_column_action_buttons(how_edit_btn, what_edit_btn)
            for i in range(len(column_data)):
                if column_data[i] == correct_data['search_data']:
                    buttons[i].click()
                    time.sleep(3)
                    self.add_edit_catalog_data(how_save_btn, what_save_btn, correct_data, table_name)
                    print(f'{table_name} table\'s entry was edited!')
                    time.sleep(1)
                    break
                else:
                    print('Nothing was edited!!!')
        else:
            print(f'{table_name} table does not have any entries to edit.')

    def delete_table_entry(self, column_data, how_del_btn, what_del_btn, search_data, how_alert_ok_btn,
                           what_alert_ok_btn, table_name):
        if len(column_data):
            buttons = self.get_column_action_buttons(how_del_btn, what_del_btn)
            for i in range(len(column_data)):
                if column_data[i] == search_data:
                    buttons[i].click()
                    time.sleep(3)
                    self.click_button(how_alert_ok_btn, what_alert_ok_btn, 'CONFIRM DELETE')
                    print('Entry was deleted')
                    break
                else:
                    print('Nothing was deleted')
        else:
            print(f'{table_name} table does not have any entries to delete.')

    def get_count_of_entry(self, how_search_btn, what_search_btn,
                           how_search_input, what_search_input,
                           # how_input_close, what_input_close,
                           search_area_how, search_area_what,
                           search_data, table_name):
        count = 0
        column_data = self.search_from_table(how_search_btn, what_search_btn,
                                             how_search_input, what_search_input,
                                             # how_input_close, what_input_close,
                                             search_area_how, search_area_what, search_data, table_name)
        if len(column_data):
            for i in range(len(column_data)):
                if column_data[i] == search_data:
                    count += 1
        return count
