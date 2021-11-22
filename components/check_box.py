from ..pages.base_page import BasePage
from ..pages.base_page import is_element_equal


class CheckBox(BasePage):
    def check_checkbox_state(self, how, what, element):
        if self.is_element_present(how, what):
            check_box = self.browser.find_element(how, what).is_selected()
            print(f'{element}\'s value is {check_box}')
            return check_box
            # if not check_box:
            #     return False
            # else:
            #     return True
        else:
            print(f'{element} element is not visible!!!')

    def check_checkbox_label(self, how, what, element, label):
        if self.is_element_present(how, what):
            check_box_label = self.browser.find_element(how, what).text
            if is_element_equal(check_box_label, label):
                return True
            else:
                return False
        else:
            print(f'{element} element is not visible!!!')

    # def check_checkbox_accessibility(self):

    # def check_checkbox_error_message(self):