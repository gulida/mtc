from ..locators.tracker_file_type_grid_locators import TrackerFileTypeLocators

from ..components.button import Button


class TrackerFileTypePage(Button):
    def test_file_type_table(self):
        column_count = 0
        columns = []
        table_name = self.browser.find_element(*TrackerFileTypeLocators.TABLE_NAME).text
        print('Table name: ', table_name)

        table_columns = self.browser.find_elements(*TrackerFileTypeLocators.TABLE_HEAD)
        column_count = len(table_columns) - 1

        for index in range(2, len(table_columns) + 1):
            if index == 2:
                table_column = self.browser.find_element_by_xpath(TrackerFileTypeLocators.HEAD_TITLE_LINK_START + str(
                    index) + ']/div')
                print(index, ' - ', table_column.text)
                columns.append(table_column.text)
            else:
                table_column = self.browser.find_element_by_xpath(TrackerFileTypeLocators.HEAD_TITLE_LINK_START + str(
                    index) + TrackerFileTypeLocators.HEAD_TITLE_LINK_END)
                print(index, ' - ', table_column.text)
                columns.append(table_column.text)

        print('Column count: ', column_count)
        print('Columns: ', columns)