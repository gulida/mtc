from ..locators.user_cabinet_locators import UserCabinetLocators

from ..components.buttons import Buttons
from ..components.text_box import TextBox


class UserCabinetPage(Buttons, TextBox):
    def test_pin_check_color_of_text_box(self):
        self.check_color_of_text_box(*UserCabinetLocators.PIN_FIELD, 'PIN', '#f44336')
