from ..pages.base_page import BasePage
from ..pages.base_page import is_element_equal
from selenium.webdriver.support.color import Color


class Button(BasePage):

    def check_button_visibility(self, how, what):
        return self.is_element_present(how, what)

    def check_button_caption(self, how, what, caption, btn):
        if self.is_element_present(how, what):
            button_caption = self.browser.find_element(how, what).text
            return is_element_equal(button_caption, caption)
        else:
            print(f'{btn} button is not visible!!!')

    def check_button_color(self, how, what, color, btn):
        if self.is_element_present(how, what):
            button_color = self.browser.find_element(how, what).value_of_css_property('background-color')
            color_hex = Color.from_string(button_color).hex
            print(f'{btn} - button\'s color is - {color_hex}...')
            return is_element_equal(color_hex, color)
        else:
            print(f'{btn} button is not visible!!!')

    def click_button(self, how, what, btn):
        if self.is_element_present(how, what):
            button = self.browser.find_element(how, what)
            button.click()
            print(f'{btn} - button was pressed...')
        else:
            print(f'{btn} button is not visible!!!')
