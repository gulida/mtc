from ..pages.base_page import BasePage
from ..pages.base_page import is_element_equal
from selenium.webdriver.support.color import Color


class Card(BasePage):

    def check_card_visibility(self, how, what):
        return self.is_element_present(how, what)


