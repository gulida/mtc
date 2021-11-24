from ..pages.base_page import BasePage
from ..pages.base_page import is_element_equal
from selenium.webdriver.support.color import Color


class Grid(BasePage):

    def check_card_visibility(self, how, what):
        return self.is_element_present(how, what)

    def search_element_in_grid(self, how, what, value, element):
        d = ''


    def add_new_element(self, how, what, value, element):
        if self.is_element_present(how, what):
            ff='cffi'
        else:
            print(f'{element} - element is not visible!!!')

