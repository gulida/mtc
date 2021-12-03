import time

from ..components.text_box import TextBox
from ..components.button import Button
from ..components.scroll_to_element import ScrollToElement
from ..base.base import form_inputs
from ..locators.tracker_common_locators import TrackerCommonLocators


class GridComponent(TextBox, Button, ScrollToElement):

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

    def get_table_entries_count(self, how, what):
        data = self.get_column_data(how, what)
        return len(data)

    def get_column_action_buttons(self, how, what):
        buttons = []
        found_buttons = self.browser.find_elements(how, what)
        for e in found_buttons:
            buttons.append(e)
        return buttons

    def search_from_table(self, how_search_btn, what_search_btn,
                          how_search_input, what_search_input,
                          search_area_how, search_area_what,
                          search_data, table_name):
        found_data_array = []
        # Checking if search input field is available
        if self.is_element_present(how_search_input, what_search_input):
            self.set_textbox_value(how_search_input, what_search_input, ' ', table_name)
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
            return found_data_array
        # If search input field is not available, first press SEARCH button
        elif self.is_element_present(how_search_btn, what_search_btn):
            self.click_button(how_search_btn, what_search_btn, 'SEARCH BUTTON')
            time.sleep(2)
            if self.is_element_present(how_search_input, what_search_input):
                self.set_textbox_value(how_search_input, what_search_input, ' ', table_name)
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
                return found_data_array
            else:
                print(f'{table_name} table does not have SEARCH FIELD...')
        # If there is no SEARCH button
        else:
            print(f'{table_name} table does not have SEARCH BUTTON...')

    def search_from_table_for_edit_delete(self, how_search_btn, what_search_btn,
                                          how_search_input, what_search_input,
                                          search_area_how, search_area_what,
                                          how_edit_btn, what_edit_btn,
                                          how_del_btn, what_del_btn,
                                          search_data, table_name):
        column_data = {}
        # Checking if search input field is available
        if self.is_element_present(how_search_input, what_search_input):
            self.set_textbox_value(how_search_input, what_search_input, ' ', table_name)
            self.set_textbox_value(how_search_input, what_search_input, search_data, table_name)
            next_arrow_flag = True
            time.sleep(3)
            while next_arrow_flag:
                found_data_array = []
                found_data = self.browser.find_elements(search_area_how, search_area_what)
                edit_btns = self.browser.find_elements(how_edit_btn, what_edit_btn)
                delete_btns = self.browser.find_elements(how_del_btn, what_del_btn)
                for data in found_data:
                    found_data_array.append(data.text)
                full_string = self.browser.find_element(*TrackerCommonLocators.SHOWED_ITEM_COUNT).text
                dict_key = full_string.split('-')[0]
                column_data.update({dict_key: [found_data_array, edit_btns, delete_btns]})
                next_button = self.browser.find_element(*TrackerCommonLocators.PAGINATION_NEXT_BUTTON)
                disabled_props = next_button.get_property('disabled')
                if not disabled_props:
                    next_button.click()
                    time.sleep(3)
                else:
                    next_arrow_flag = False
            return column_data
        # If search input field is not available, first press SEARCH button
        elif self.is_element_present(how_search_btn, what_search_btn):
            self.click_button(how_search_btn, what_search_btn, 'SEARCH BUTTON')
            time.sleep(2)
            if self.is_element_present(how_search_input, what_search_input):
                self.set_textbox_value(how_search_input, what_search_input, ' ', table_name)
                self.set_textbox_value(how_search_input, what_search_input, search_data, table_name)
                next_arrow_flag = True
                time.sleep(3)
                while next_arrow_flag:
                    found_data_array = []
                    found_data = self.browser.find_elements(search_area_how, search_area_what)
                    edit_btns = self.browser.find_elements(how_edit_btn, what_edit_btn)
                    delete_btns = self.browser.find_elements(how_del_btn, what_del_btn)
                    for data in found_data:
                        found_data_array.append(data.text)
                    full_string = self.browser.find_element(*TrackerCommonLocators.SHOWED_ITEM_COUNT).text
                    dict_key = full_string.split('-')[0]
                    column_data.update({dict_key: [found_data_array, edit_btns, delete_btns]})
                    next_button = self.browser.find_element(*TrackerCommonLocators.PAGINATION_NEXT_BUTTON)
                    disabled_props = next_button.get_property('disabled')
                    if not disabled_props:
                        next_button.click()
                        time.sleep(3)
                    else:
                        next_arrow_flag = False
                return column_data
            else:
                print(f'{table_name} table does not have SEARCH FIELD...')
        # If there is no SEARCH button
        else:
            print(f'{table_name} table does not have SEARCH BUTTON...')

    # ADD & EDIT
    # How it works:
    # data - json (dictionary in python) where you have new data
    def add_edit_catalog_data(self, how, what, data, element):
        data.pop('search_data')
        keys = data.keys()
        for key in keys:
            self.set_textbox_value(*form_inputs(key), data[key], element + '_' + str(key))
        time.sleep(2)
        self.click_button(how, what, element)
        time.sleep(2)

    # How it works:
    # column_data = self.search_from_table()
    # how_add_btn, what_add_btn - ADD BUTTON
    # new_entry_data - json (dictionary in python)  where you have new data
    # how_save_btn, what_save_btn - SAVE BUTTON of catalog form
    def add_catalog_table_entry(self, column_data, how_add_btn, what_add_btn,
                                new_entry_data, how_save_btn, what_save_btn,
                                table_name):
        add_flag = True
        if len(column_data):
            for i in range(len(column_data)):
                if column_data[i] == new_entry_data['search_data']:
                    print('This value is already exists in the table!!!')
                    add_flag = False
                    break
        if add_flag:
            # self.browser.execute_script("window.scrollTo(0, 0);")
            # element = self.browser.find_element(how_add_btn, what_add_btn)
            # coordinates = element.location_once_scrolled_into_view  # returns dict of X, Y coordinates
            # self.browser.execute_script('window.scrollTo({}, {});'.format(coordinates['x'], coordinates['y']))
            self.scroll_to_component(how_add_btn, what_add_btn)
            time.sleep(2)
            self.click_button(how_add_btn, what_add_btn, f'{table_name} ADD BUTTON')
            time.sleep(2)
            self.add_edit_catalog_data(how_save_btn, what_save_btn, new_entry_data, 'SAVE')
            print(f'New entry was added to {table_name} table!')
            time.sleep(2)

    # How it works:
    # column_data = self.search_from_table()
    # column_data_collection = self.search_from_table_for_edit_delete()
    # correct_data - json (dictionary in python)  where you have search data and new data
    def edit_catalog_table_entry(self, column_data, column_data_collection,
                                 correct_data, how_save_btn, what_save_btn, table_name):
        if len(column_data):
            message_flag = True
            break_flag = False
            for keys, items in column_data_collection.items():
                full_string = self.browser.find_element(*TrackerCommonLocators.SHOWED_ITEM_COUNT).text
                showed_item_count = full_string.split('-')[0]
                while int(keys) != int(showed_item_count):
                    if int(keys) < int(showed_item_count):
                        back_arrow = self.browser.find_element(*TrackerCommonLocators.PAGINATION_BACK_BUTTON)
                        back_arrow.click()
                        time.sleep(2)
                        full_string = self.browser.find_element(*TrackerCommonLocators.SHOWED_ITEM_COUNT).text
                        showed_item_count = full_string.split('-')[0]
                    elif int(keys) > int(showed_item_count):
                        next_arrow = self.browser.find_element(*TrackerCommonLocators.PAGINATION_NEXT_BUTTON)
                        next_arrow.click()
                        time.sleep(2)
                        full_string = self.browser.find_element(*TrackerCommonLocators.SHOWED_ITEM_COUNT).text
                        showed_item_count = full_string.split('-')[0]
                for i in range(len(items[0])):
                    if items[0][i] == correct_data['search_data']:
                        items[1][i].click()
                        time.sleep(3)
                        self.add_edit_catalog_data(how_save_btn, what_save_btn, correct_data, 'SAVE')
                        print(f'{table_name} table\'s entry was edited!')
                        message_flag = False
                        time.sleep(1)
                        break_flag = True
                        break
                if break_flag:
                    break

            if message_flag:
                print('Nothing was edited!!!')
        else:
            print(f'{table_name} table does not have any entries to edit.')

    # How it works:
    # column_data = self.search_from_table()
    # column_data_collection = self.search_from_table_for_edit_delete()
    # search data - string
    def press_edit_button_of_table_entry(self, column_data, column_data_collection,
                                         search_data, table_name):
        if len(column_data):
            message_flag = True
            break_flag = False
            for keys, items in column_data_collection.items():
                full_string = self.browser.find_element(*TrackerCommonLocators.SHOWED_ITEM_COUNT).text
                showed_item_count = full_string.split('-')[0]
                while int(keys) != int(showed_item_count):
                    if int(keys) < int(showed_item_count):
                        back_arrow = self.browser.find_element(*TrackerCommonLocators.PAGINATION_BACK_BUTTON)
                        back_arrow.click()
                        time.sleep(2)
                        full_string = self.browser.find_element(*TrackerCommonLocators.SHOWED_ITEM_COUNT).text
                        showed_item_count = full_string.split('-')[0]
                    elif int(keys) > int(showed_item_count):
                        next_arrow = self.browser.find_element(*TrackerCommonLocators.PAGINATION_NEXT_BUTTON)
                        next_arrow.click()
                        time.sleep(2)
                        full_string = self.browser.find_element(*TrackerCommonLocators.SHOWED_ITEM_COUNT).text
                        showed_item_count = full_string.split('-')[0]
                for i in range(len(items[0])):
                    if items[0][i] == search_data:
                        items[1][i].click()
                        time.sleep(3)
                        print(f'Edit button of {table_name} table entry\'s was pressed!')
                        message_flag = False
                        time.sleep(1)
                        break_flag = True
                        break
                if break_flag:
                    break

            if message_flag:
                print('Nothing was pressed!!!')
        else:
            print(f'{table_name} table does not have any entries to edit.')

    # How it works:
    # column_data = self.search_from_table()
    # column_data_collection = self.search_from_table_for_edit_delete()
    # search data - string
    # how_alert_ok_btn, what_alert_ok_btn - ACCEPT BUTTON on dialog window
    def delete_table_entry(self, column_data, column_data_collection, search_data,
                           how_alert_ok_btn, what_alert_ok_btn, table_name):
        if len(column_data):
            message_flag = True
            break_flag = False
            for keys, items in column_data_collection.items():
                full_string = self.browser.find_element(*TrackerCommonLocators.SHOWED_ITEM_COUNT).text
                showed_item_count = full_string.split('-')[0]
                while int(keys) != int(showed_item_count):
                    if int(keys) < int(showed_item_count):
                        back_arrow = self.browser.find_element(*TrackerCommonLocators.PAGINATION_BACK_BUTTON)
                        back_arrow.click()
                        time.sleep(2)
                        full_string = self.browser.find_element(*TrackerCommonLocators.SHOWED_ITEM_COUNT).text
                        showed_item_count = full_string.split('-')[0]
                    elif int(keys) > int(showed_item_count):
                        next_arrow = self.browser.find_element(*TrackerCommonLocators.PAGINATION_NEXT_BUTTON)
                        next_arrow.click()
                        time.sleep(2)
                        full_string = self.browser.find_element(*TrackerCommonLocators.SHOWED_ITEM_COUNT).text
                        showed_item_count = full_string.split('-')[0]
                for i in range(len(items[0])):
                    if items[0][i] == search_data:
                        items[2][i].click()
                        time.sleep(3)
                        self.click_button(how_alert_ok_btn, what_alert_ok_btn, 'CONFIRM DELETE')
                        print(f'{table_name} table\'s entry was deleted')
                        message_flag = False
                        time.sleep(1)
                        break_flag = True
                        break
                if break_flag:
                    break
            if message_flag:
                print('Nothing was deleted!!!')
        else:
            print(f'{table_name} table does not have any entries to delete.')

    def get_count_of_entry_by_search(self, how_search_btn, what_search_btn,
                                     how_search_input, what_search_input,
                                     search_area_how, search_area_what,
                                     search_data, table_name):
        count = 0
        column_data = self.search_from_table(how_search_btn, what_search_btn,
                                             how_search_input, what_search_input,
                                             search_area_how, search_area_what,
                                             search_data, table_name)
        if len(column_data):
            for i in range(len(column_data)):
                if column_data[i] == search_data:
                    count += 1
        return count
