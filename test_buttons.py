import time

from .pages.executive_secretary_page import ExecutiveSecretaryPage
from .pages.main_page import MainPage
from .pages.user_cabinet_page import UserCabinetPage
from .pages.active_case_page import ActiveCasePage


def test_buttons(browser):
    link = "http://194.87.102.173:3004"
    page = MainPage(browser, link)
    page.open()
    page.test_login_button_visibility()
    time.sleep(5)
    # page.test_login_button_caption()
    # time.sleep(3)
    # page.test_login_button_color()
    page.test_username_field_visibility()
    time.sleep(3)
    page.test_username_sent_text()
    time.sleep(2)
    # page.test_username_check_text()
    # user_cabinet_page = UserCabinetPage(browser, browser.current_url)
    page.test_username_check_text_box_color()
    page.test_username_check_error_msg()
    time.sleep(10)