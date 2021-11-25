from ..base.base import Base
from ..base.base import is_element_equal


class CheckBox(Base):

    def check_checkbox_visibility(self, how, what):
        if self.is_element_present(how, what):
            return True
        else:
            return False

    def check_checkbox_state(self, how, what, element):
        if self.is_element_present(how, what):
            check_box = self.browser.find_element(how, what).is_selected()
            print(f'{element}\'s value is {check_box}')
            return check_box
        else:
            print(f'{element} element is not visible!!!')

    def check_checkbox_label(self, how, what, label, element):
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
